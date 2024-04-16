from fastapi import FastAPI
from app.controller import campaign_controller, ads_controller, ad_sets_controller

app = FastAPI()

app.include_router(campaign_controller.router, prefix="/api/v1/campaigns", tags=["campaigns"])
app.include_router(ad_sets_controller.ad_set_router, prefix="/api/v1/campaigns", tags=["ad_groups"])
app.include_router(ads_controller.ad_router, prefix="/api/v1/campaigns", tags=["ads"])
