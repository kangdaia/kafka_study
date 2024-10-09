from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import Column, Integer, String
from src.database import Base


class StockData(Base):
    __tablename__ = "stock_data"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    open_price = Column(String)
    volume = Column(Integer)
    timestamp = Column(String)


class StockMessage(BaseModel):
    symbol: str  # 주식 티커 (문자열)
    open_price: float  # 주식의 오픈 가격 (실수형)
    volume: int  # 거래량 (정수형)
    timestamp: datetime  # 타임스탬프 (datetime 객체)

    class Config:
        orm_mode = True