import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from api.routers.v1.sites_list_router import router as sites_list_router

# from routers.v1.sites_list_router import router as site_list_router

app = FastAPI()


@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}


app.include_router(sites_list_router, prefix="/api/v1/sites")


handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
