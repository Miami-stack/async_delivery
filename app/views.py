import json
from typing import Callable, Dict
import jsonschema
from aiohttp.web import Response, View
from app import db
from app.schema import SCHEMA


def json_validation(input_json: Dict, schema: Dict = SCHEMA) -> [bool, Dict]:
    """Функция для валидации json."""
    try:
        jsonschema.validate(input_json, schema)
        return input_json
    except jsonschema.exceptions.ValidationError:
        print("Невалидный json")
        return False


class HealthView(View):
    """Вью, созданное лишь для возможности проверить жив ли сервис."""

    async def get(self) -> Response:
        """Хелсчек сервиса."""
        return Response(status=200)


class CheckStatus(View):
    async def get(self):
        engine = self.request.app["engine"]
        psq_db = await db.select_data(engine)
        return Response(status=200, body=json.dumps(psq_db))


class CreateGoods(View):

    def json_validation(self: Dict, schema: Dict = SCHEMA) -> [bool, Dict]:
        """Функция для валидации json."""
        try:
            jsonschema.validate(self, schema)
            return self
        except jsonschema.exceptions.ValidationError:
            print("Невалидный json")
            return False

    async def post(self):
        data = await self.request.json()
        if json_validation(data) is True:
            id = data["identificator"]
            status = data["status"]
            data2 = {"identificator": id, "status": status}
            engine = self.request.app["engine"]
            psq_db_post = await db.insert(data2, engine)
            return Response(status=200, body=json.dumps(psq_db_post))
