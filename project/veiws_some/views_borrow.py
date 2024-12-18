import json
import logging
from datetime import datetime
from flask import (request, jsonify, flash, Response)
from project.apps import app_ as app
from project.models_some.model_borrow import Borrow
from project.models_some.model_autors import Author
from project.transaction_some.transaction_person import Library_Person
from project.apps import csrf
from project.logs import configure_logging

configure_logging(logging.INFO)
log = logging.getLogger(__name__)

async def borrow_api_apth():
    @app.route("/api/v1/authors", methods=["POST"])
    @csrf.exempt
    async def borrow_add() -> Response:
        data = json.loads(request.data)
        text = f"[{borrow_add.__name__}]:"
        log.info(f"{text} START")
        try:
            pass
            # persone = Library_Person(Author)
            # key_list = list(data.keys())
            # if "firstname" not in key_list or "secondname" not in key_list:
            #     text = "".join(
            #         f"{text}  Does not have a 'firstname' or 'secondname'"
            #         )
            #     flash(text)
            # else:
            #     birthday = \
            #         data["birthday"] if data["birthday"] else datetime.utcnow()
            #     await persone.add_one(
            #         firstname_=data["firstname"] if data["firstname"] else "",
            #         secondname_=data["secondname"] if data[
            #             "secondname"] else "",
            #         birthday_=data["birthday"] if data["birthday"] else None
            #         )
            #     text = f"{text}  END"
            #     return jsonify({"message": text}), 200
        except Exception as e:
            text = f"{text}Mistake => {e.__str__()}"
            raise ValueError(text)
        finally:
            flash(text)
            log.info(text)