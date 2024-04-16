from pydantic import BaseModel
from typing import Optional


class Ad(BaseModel):
    id: int
    ad_group_set_id: int
    name: str
    identity: str
    ad_format: str
    headline: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    video_url: Optional[str] = None
    call_to_action: str
    landing_page_url: str

class AdCreate(BaseModel):
    ad_group_set_id: int
    name: str
    identity: str
    ad_format: str
    headline: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    video_url: Optional[str] = None
    call_to_action: str
    landing_page_url: str
