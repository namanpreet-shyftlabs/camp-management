from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship

from app.database import Base


class CampaignORM(Base):
    __tablename__ = 'campaigns'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    platform = Column(String, nullable=False)  # Google Ads or Meta Ads
    objective = Column(String, nullable=False)
    daily_budget = Column(Float, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    bidding_strategy = Column(String, nullable=False)
    bid_amount = Column(Float)

    ad_group_sets = relationship("AdGroupSetORM", back_populates="campaign")
