from fastapi import FastAPI, HTTPException

from database import SessionLocal, init_db
from models.trip import Trip
from schemas.trip import TripRequest, TripResponse
from services.trip_service import (
    get_default_recommendations,
    get_transportations,
    get_trip_category,
    calculate_daily_budget,
)

app = FastAPI(title="KelanaAI API")

init_db()

@app.get("/api/v1/recommendations")
def read_recommendations():
    return get_default_recommendations()

@app.get("/api/v1/transportations")
def read_transportations():
    return get_transportations()

@app.post("/api/v1/trips", response_model=TripResponse)
def create_trip(request: TripRequest):
    category = get_trip_category(request.budget)
    daily_budget = calculate_daily_budget(request.budget, request.days)

    trip = Trip(
        destination=request.destination,
        days=request.days,
        budget=request.budget,
        category=category,
        daily_budget=daily_budget,
    )

    db = SessionLocal()
    db.add(trip)
    db.commit()
    db.refresh(trip)
    db.close()

    return trip

@app.get("/api/v1/trips", response_model=list[TripResponse])
def list_trips():
    db = SessionLocal()
    trips = db.query(Trip).all()
    db.close()
    return trips

@app.get("/api/v1/trips/{trip_id}", response_model=TripResponse)
def get_trip(trip_id: int):
    db = SessionLocal()
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    db.close()

    if trip is None:
        raise HTTPException(status_code=404, detail=f"Trip with id {trip_id} not found")

    return trip

@app.put("/api/v1/trips/{trip_id}", response_model=TripResponse)
def update_trip(trip_id: int, request: TripRequest):
    db = SessionLocal()
    trip = db.query(Trip).filter(Trip.id == trip_id).first()

    if trip is None:
        db.close()
        raise HTTPException(status_code=404, detail=f"Trip with id {trip_id} not found")

    # recalculate category & daily_budget berdasarkan budget baru
    trip.destination = request.destination
    trip.days = request.days
    trip.budget = request.budget
    trip.category = get_trip_category(request.budget)
    trip.daily_budget = calculate_daily_budget(request.budget, request.days)

    db.commit()
    db.refresh(trip)
    db.close()

    return trip

@app.delete("/api/v1/trips/{trip_id}")
def delete_trip(trip_id: int):
    db = SessionLocal()
    trip = db.query(Trip).filter(Trip.id == trip_id).first()

    if trip is None:
        db.close()
        raise HTTPException(status_code=404, detail=f"Trip with id {trip_id} not found")

    db.delete(trip)
    db.commit()
    db.close()

    return {"message": f"Trip with id {trip_id} deleted successfully"}