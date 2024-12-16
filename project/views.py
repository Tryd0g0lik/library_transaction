from datetime import datetime
from flask import (request, jsonify, flash, Response)
from project.apps import app_ as app
from project.models_some.model_autors import Author
from project.transaction_some.transaction_book import Library_book
from project.transaction_some.transaction_borrow import Library_Borrow
from project.transaction_some.transaction_person import Library_Person


@app.route("/api/v1/authors", methods=["GET"])
def author_path():
    response = {"massage": "", "result": None}
    try:
        person = Library_Person(Author)
        response["result"] = person.receive()
    except Exception as e:
        response["message"] = f"{e.__str__()}"
    finally:
        return jsonify(response)
        
@app.route("/api/v1/authors", methods=["POST"])
def author_add() -> Response:
    data = request.json()
    text = "Everything went well."
    try:
        persone = Library_Person(Author)
        key_list = list(data.keys())
        if "firstname" not in key_list or "secondname" not in key_list:
            text = "Does not have a 'firstname' or 'secondname'"
            flash(text)
        else:
            birthday = \
                data["birthday"] if data["birthday"] else datetime.utcnow
            persone.add_one(data["fisrtname"], data["secondname"],
                            birthday)
            flash(text)
    except Exception as e:
        text = f"Mistake => {e.__str__()}"
    finally:
        return jsonify({"message": text})
    