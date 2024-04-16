from sqlalchemy.orm import Session
from app.model.ad_set import AdGroupSetORM


def create_ad_set(db: Session, ad_set_data: AdGroupSetORM):
    db_ad_set = AdGroupSetORM(**ad_set_data.dict())
    db.add(db_ad_set)
    db.commit()
    db.refresh(db_ad_set)
    return db_ad_set


def get_ad_set(db: Session, ad_set_id: int):
    return db.query(AdGroupSetORM).filter(AdGroupSetORM.id == ad_set_id).first()


def update_ad_set(db: Session, ad_set_id: int, ad_set_data: AdGroupSetORM):
    db_ad_set = db.query(AdGroupSetORM).filter(AdGroupSetORM.id == ad_set_id).first()
    if db_ad_set:
        for var, value in vars(ad_set_data).items():
            setattr(db_ad_set, var, value) if value else None
        db.commit()
        db.refresh(db_ad_set)
    return db_ad_set
