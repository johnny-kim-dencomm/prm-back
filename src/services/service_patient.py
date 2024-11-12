from fastapi_sqlalchemy import db
from sqlalchemy.exc import SQLAlchemyError

from src.models import model_patient

def get_patient_list():
    try:
        result = db.session.query(model_patient.PatientInfo)
        return result.all()
    except SQLAlchemyError as e:
        raise e


def get_partient(patient_no: int):
    try:
        result = db.session.query(model_patient.PatientInfo).filter(model_patient.PatientInfo.patient_no == patient_no)
        return result.first()
    except SQLAlchemyError as e:
        raise e