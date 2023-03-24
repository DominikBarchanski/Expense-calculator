from fastapi import FastAPI
from app.core import config
from app.db.sesion import create_database_tables
from app.api.api_v1 import api_router

app = FastAPI(title=config.settings.PROJECT_NAME, version="0.1.0")

app.include_router(api_router, prefix='/api/v1')


@app.on_event("startup")
async def startup_event():
    create_database_tables()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.", port=8000)
