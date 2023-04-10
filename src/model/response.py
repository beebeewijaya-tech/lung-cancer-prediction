from pydantic import BaseModel
from typing import Optional


class Predict(BaseModel):
    message: Optional[str] = ""
    is_lung_cancer: Optional[bool] = False
