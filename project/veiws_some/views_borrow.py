import json
import logging
from datetime import datetime
from flask import (request, jsonify, flash, Response)
from project.apps import app_ as app
from project.models_some.model_borrow import Borrow
from project.models_some.model_autors import Author
from project.transaction_some.transaction_borrow import Library_Borrow
from project.transaction_some.transaction_person import Library_Person
from project.apps import csrf
from project.logs import configure_logging

configure_logging(logging.INFO)
log = logging.getLogger(__name__)

async def borrow_api_apth():
    
    @app.route("/api/v1/borrows", methods=["POST"])
    @csrf.exempt
    async def borrow_add() -> Response:
        data = json.loads(request.data)
        text = f"[{borrow_add.__name__}]:"
        log.info(f"{text} START")
        try:
            pass
            book = Library_Borrow()
            
            key_list = list(data.keys())
            if "book_id" not in key_list or "client_id" not in key_list or \
              "date_borrow" not in key_list:
                text = "".join(
                    f"{text} Does not have a 'book_id' or 'client_id' \
or 'date_borrow'"
                    )
                flash(text)
            else:
                date_return = \
                    data["date_return"] if data["date_return"] else None
                await book.add_one(
                    book_id_=data["book_id"] if data["book_id"] else None,
                    client_id_=data["client_id"] if data["client_id"] else None,
                    date_borrow_=data["date_borrow"] if data["date_borrow"]
                    else None,
                    date_return_= date_return,
                    )
                text = f"{text}  END"
                return jsonify({"message": text}), 200
        except Exception as e:
            text = f"{text} Mistake => {e.__str__()}"
            raise ValueError(text)
        finally:
            flash(text)
            log.info(text)