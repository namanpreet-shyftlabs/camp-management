from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schema.ad import Ad, AdCreate
from app.service import ad_service
from app.database import get_db

ad_router = APIRouter()


@ad_router.post("/", response_model=Ad)
def create_ad(ad: AdCreate, db: Session = Depends(get_db)):
    return ad_service.create_ad(db, ad)


@ad_router.get("/{ad_id}", response_model=Ad)
def read_ad(ad_id: int, db: Session = Depends(get_db)):
    db_ad = ad_service.get_ad(db, ad_id)
    if db_ad is None:
        raise HTTPException(status_code=404, detail="Ad not found")
    return db_ad


@ad_router.put("/{ad_id}", response_model=Ad)
def update_ad(ad_id: int, ad: Ad, db: Session = Depends(get_db)):
    updated_ad = ad_service.update_ad(db, ad_id, ad)
    if updated_ad is None:
        raise HTTPException(status_code=404, detail="Ad not found")
    return updated_ad
