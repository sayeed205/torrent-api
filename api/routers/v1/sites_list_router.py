from fastapi import APIRouter, status

from api.utils.utils import error_handler, get_all_sites

router = APIRouter(tags=["Get all sites"])


@router.get("/")
@router.get("")
async def get_all_supported_sites():
    all_sites = get_all_sites()

    sites_list = [
        site for site in all_sites.keys() if all_sites[site]["website"]
    ]
    return error_handler(
        status_code=status.HTTP_200_OK,
        json_message={
            "supported_sites": sites_list,
        },
    )
