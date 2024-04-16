from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, ARRAY
from sqlalchemy.orm import relationship

from app.database import Base

class AdGroupSetORM(Base):
    __tablename__ = 'ad_group_sets'

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey('campaigns.id'))
    name = Column(String, nullable=False)
    geographic_targeting = Column(String, nullable=False)
    language_targeting = Column(String, nullable=False)
    age_targeting = Column(String, nullable=False)
    keywords = Column(ARRAY(String))
    keyword_match_types = Column(ARRAY(String))

    # Relationships
    campaign = relationship("CampaignORM", back_populates="ad_group_sets")
    ads = relationship("AdORM", back_populates="ad_group_set")
