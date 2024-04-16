from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schema.campaign import Campaign, CampaignCreate
from app.service import campaign_service

router = APIRouter()


@router.post("/", response_model=Campaign)
def create_campaign(campaign: CampaignCreate, db: Session = Depends(get_db)):
    return campaign_service.create_campaign(db, campaign)


@router.get("/{campaign_id}", response_model=Campaign)
def read_campaign(campaign_id: int, db: Session = Depends(get_db)):
    db_campaign = campaign_service.get_campaign(db, campaign_id)
    if db_campaign is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return db_campaign


@router.put("/{campaign_id}", response_model=Campaign)
def update_campaign(campaign_id: int, campaign: Campaign, db: Session = Depends(get_db)):
    updated_campaign = campaign_service.update_campaign(db, campaign_id, campaign)
    if updated_campaign is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return updated_campaign
