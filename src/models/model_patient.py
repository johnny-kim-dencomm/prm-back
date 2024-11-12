from datetime import datetime
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import TIME
from src.database import Base


class PatientInfo(Base):
    __tablename__ = "patient_info"

    patient_no: int | Column = Column(Integer, name="patient_no", primary_key=True, unique=True, nullable=False)
    patient_nm: str | Column = Column(String(100), name="patient_nm", nullable=False)
    phone_no: str | Column = Column(String(30), name="phone_no", nullable=False)
    email: str | Column = Column(String(255), name="email", nullable=True)
    use_yn: str | Column = Column(String(1), name="use_yn", default="Y")
    created_by: str | Column = Column(String(30), name="created_by")
    created_at: datetime | Column = Column(TIME, name="created_at")
    updated_by: str | Column = Column(String(30), name="updated_by")
    updated_at: datetime | Column = Column(TIME, name="updated_at")