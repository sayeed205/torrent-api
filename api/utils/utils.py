from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from api.utils.all_sites import all_sites as __all_sites


def is_site_available(site) -> bool:
    if site in __all_sites.keys():
        return True
    return False


def get_all_sites():
    return __all_sites


def error_handler(status_code, json_message):
    return JSONResponse(
        status_code=status_code,
        content=jsonable_encoder(json_message),
    )
