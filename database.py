from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


engine = create_engine("sqlite:///weather.db")

Base = declarative_base()

class OpenWeatherAPIData(Base):
  __tableName__ = 'weather'
  cityName = Column(String, primary_key=True)
  weatherDescription = Column(String, nullable=False)
  cityTemp = Column(Float, nullable=False)
  humidity = Column(String, nullable=False)
  currentTime = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session();


