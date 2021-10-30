#!/usr/bin/env python3
import requests
import json
from pprint import pprint

GAMES_ONLY = False
EXTENSION = 0

base_url = "https://auction.unityads.unity3d.com/"

extensions = [
    "v5/games/30871/requests",
    "v5/games/1000283/requests",
]

url = base_url + extensions[EXTENSION]

'''
The following keys existed in the params but weren't required.
Their values have been removed for privacy.

advertisingTrackingId
limitAdTracking
deviceModel
platform
sdkVersion
stores
osVersion
screenScale
connectionType
networkType

The dimension keys below are required, but can be of any value
'''
params = {
    "screenWidth": "1920",
    "screenHeight": "1080",
}

headers = {
    "Content-Type": "application/json",
#    "User-Agent": "" # This was the user agent of the requesting game, and isn't required.
}

'''
The following keys existed in the payload but weren't required.
Their values have been removed for privacy.

abGroup
agreedOverAgeLimit
bundleId
bundleVersion
cachedCampaigns
coppa
developerId
deviceFreeSpace
ext
    ad_load_duration
    device_battery_charging
    device_battery_level
    device_incapabilities
    granular_speed_bucket
    ios_jailbroken
    iu_sizes
    mobile_device_submodel
    network_metered
    prior_click_count
    prior_user_requests
    seq_num
frameworkName
frameworkVersion
gameSessionCounters
    adRequests
    latestCampaignsStarts
    starts
    startsPerCampaign
    startsPerTarget
    views
    viewsPerCampaign
    viewsPerTarget
gameSessionId
gdprEnabled
isLoadEnabled
isPromoCatalogAvailable
language
legalFramework
networkOperator
networkOperatorName
omidJSVersion
omidPartnerName
optOutEnabled
optOutRecorded
organizationId
privacy
    firstRequest
    method
    permissions
        ads
        external
        gameExp
projectId
requestSignal
sessionDepth
simulator
timeZone
volume
webviewUa
wiredHeadset

The key/values below are required, but can be manipulated as shown below.
'''
json_payload = {
    'placements': {
        'defaultRewardedPlacement': {
            'adTypes': [
                'MRAID',
                'VIDEO',
            ],
            'allowSkip': False,
            'auctionType': 'cpm',
        },
        'defaultVideoAndPictureZone': {
            'adTypes': [
                'MRAID',
                'VIDEO',
                'DISPLAY',
            ],
            'allowSkip': True,
            'auctionType': 'cpm',
        },
        'rewardedVideo': {
            'adTypes': [
                'MRAID',
                'VIDEO',
            ],
            'allowSkip': False,
            'auctionType': 'cpm',
        },
        'video': {
            'adTypes': [
                'MRAID',
                'VIDEO',
            ],
            'allowSkip': True,
            'auctionType': 'cpm',
        }
    },
    'properties': '' # this seems to be a required base64 string
    'token': '' # this seems to be a required JWT
    'webviewUa': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1', 
}

if GAMES_ONLY:
    for key in json_payload["placements"]:
        json_payload["placements"][key]["adTypes"] = ["MRAID"]

r = requests.post(
    url=url,
    params=params,
    json=json_payload,
    headers=headers,
)

media = r.json()["media"]
print(json.dumps(media))
