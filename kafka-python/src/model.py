from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, Boolean, Text
from src.database import Base


class WeatherData(Base):
    __tablename__ = 'weather_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    last_updated_epoch = Column(Integer, nullable=False)
    last_updated = Column(String, nullable=False)
    temp_c = Column(Float, nullable=False)
    temp_f = Column(Float, nullable=False)
    is_day = Column(Boolean, nullable=False)
    condition = Column(Text, nullable=False)
    wind_mph = Column(Float, nullable=False)
    wind_kph = Column(Float, nullable=False)
    wind_degree = Column(Integer, nullable=False)
    wind_dir = Column(String, nullable=False)
    pressure_mb = Column(Float, nullable=False)
    pressure_in = Column(Float, nullable=False)
    precip_mm = Column(Float, nullable=False)
    precip_in = Column(Float, nullable=False)
    humidity = Column(Integer, nullable=False)
    cloud = Column(Integer, nullable=False)
    feelslike_c = Column(Float, nullable=False)
    feelslike_f = Column(Float, nullable=False)
    windchill_c = Column(Float, nullable=False)
    windchill_f = Column(Float, nullable=False)
    heatindex_c = Column(Float, nullable=False)
    heatindex_f = Column(Float, nullable=False)
    dewpoint_c = Column(Float, nullable=False)
    dewpoint_f = Column(Float, nullable=False)
    vis_km = Column(Float, nullable=False)
    vis_miles = Column(Float, nullable=False)
    uv = Column(Float, nullable=False)
    gust_mph = Column(Float, nullable=False)
    gust_kph = Column(Float, nullable=False)