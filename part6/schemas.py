from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PredictIn(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class PredictOut(BaseModel):
    iris_class: int
