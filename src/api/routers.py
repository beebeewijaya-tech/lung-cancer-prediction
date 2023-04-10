from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from src.model.response import Predict
from src.model.person import Person
from .controllers import predicting_lung_cancer

router = APIRouter(
    prefix="/v1",
    tags=["predict"]
)


@router.post("/predict")
async def predict(body: Person) -> Predict:
    result = predicting_lung_cancer(body)
    if result is None:
        raise HTTPException(
            status_code=400, detail="Failed to predict the data")

    p = Predict(
        message="Successfully predict the lung cancer person",
        is_lung_cancer=result
    )
    return p
