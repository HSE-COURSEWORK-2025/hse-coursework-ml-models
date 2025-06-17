import enum
from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text,
    Enum as SQLEnum,
    ForeignKey
)
from sqlalchemy.sql import expression
from sqlalchemy.orm import declarative_base, relationship
from models.models import DataType


Base = declarative_base()


class RawRecords(Base):
    __tablename__ = "raw_records"

    id = Column(Integer, primary_key=True, index=True)
    data_type = Column(String, nullable=False)
    email = Column(String, nullable=False, index=True)
    time = Column(DateTime(timezone=True), nullable=False, index=True)
    value = Column(Text, nullable=False)



class OutliersRecords(Base):
    __tablename__ = "outliers_records"

    id = Column(Integer, primary_key=True, index=True)
    raw_record_id = Column(Integer, ForeignKey("raw_records.id"), nullable=False)

    outliers_search_iteration_num = Column(Integer, nullable=False)
    outliers_search_iteration_datetime = Column(DateTime(timezone=True), nullable=False)

    raw_record = relationship("RawRecords", backref="outlier_record", uselist=False)


class MLPredictionsRecords(Base):
    __tablename__ = "ml_predictions_records"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)

    result_value = Column(Text, nullable=False)
    diagnosis_name = Column(Text, nullable=False)

    iteration_num = Column(Integer, nullable=False)
    iteration_datetime = Column(DateTime(timezone=True), nullable=False)
