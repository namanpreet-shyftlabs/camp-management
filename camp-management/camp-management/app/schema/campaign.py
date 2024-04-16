from pydantic import BaseModel
from typing import Optional
from datetime import date


class Campaign(BaseModel):
    id: int
    name: str
    platform: str  # Google Ads or Meta Ads
    objective: str
    daily_budget: float
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    bidding_strategy: str
    bid_amount: Optional[float] = None

class CampaignCreate(BaseModel):
    name: str
    platform: str  # Google Ads or Meta Ads
    objective: str
    daily_budget: float
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    bidding_strategy: str
    bid_amount: Optional[float] = None
