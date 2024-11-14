import logging
from fastapi import FastAPI
from datetime import datetime
from src.scheduler import scheduler
from contextlib import asynccontextmanager
from src.database import engine
from src.model import Base
from src.consumer import consume_messages
import asyncio


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()
    consume_messages()
    yield
    print("App Closed.")


app = FastAPI(
    title="Kafka Example App",
    description="",
    version="0.0.1",
    # openapi_tags=tags,
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
    lifespan=lifespan
)

# 데이터베이스 테이블 생성 (애플리케이션 시작 시 한 번 호출)
Base.metadata.create_all(bind=engine)

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

