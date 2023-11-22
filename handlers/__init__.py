from loader import dp

from . import basic
from . import shop


dp.include_routers(
    basic.router
    ,shop.router
    )