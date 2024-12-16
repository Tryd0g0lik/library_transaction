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
        
    