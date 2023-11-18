from loader import dp

from . import basic
# from . import admin


dp.include_routers(
    basic.router, 
    # admin.router
    )