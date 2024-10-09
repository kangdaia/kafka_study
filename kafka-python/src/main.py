import logging
from fastapi import FastAPI
from datetime import datetime
from src.scheduler import scheduler
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()
    yield


app = FastAPI(
    title="Kafka Example App",
    description="",
    version="0.0.1",
    # openapi_tags=tags,
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
    lifespan=lifespan
)

# configure log
logging.basicConfig(level=logging.DEBUG, filename=f'log/{datetime.now().strftime("%Y-%m-%d")}.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

origins = [
    "http://localhost:8088",
]

@app.get("/", summary="Health Check")
async def root():
    logger.debug("Root endpoint accessed")
    return {"CONNECT"}