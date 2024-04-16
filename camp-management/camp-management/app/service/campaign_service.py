from sqlalchemy.orm import Session
from app.model.campaign import CampaignORM


def create_campaign(db: Session, campaign: CampaignORM):
    db_campaign = CampaignORM(**campaign.dict())
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)
    return db_campaign


def get_campaign(db: Session, campaign_id: int):
    return db.query(CampaignORM).filter(CampaignORM.id == campaign_id).first()


def update_campaign(db: Session, campaign_id: int, campaign_data: CampaignORM):
    db_campaign = db.query(CampaignORM).filter(CampaignORM.id == campaign_id).first()
    if db_campaign is None:
        return None
    for var, value in vars(campaign_data).items():
        setattr(db_campaign, var, value) if value else None
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)
    return db_campaign
