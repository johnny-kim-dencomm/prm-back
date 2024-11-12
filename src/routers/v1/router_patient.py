from fastapi import APIRouter, HTTPException, status, Path

from src.services import service_patient

router = APIRouter(
    prefix="/api/v1",
    tags=["API"]
)


@router.get("/patients")
async def get_api_v1_patients():
    try:
        return service_patient.get_patient_list()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=repr(e))


@router.get("/patient/{patient_no}")
async def get_api_v1_patient(
    patient_no: int = Path(title="patient_no", description="환자번호")
):
    try:
        return service_patient.get_partient(patient_no=patient_no)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=repr(e))