import json
import logging
from datetime import datetime
from flask import (request, jsonify, flash, Response)
from project.apps import app_ as app
from project.models_some.model_autors import Author
from project.transaction_some.transaction_person import Library_Person
from project.apps import csrf
from project.logs import configure_logging

configure_logging(logging.INFO)
log = logging.getLogger(__name__)


@app.route("/api/v1/authors/<int:index>", methods=["DELETE"])
@csrf.exempt
def author_one_remove(index):
    """
    
    :param index:
    :return: ```json
    {
        "massage": "Ok",
        "result": true # or false
    }
    ```
    """
    response = {"massage": "Ok", "result": None}
    text = f"[{author_one_get.__name__}]:"
    log.info(f"{text} START")
    try:
        if not index:
            text = f"{text} 'index' is invalid."
            raise ValueError(text)
    
        person = Library_Person(Author)
        response["result"] = person.removing(index)
        text = "".join(f"{text}  END")
    except Exception as e:
        text = "".join(f"{text} Mistake => {e.__str__()}")
        response["message"] = text
    finally:
        log.info(text)
        return jsonify(response), 400
@app.route("/api/v1/authors/<int:index>", methods=["GET"])
def author_one_get(index):
    """
    Receive tha one author by index.
    :return ```json
    {
        "massage": "",
        "result": [
            {
                "birthday": "2024-12-17T00:03:55.776287",
                "firstname": "Igor",
                "secondname": "Igorev"
            }
        ]
    }
    ```
    """
    response = {"massage": "Ok", "result": None}
    text = f"[{author_one_get.__name__}]:"
    log.info(f"{text} START")
    try:
        if not index:
            text = f"{text} 'index' is invalid."
            raise ValueError(text)
        
        person = Library_Person(Author)
        response["result"] = person.receive(index)
        text = "".join(f"{text}  END")
    except Exception as e:
        text = "".join(f"{text} Mistake => {e.__str__()}")
        response["message"] = text
    finally:
        log.info(text)
        return jsonify(response), 200

@app.route("/api/v1/authors", methods=["GET"])
def author_get():
    """

    :return:
    ```json
        {
        "massage": "",
        "result": [
            {
                "birthday": "2024-12-17T00:03:55.776287",
                "firstname": "Igor",
                "secondname": "Igorev"
            }
        ]

    ```
    """
    response = {"massage": "Ok", "result": None}
    text = f"[{author_get.__name__}]:"
    log.info(f"{text} START")
    try:
        person = Library_Person(Author)
        response["result"] = person.receive()
        text = "".join(f"{text}  END")
    except Exception as e:
        text = "".join(f"{text} Mistake => {e.__str__()}")
        response["message"] = text
    finally:
        log.info(text)
        return jsonify(response), 200


@app.route("/api/v1/authors", methods=["POST"])
@csrf.exempt
def author_add() -> Response:
    data = json.loads(request.data)
    text = f"[{author_add.__name__}]:"
    log.info(f"{text} START")
    try:
        persone = Library_Person(Author)
        key_list = list(data.keys())
        if "firstname" not in key_list or "secondname" not in key_list:
            text = "".join(
                f"{text}  Does not have a 'firstname' or 'secondname'"
                )
            flash(text)
        else:
            birthday = \
                data["birthday"] if data["birthday"] else datetime.utcnow()
            persone.add_one(
                firstname_=data["firstname"],
                secondname_=data["secondname"],
                birthday_=birthday
                )
            text = "".join(f"{text}  END")
    
    except Exception as e:
        text = "".join(f"{text}Mistake => {e.__str__()}")
    finally:
        flash(text)
        log.info(text)
        return jsonify(
            {"message": text}, status=200, mimetype='application/json'
            )
