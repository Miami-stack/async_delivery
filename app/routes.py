from aiohttp import web

from app.views import HealthView, CheckStatus, CreateGoods, UpdateGoods


def inject_routes(app: web.Application) -> None:
    """Инициализация роутов."""
    app.add_routes(
        [
            web.view("/heartbeat", HealthView),
            web.view("/checkstatus", CheckStatus),
            web.view("/creategoods", CreateGoods),
            web.view("/updategoods", CreateGoods)
        ]
    )
