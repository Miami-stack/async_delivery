import json
from typing import Callable, Dict
import jsonschema
from aiohttp.web import Response, View
from app import db
from app.schema import SCHEMA


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

    async def post(self):
        data = await self.request.json()
        jsonschema.validate(data, schema=SCHEMA)
        engine = self.request.app["engine"]
        psq_db_post = await db.insert_data(data, engine)
        print(psq_db_post)
        print(type(psq_db_post))
        return Response(status=200, body=json.dumps(data))


class UpdateGoods(View):

    async def post(self):
        data = await self.request.json()
        jsonschema.validate(data, schema=SCHEMA)
        engine = self.request.app["engine"]
        psq_db_post = await db.update_data(data, engine)
        print(psq_db_post)
        print(type(psq_db_post))
        return Response(status=200, body=json.dumps(data))
