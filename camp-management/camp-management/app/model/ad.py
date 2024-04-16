from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class AdORM(Base):
    __tablename__ = 'ads'

    id = Column(Integer, primary_key=True, index=True)
    ad_group_set_id = Column(Integer, ForeignKey('ad_group_sets.id'))
    name = Column(String, nullable=False)
    identity = Column(String, nullable=False)
    ad_format = Column(String, nullable=False)
    headline = Column(String)
    description = Column(String)
    image_url = Column(String)
    video_url = Column(String)
    call_to_action = Column(String, nullable=False)
    landing_page_url = Column(String, nullable=False)

    # Relationship
    ad_group_set = relationship("AdGroupSetORM", back_populates="ads")
