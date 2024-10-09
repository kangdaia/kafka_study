from apscheduler.schedulers.background import BackgroundScheduler
from src.config import settings
import aiohttp
import json
import asyncio


scheduler = BackgroundScheduler()


async def fetch_stock_data(session, ticker):
    BASE_URL = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": ticker,  # 원하는 주식 티커
        "interval": "1min",  # 데이터 간격
        "apikey": settings.alpha_vantage_key  # API 키
    }
    async with session.get(BASE_URL, params=params) as response:
        if response.status == 200:
            data = await response.json()
            time_series = data.get('Time Series (1min)', {})
            latest_time = next(iter(time_series))  # 가장 최근의 데이터 시간
            latest_data = time_series[latest_time]
            
            topic = f"stock_data_{ticker}"
            message = {
                "symbol": params['symbol'],
                "open_price": float(latest_data['1. open']),
                "volume": int(latest_data['5. volume']),
                "timestamp": latest_time
            }
            serialized_message = json.dumps(message).encode('utf-8')
            #produce_message(topic, message)
            print(f"Message sent to Kafka: {message}")
        else:
            print(f"Failed to fetch data from API. Status code: {response.status}")


async def fetch_all_symbols_stocks():
    symbols = ["NVDA", "GOOG", "SNOW", "IBM", "COST"]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_stock_data(session, symbol) for symbol in symbols]
        await asyncio.gather(*tasks)  # 모든 티커에 대한 요청을 병렬로 처리


def run_fetch_stock_data():
    asyncio.run(fetch_all_symbols_stocks())


scheduler.add_job(run_fetch_stock_data, 'interval', minutes=1)