from api.torrents.x1337 import x1337 as __x1337

all_sites = {
    "1337x": {
        "website": __x1337,
        "trending_available": True,
        "trending_category": True,
        "search_by_category": True,
        "recent_available": True,
        "recent_category_available": True,
        "categories": [
            "anime",
            "music",
            "games",
            "tv",
            "apps",
            "documentaries",
            "other",
            "xxx",
            "movies",
        ],
        "limit": 100,
    },
}
