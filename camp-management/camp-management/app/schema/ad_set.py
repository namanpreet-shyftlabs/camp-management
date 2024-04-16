from pydantic import BaseModel
from typing import Optional, List


class AdGroupSet(BaseModel):
    id: int
    campaign_id: int
    name: str
    geographic_targeting: str
    language_targeting: str
    age_targeting: str
    keywords: Optional[List[str]] = []
    keyword_match_types: Optional[List[str]] = []

class AdGroupSetCreate(BaseModel):
    campaign_id: int
    name: str
    geographic_targeting: str
    language_targeting: str
    age_targeting: str
    keywords: Optional[List[str]] = []
    keyword_match_types: Optional[List[str]] = []