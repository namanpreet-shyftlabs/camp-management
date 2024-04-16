from sqlalchemy.orm import Session
from app.model.ad import AdORM


def create_ad(db: Session, ad_data: AdORM):
    db_ad = AdORM(**ad_data.dict())
    db.add(db_ad)
    db.commit()
    db.refresh(db_ad)
    return db_ad


def get_ad(db: Session, ad_id: int):
    return db.query(AdORM).filter(AdORM.id == ad_id).first()


def update_ad(db: Session, ad_id: int, ad_data: AdORM):
    db_ad = db.query(AdORM).filter(AdORM.id == ad_id).first()
    if db_ad:
        for var, value in vars(ad_data).items():
            setattr(db_ad, var, value) if value else None
        db.commit()
        db.refresh(db_ad)
    return db_ad
