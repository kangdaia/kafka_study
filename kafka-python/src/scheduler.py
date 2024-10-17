from apscheduler.schedulers.background import BackgroundScheduler
from src.config import settings
from src.producer import produce_message
import aiohttp
import json
import asyncio


scheduler = BackgroundScheduler()


async def fetch_weather_data(session, city):
    BASE_URL = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": settings.weather_api_key,  # API 키
        "q": city
    }
    async with session.get(BASE_URL, params=params) as response:
        if response.status == 200:
            data = await response.json()
            city = city.replace(" ", "_")
            topic = f"weather_data_{city}"

            produce_message(topic, data["current"])
            print(f"Message sent to Kafka: {data}")
        else:
            print(f"Failed to fetch data from API. Status code: {response.status}")


async def fetch_all_cities_weathers(cities):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_weather_data(session, city) for city in cities]
        await asyncio.gather(*tasks)  # 모든 티커에 대한 요청을 병렬로 처리


def run_fetch_weather_data(cities=["Seoul", "Paris", "New York", "Seattle", "Sydney"]):
    asyncio.run(fetch_all_cities_weathers(cities))


scheduler.add_job(run_fetch_weather_data, 'interval', minutes=1)