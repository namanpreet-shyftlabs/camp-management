import requests

from app.model.campaign import CampaignORM


def add_data_to_meta_account(campaign: CampaignORM):
    url = "https://graph.facebook.com/v15.0/act_id/campaigns"

    payload = {
        'access_token': '',
        'name': campaign.name,
        'status': 'PAUSED',
        'objective': campaign.objective,
        'special_ad_categories': '[]'
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Request successful!")
        print(response.json())
    else:
        print(f"Failed to create campaign. Status code: {response.status_code}")
        print(response.text)
