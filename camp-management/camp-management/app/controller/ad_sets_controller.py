from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schema.ad_set import AdGroupSet, AdGroupSetCreate
from app.service import ad_sets_service
from app.database import get_db

ad_set_router = APIRouter()

@ad_set_router.post("/", response_model=AdGroupSet)
def create_ad_set(ad_set: AdGroupSetCreate, db: Session = Depends(get_db)):
    return ad_sets_service.create_ad_set(db, ad_set)

@ad_set_router.get("/{ad_set_id}", response_model=AdGroupSet)
def read_ad_set(ad_set_id: int, db: Session = Depends(get_db)):
    db_ad_set = ad_sets_service.get_ad_set(db, ad_set_id)
    if db_ad_set is None:
        raise HTTPException(status_code=404, detail="Ad set not found")
    return db_ad_set

@ad_set_router.put("/{ad_set_id}", response_model=AdGroupSet)
def update_ad_set(ad_set_id: int, ad_set: AdGroupSet, db: Session = Depends(get_db)):
    updated_ad_set = ad_sets_service.update_ad_set(db, ad_set_id, ad_set)
    if updated_ad_set is None:
        raise HTTPException(status_code=404, detail="Ad set not found")
    return updated_ad_set
