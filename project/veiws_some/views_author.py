"""Here are the API keys for work with authors"""

import json
import logging
from datetime import datetime

from flask import Response, flash, jsonify, request

from project.apps import app_ as app
from project.apps import csrf
from project.logs import configure_logging
from project.models_some.model_autors import Author
from project.transaction_some.transaction_person import Library_Person

configure_logging(logging.INFO)
log = logging.getLogger(__name__)


async def author_api_path():
    @app.route("/api/v1/authors/<int:index>", methods=["PUT"])
    @csrf.exempt
    async def author_one_change(index):
        """
        TODO: Here, can change the one or everything data from Author's table of db.\
          You can will change the all properties, this is 'firstname', 'secondname' and \
          'birthday' or only one from everything properties.
        Here, can change the one or everything Author's attribute from: \n
        - 'firstname';
        - 'secondname';
        - 'birthday'.
        Format the date is 'year.month.day' or 'year-month-day'.
        Request is
         ```json
            {
                "firstname": "Igor77", \n
                "secondname": null, // or 'Igorev' \n
                "birthday": null // or '1980.06.25'
            }
        ```
        Over is a code for an entrypoint.
        :param index: int. Index.
        :return: ```json
        {
            "message": "Ok",
            "result": true # or false
        }
        ``` and the status code = 200
        """
        data = json.loads(request.data)
        response = {"message": "Ok", "result": None}
        text = f"[{author_one_get.__name__}]:"
        log.info(f"{text} START")
        status_code = 200
        try:
            if not index:
                text = f"{text} 'index' is invalid."
                response["message"] = "Not Ok"
                status_code = 400
                raise ValueError(text)

            person = Library_Person(Author)
            response["result"] = await person.update(
                index,
                new_firstname_=data["firstname"] if data["firstname"] else "",
                new_secondname_=data["secondname"] if data["secondname"] else "",
                new_birthday_=data["birthday"] if data["birthday"] else None,
            )
            if not response["result"]:
                response["message"] = "Not Ok"
            text = "".join(f"{text}  END")
        except Exception as e:
            status_code = 400
            text = "".join(f"{text} Mistake => {e.__str__()}")
            response["message"] = text
            response["message"] = "Not Ok"
        finally:
            log.info(text)
            return jsonify(response), status_code

    @app.route("/api/v1/authors/<int:index>", methods=["DELETE"])
    @csrf.exempt
    async def author_one_remove(index):
        """

        :param index:
        :return: ```json
        {
            "message": "Ok",
            "result": true # or false
        }
        ```
        """
        response = {"message": "Ok", "result": None}
        text = f"[{author_one_get.__name__}]:"
        log.info(f"{text} START")
        try:
            if not index:
                text = f"{text} 'index' is invalid."
                raise ValueError(text)

            person = Library_Person(Author)
            result = await person.removing(index)
            if not result:
                response["message"] = "Not OK"

            response["result"] = result
            text = "".join(f"{text}  END")
        except Exception as e:
            text = "".join(f"{text} Mistake => {e.__str__()}")
            response["message"] = text
        finally:
            log.info(text)
            return jsonify(response), 400

    @app.route("/api/v1/authors/<int:index>", methods=["GET"])
    async def author_one_get(index):
        """
        Receive tha one author by index.
        :return ```json
        {
            "message": "",
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
        response = {"message": "Ok", "result": None}
        text = f"[{author_one_get.__name__}]:"
        log.info(f"{text} START")
        try:
            if not index:
                text = f"{text} 'index' is invalid."
                raise ValueError(text)

            person = Library_Person(Author)
            response["result"] = await person.receive(index)
            text = "".join(f"{text}  END")
        except Exception as e:
            text = "".join(f"{text} Mistake => {e.__str__()}")
            response["message"] = text
        finally:
            log.info(text)
            return jsonify(response), 200

    @app.route("/api/v1/authors", methods=["GET"])
    async def author_get():
        """
         We create a request by API's reference '/api/v1/authors' and method "GET".
            It returns everything authors from db.
        :return:
        ```json
            {
            "message": "",
            "result": [
                {
                    "birthday": "2024-12-17T00:03:55.776287",
                    "firstname": "Igor",
                    "secondname": "Igorev"
                }
            ]

        ```
        """
        response = {"message": "Ok", "result": None}
        text = f"[{author_get.__name__}]:"
        log.info(f"{text} START")
        try:
            person = Library_Person(Author)
            response["result"] = await person.receive()
            text = "".join(f"{text}  END")
        except Exception as e:
            text = "".join(f"{text} Mistake => {e.__str__()}")
            response["message"] = text
        finally:
            log.info(text)
            return jsonify(response), 200

    @app.route("/api/v1/authors", methods=["POST"])
    @csrf.exempt
    async def author_add() -> Response:
        data = json.loads(request.data)
        text = f"[{author_add.__name__}]:"
        log.info(f"{text} START")
        try:
            persone = Library_Person(Author)
            key_list = list(data.keys())
            if "firstname" not in key_list or "secondname" not in key_list:
                text = "".join(f"{text}  Does not have a 'firstname' or 'secondname'")
                flash(text)
            else:
                birthday = data["birthday"] if data["birthday"] else datetime.utcnow()
                await persone.add_one(
                    firstname_=data["firstname"] if data["firstname"] else "",
                    secondname_=data["secondname"] if data["secondname"] else "",
                    birthday_=data["birthday"] if data["birthday"] else None,
                )
                text = f"{text}  END"
                return jsonify({"message": text}), 200
        except Exception as e:
            text = f"{text}Mistake => {e.__str__()}"
            raise ValueError(text)
        finally:
            flash(text)
            log.info(text)
