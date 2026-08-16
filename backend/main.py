from fastapi import FastAPI
from services.trip_service import get_default_recommendations, get_transportations

app = FastAPI(title="KelanaAI API")


@app.get("/api/v1/recommendations")
def read_recommendations():
    return get_default_recommendations()


@app.get("/api/v1/transportations")
def read_transportations():
    return get_transportations()