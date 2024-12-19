"""Here are the API keys for work with clients"""

import json
import logging
from datetime import datetime

from flask import Response, flash, jsonify, request

from project.apps import app_ as app
from project.apps import csrf
from project.logs import configure_logging
from project.models_some.model_client import Client
from project.transaction_some.transaction_person import Library_Person

configure_logging(logging.INFO)
log = logging.getLogger(__name__)


async def сlient_api_path():
    @app.route("/api/v1/clients/<int:index>", methods=["PUT"])
    @csrf.exempt
    async def сlient_one_change(index):
        """
        Here, can change the one or everything Client's attribute from: \n
        - 'firstname';
        - 'birthday'.

        Request is
         ```json
            {
                "firstname": "Igor77", \n
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
        text = f"[{сlient_one_get.__name__}]:"
        log.info(f"{text} START")
        try:
            if not index:
                text = f"{text} 'index' is invalid."
                raise ValueError(text)

            person = Library_Person(Client)
            response["result"] = await person.update(
                index,
                new_firstname_=data["firstname"] if data["firstname"] else "",
                new_birthday_=data["birthday"] if data["birthday"] else None,
            )
            text = "".join(f"{text}  END")
        except Exception as e:
            text = "".join(f"{text} Mistake => {e.__str__()}")
            response["message"] = text
        finally:
            log.info(text)
            return jsonify(response), 200

    @app.route("/api/v1/clients/<int:index>", methods=["DELETE"])
    @csrf.exempt
    async def сlient_one_remove(index):
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
        text = f"[{сlient_one_get.__name__}]:"
        log.info(f"{text} START")
        try:
            if not index:
                text = f"{text} 'index' is invalid."
                raise ValueError(text)

            person = Library_Person(Client)
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

    @app.route("/api/v1/clients/<int:index>", methods=["GET"])
    async def сlient_one_get(index):
        """
        Receive tha one client by index.
        :return ```json
        {
            "message": "",
            "result": [
                {
                    "birthday": "2024-12-17T00:03:55.776287",
                    "firstname": "Igor"
                }
            ]
        }
        ```
        """
        response = {"message": "Ok", "result": None}
        text = f"[{сlient_one_get.__name__}]:"
        log.info(f"{text} START")
        try:
            if not index:
                text = f"{text} 'index' is invalid."
                raise ValueError(text)

            person = Library_Person(Client)
            response["result"] = await person.receive(index)
            text = "".join(f"{text}  END")
        except Exception as e:
            text = "".join(f"{text} Mistake => {e.__str__()}")
            response["message"] = text
        finally:
            log.info(text)
            return jsonify(response), 200

    @app.route("/api/v1/clients", methods=["GET"])
    async def сlient_get():
        """
         We create a request by API's reference '/api/v1/clients' and method "GET".
            It returns everything clients from db.
        :return:
        ```json
            {
            "message": "",
            "result": [
                {
                    "birthday": "2024-12-17T00:03:55.776287",
                    "firstname": "Igor",
                }
            ]

        ```
        """
        response = {"message": "Ok", "result": None}
        text = f"[{сlient_get.__name__}]:"
        log.info(f"{text} START")
        try:
            person = Library_Person(Client)
            response["result"] = await person.receive()
            text = "".join(f"{text}  END")
        except Exception as e:
            text = "".join(f"{text} Mistake => {e.__str__()}")
            response["message"] = text
        finally:
            log.info(text)
            return jsonify(response), 200

    @app.route("/api/v1/clients", methods=["POST"])
    @csrf.exempt
    async def сlient_add() -> Response:
        data = json.loads(request.data)
        text = f"[{сlient_add.__name__}]:"
        log.info(f"{text} START")
        try:
            persone = Library_Person(Client)
            key_list = list(data.keys())
            if "firstname" not in key_list:
                text = "".join(f"{text}  Does not have a 'firstname'")
                flash(text)
            else:
                birthday = data["birthday"] if data["birthday"] else datetime.utcnow()
                await persone.add_one(
                    firstname_=data["firstname"] if data["firstname"] else "",
                    birthday_=birthday,
                )
                text = f"{text}  END"
                return jsonify({"message": text}), 200
        except Exception as e:
            text = f"{text}Mistake => {e.__str__()}"
            raise ValueError(text)
        finally:
            flash(text)
            log.info(text)
