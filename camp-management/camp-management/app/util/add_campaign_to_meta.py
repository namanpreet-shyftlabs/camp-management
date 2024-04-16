import requests

from app.model.campaign import CampaignORM


def add_data_to_meta_account(campaign: CampaignORM):
    url = "https://graph.facebook.com/v15.0/act_1378888112738553/campaigns"

    payload = {
        'access_token': 'EAAfKXwEvzoYBOwetMTotWGKbqA4vrOfGOKKtpBLw6IsMCKJQdyLMSxr3B3zZBuqCte5VaC39YSeOhgAZC2ulmcUB1yL8WUJZBAVTuYH8GEvPzYgGCt7gbanNnfQaTTKTQYVIdSm4y59kltHcXbUb3dqhHnfH6hZBjQYejECzLpa7h8bZB7pygSEnWPZAPLWL6utwZDZD',
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
