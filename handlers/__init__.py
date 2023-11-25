from loader import dp

from . import basic
from . import shop
from . import admin

dp.include_routers(
    basic.router
    ,shop.router
    ,admin.router
    )