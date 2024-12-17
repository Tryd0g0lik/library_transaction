import json
import logging
from datetime import datetime
from flask import (request, jsonify, flash, Response)
from project.apps import app_ as app
from project.models_some.model_autors import Author
from project.transaction_some.transaction_book import Library_book
from project.transaction_some.transaction_person import Library_Person
from project.apps import csrf
from project.logs import configure_logging

configure_logging(logging.INFO)
log = logging.getLogger(__name__)


@app.route("/api/v1/books", methods=["GET"])
def book_get():
    """

    :return:
    ```json
        {
            "massage": "Ok",
            "result": [
                {
                    "author_id": 2,
                    "descriptions": "descriptions descriptions ",
                    "index": 1,
                    "quantity": 24,
                    "title": "title of book"
                }
            ]
        }

    ```
    """
    response = {"massage": "Ok", "result": None}
    text = f"[{book_get.__name__}]:"
    log.info(f"{text} START")
    status_code = 400
    try:
        person = Library_book()
        response["result"] = person.receive()
        text = f"{text}  END"
        status_code = 200
    except Exception as e:
        text = f"{text} Mistake => {e.__str__()}"
        response["message"] = text
    finally:
        log.info(text)
        return jsonify(response), status_code

@app.route("/api/v1/books", methods=["POST"])
@csrf.exempt
def book_add() -> Response:
    """
    We create a request by API's reference ('/api/v1/books').
    Request's body contain:
    ```json
        {
            "title":"title of book",
            "descriptions":"descriptions descriptions ",
            "author_id":2,
            "quantity":24
        }
    ```
    :return:```json
        {"message": "Ok"} // or
        // {"message":"[get_one] Something what wrong! False"}
    ```
    """
    data = json.loads(request.data)
    text = f"[{book_add.__name__}]:"
    log.info(f"{text} START")
    try:
        persone = Library_book()
        key_list = list(data.keys())
        if "title" not in key_list or "descriptions" not in key_list or\
            "author_id" not in key_list or "quantity" not in key_list:
            text = "".join(
                f"{text}  Does not have a 'title' or 'descriptions', \
or 'author_id', or 'quantity'"
            )
            flash(text)
        else:
            result = persone.add_one(
                title_=data["title"],
                descriptions_=data["descriptions"],
                author_id_=int(data["author_id"]),
                quantity_=int(data["quantity"])
            )
            text = f"{text}  END"
            if not result:
                text = f"{text}  Something what wrong! False"
                return jsonify({"message": text}), 400
                
            return jsonify({"message": "Ok"}), 200
    except Exception as e:
        text = f"{text}Mistake => {e.__str__()}"
        raise ValueError(text)
    finally:
        flash(text)
        log.info(text)

