"""Here are the API keys for work with clients and books"""

import json
import logging

from flask import Response, flash, jsonify, request

from project.apps import app_ as app
from project.apps import csrf
from project.logs import configure_logging
from project.transaction_some.transaction_borrow import Library_Borrow

configure_logging(logging.INFO)
log = logging.getLogger(__name__)


async def borrow_api_apth():

    @app.route("/api/v1/borrows/<int:index>/return", methods=["PATCH"])
    @csrf.exempt
    async def borrow_one_change(index):
        """
        Here, can change the one or everything Book's attributes from: \n
        - "book_id";
        - "client_id";
        - "date_borrow";
        - "date_borrow",
        'index', it is number a book which we want to change.
        Format the date is 'year.month.day' or 'year-month-day'.
        Request is
         ```json
            {
                "book_id": 1,
                "client_id": 1,
                "date_borrow": ...,
                "date_return": ...
                "quantity": ...
            }
        ``` or the single from over code. Example is the code below:
        ```jsom
        {
            "book_id": null,
            "client_id": 2,
            "date_borrow": null,
            "date_return": null,
            "quantity": null
        }
        # or
        {
            "author_id":2
        }
        ```
        Over is a code for an entrypoint.
        :param index: int. Index from db..
        :return: ```json
        {
            "message": "Ok", \n
            "result": true # or false \n
        }
        ``` and the status code = 200
        """
        data = json.loads(request.data)
        response = {"message": "Ok", "result": None}
        text = f"[{borrow_one_change.__name__}]:"
        log.info(f"{text} START")
        try:
            if not index:
                text = f"{text} 'index' is invalid."
            else:
                person = Library_Borrow()
                result: bool = await person.update(
                    index,
                    book_id_=data["book_id"] if data["book_id"] else None,
                    client_id_=data["client_id"] if data["client_id"] else None,
                    date_borrow_=data["date_borrow"] if data["date_borrow"] else None,
                    date_return_=data["date_return"] if data["date_return"] else None,
                    quantity_=data["quantity"] if data["quantity"] else None,
                )
                if not result:
                    response["message"] = "Not OK"
                text = f"{text}  END"
        except Exception as e:
            text = f"{text} Mistake => {e.__str__()}"
            response["message"] = text
        finally:
            log.info(text)
            return jsonify(response), 200

    @app.route("/api/v1/borrows", methods=["POST"])
    @csrf.exempt
    async def borrow_add() -> Response:
        """
        TODO: New borrow's line adds to the Model db's table
            - book_id_: int. The book's index from 'Book'.
            - client_id_: int. The Client's index from 'Client'.
            - date_borrow_: datetime. This is datetime when the client
         received a book.
            - date_return_: datetime. This is datetime when the client
         return a book.
        :return: bool. 'True' it means was created new line in db or not.
         If we received meaning 'False', it means what we receives
         a mis
                We create a request by API's reference ('/api/v1/books').
                Request's body contain:
                ```json
                    {
                        "book_id":...,
                        "client_id": ...,
                        "date_borrow": ...,
                        "date_return": ...,
                        "quantity": ...
                    }
                ```
                :return:```json
                    {"message": "Ok"} // or
                    // {"message":"[get_one] Something what wrong! False"}
                ```
        """
        data = json.loads(request.data)
        text = f"[{borrow_add.__name__}]:"
        log.info(f"{text} START")
        try:
            pass
            book = Library_Borrow()

            key_list = list(data.keys())
            if (
                "book_id" not in key_list
                or "client_id" not in key_list
                or "date_borrow" not in key_list
            ):
                text = f"{text} Does not have a 'book_id' or 'client_id' \
or 'date_borrow'"
                flash(text)
            else:
                date_return = data["date_return"] if data["date_return"] else None
                result = await book.add_one(
                    book_id_=data["book_id"] if data["book_id"] else None,
                    client_id_=data["client_id"] if data["client_id"] else None,
                    date_borrow_=data["date_borrow"] if data["date_borrow"] else None,
                    date_return_=date_return,
                    quantity_=data["quantity"] if data["quantity"] else 1,
                )
                text = f"{text}  END"
                if not result:
                    text = f"{text}  Something what wrong! False"
                    return jsonify({"message": text, "result": False}), 400

                return jsonify({"message": "Ok", "result": True}), 200
        except Exception as e:
            text = f"{text} Mistake => {e.__str__()}"
            raise ValueError(text)
        finally:
            flash(text)
            log.info(text)

    @app.route("/api/v1/borrows", methods=["GET"])
    @app.route("/api/v1/borrows/<int:index>", methods=["GET"])
    async def borrow_get(index: int = None):
        """
        We create a request by API's reference '/api/v1/borrows' and method "GET".
        It returns the all books from db.
        If, API's reference '/api/v1/borrows/{index}' this mean what we want getting
        one a book by ID.
        Request's body contain:
        :return:
        ```json
            {
            "message": "Ok",
            "result": [
                        {
                    "book_id": 1,
                    "client_id": 2,
                    "date_borrow": "Wed, 18 Dec 2024 07:49:19 GMT",
                    "date_return": null,
                    "index": 1
                    "quantity": < integer/None > # If, our the script not received\
the book's quantity. We will see the message "Mistake => Not received
a quantity. Something what wrong with the book quantity."
                },
            ]
        }

        ```
        or
        ```json
        {
            "message": "Ok",
            "result": false
        }
        # or
        {
            "message": "Not OK",
            "result": false
        }
        ``` if an index was, not found
        """
        response = {"message": "Ok", "result": None}
        text = f"[{borrow_get.__name__}]:"
        log.info(f"{text} START")
        status_code = 400
        try:
            person = Library_Borrow()
            result = await person.receive(index)
            if not result:
                response["message"] = "Not OK"
            response["result"] = result
            # CHACKER a QUANTITY
            """
            If the 'chacker_quantity' has length more when zero,
            for
            """
            chacker_quantity = [
                view for view in response["result"] if not view["quantity"]
            ]
            if len(chacker_quantity) > 0:
                text = f"{text} \
Mistake => Not received a quantity. Something what wrong with \
the book quantity."
                result["message"] = text

            text = f"{text}  END"
            status_code = 200
        except Exception as e:
            text = f"{text} Mistake => {e.__str__()}"
            response["message"] = text
        finally:
            log.info(text)
            return jsonify(response), status_code
