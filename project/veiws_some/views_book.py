"""Here are the API keys for work with books"""
import json
import logging
from flask import (request, jsonify, flash, Response)
from project.apps import app_ as app
from project.transaction_some.transaction_book import Library_book
from project.apps import csrf
from project.logs import configure_logging

configure_logging(logging.INFO)
log = logging.getLogger(__name__)

async def book_api_path():
    @app.route("/api/v1/books/<int:index>", methods=["PUT"])
    @csrf.exempt
    async def book_one_change(index):
        """
        Here, can change the one or everything Book's attributes from: \n
        - "author_id";
        - "descriptions";
        - "index";
        - "quantity";
        - "title". Or the single attribute for changes. Index's attribute,
        it is number a book which we want to change.
    
        Request is
         ```json
            {
                "title":"title Big book",
                "descriptions":"descriptions descriptions ",
                "author_id":1,
                "quantity":24
            }
        ``` or the single from over code. Example is the code below:
        ```jsom
        {
            "title":null,
            "descriptions":null,
            "author_id":2,
            "quantity":null
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
        text = f"[{book_one_change.__name__}]:"
        log.info(f"{text} START")
        try:
            if not index:
                text = f"{text} 'index' is invalid."
            else:
                person = Library_book()
                result: bool = await person.update(
                    index,
                    new_title_=data["title"] if data["title"] else "",
                    new_descriptions_=data["descriptions"] if data["descriptions"]
                    else "",
                    new_author_id_=data["author_id"] if data["author_id"] else "",
                    new_quantity_=data["quantity"] if data["quantity"] else "",
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
        
    @app.route("/api/v1/books/<int:index>", methods=["DELETE"])
    @csrf.exempt
    async def book_one_remove(index:int = None):
        """
        We create a request by API's reference '/api/v1/books/{index}'
        and method "DELETE".
        This mean what we want getting one a book by ID.
        :return if everything is the OK, it means we will get the ```json
        {
            "message": "Ok",
            "result": true
        } or not the OK ```json
        {
            "message": "Not OK",
            "result": false
        }
        ```
        """
        response = {"message": "Ok", "result": None}
        text = f"[{book_get.__name__}]:"
        log.info(f"{text} START")
        status_code = 400
        try:
            person = Library_book()
            result: bool = await person.removing(index)
            if not result:
                response["message"] = "Not OK"
            response["result"] = result
            text = f"{text}  END"
            
        except Exception as e:
            text = f"{text} Mistake => {e.__str__()}"
            response["message"] = text
        finally:
            log.info(text)
            return jsonify(response), status_code
        
    @app.route("/api/v1/books", methods=["GET"])
    @app.route("/api/v1/books/<int:index>", methods=["GET"])
    async def book_get(index:int = None):
        """
        We create a request by API's reference '/api/v1/books' and method "GET".
        It returns the all books from db.
        If, API's reference '/api/v1/books/{index}' this mean what we want getting
        one a book by ID.
        Request's body contain:
        :return:
        ```json
            {
                "message": "Ok",
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
        or
        ```json
        {
            "message": "Ok",
            "result": false
        }
        ``` if an index was, not found
        """
        response = {"message": "Ok", "result": None}
        text = f"[{book_get.__name__}]:"
        log.info(f"{text} START")
        status_code = 400
        try:
            person = Library_book()
            result = await person.receive(index)
            if not result:
                response["message"] = "Not OK"
            response["result"] = result
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
    async def book_add() -> Response:
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
                result = await persone.add_one(
                    title_=data["title"] if data["title"] else "",
                    descriptions_=data["descriptions"] if data["descriptions"]
                    else "",
                    author_id_=data["author_id"] if data["author_id"] else "",
                    quantity_=data["quantity"] if data["quantity"] else "",
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
    
