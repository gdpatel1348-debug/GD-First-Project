from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    role = Column(String, nullable=False) # 'factory_admin', 'banker', 'regulator'

class Factory(Base):
    __tablename__ = 'factories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    industry = Column(String, nullable=False)
    location = Column(String, nullable=False)
    
class SensorData(Base):
    __tablename__ = 'sensor_data'
    id = Column(Integer, primary_key=True)
    factory_id = Column(Integer, ForeignKey('factories.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)
    pm25 = Column(Float)
    pm10 = Column(Float)
    co2 = Column(Float)
    nox = Column(Float)
    sox = Column(Float)
    voc = Column(Float)
    is_tampered = Column(Boolean, default=False) # Cryptographic identity validation

class EnergyUsage(Base):
    __tablename__ = 'energy_usage'
    id = Column(Integer, primary_key=True)
    factory_id = Column(Integer, ForeignKey('factories.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)
    kwh_consumption = Column(Float)
    power_factor = Column(Float)
    peak_demand = Column(Float)
    renewable_share = Column(Float)

class WaterQuality(Base):
    __tablename__ = 'water_quality'
    id = Column(Integer, primary_key=True)
    factory_id = Column(Integer, ForeignKey('factories.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)
    ph = Column(Float)
    tds = Column(Float)
    bod = Column(Float)
    cod = Column(Float)
    heavy_metals = Column(Float)

class WasteMetrics(Base):
    __tablename__ = 'waste_metrics'
    id = Column(Integer, primary_key=True)
    factory_id = Column(Integer, ForeignKey('factories.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)
    hazardous_waste_vol = Column(Float)
    recycling_percentage = Column(Float)
    landfill_diversion_rate = Column(Float)

class CarbonEmissions(Base):
    __tablename__ = 'carbon_emissions'
    id = Column(Integer, primary_key=True)
    factory_id = Column(Integer, ForeignKey('factories.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)
    scope1 = Column(Float)
    scope2 = Column(Float)
    scope3 = Column(Float)
    total_co2e = Column(Float)

class FinancialData(Base):
    __tablename__ = 'financial_data'
    id = Column(Integer, primary_key=True)
    factory_id = Column(Integer, ForeignKey('factories.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)
    revenue = Column(Float)
    profit = Column(Float)
    debt = Column(Float)
    credit_score = Column(Float)
    banking_data_verified = Column(Boolean, default=True)

class GreenScores(Base):
    __tablename__ = 'green_scores'
    id = Column(Integer, primary_key=True)
    factory_id = Column(Integer, ForeignKey('factories.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)
    green_credit_score = Column(Float)
    green_impact_score = Column(Float)

# Initialize Setup Function
def init_db(db_uri='sqlite:///ecocredit.db'):
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
