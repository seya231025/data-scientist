# app/api/endpoints.py

from fastapi import APIRouter
from app.services.titanic import analyze_titanic_data

router = APIRouter()

@router.get("/titanic-analysis")
def get_titanic_analysis():
    result = analyze_titanic_data("data/titanic.csv")
    return result
