import requests
from datetime import datetime
import json
from super_secret import auth

# import personal token from 'super_secret' file.
TOKEN = auth

# Resturant ID (for Grubhub)
SAXBY_STORE_ID = "-15428134"
D_ANGELO_STORE_ID= "-14912550"
CHOOLAH_STORE_ID= "-14908827"
STARBUCKS_STORE_ID= "-11204191"
SUBWAY_STORE_ID= "-11204205"
KIGO_KITCHEN_STORE_ID= "-11201780"
POPEYES_STORE_ID= "-11202811"
SWEET_TOMATOES_STORE_ID= "-11202822"
TUE_TACO_STORE_ID= "-11201935"

# Current date in ISO format (required by API endpoint).
d = datetime.utcnow().isoformat() + 'Z'

STORE_ID_dc = {"Saxby": SAXBY_STORE_ID, 
               "D'Angelo's": D_ANGELO_STORE_ID,
               "Choolah": CHOOLAH_STORE_ID,
               "Starbucks": STARBUCKS_STORE_ID,
               "Subway": SUBWAY_STORE_ID,
               "Kigo Kitchen": KIGO_KITCHEN_STORE_ID,
               "Popeyes": POPEYES_STORE_ID,
               "Sweet Tomatoes": SWEET_TOMATOES_STORE_ID,
               "Tue Taco": TUE_TACO_STORE_ID}

# store final results here. 
api = {}

# pass a GET request for each store, and append them to API dictionary. 
for store_name in STORE_ID_dc:
    r = requests.get(
    f"https://api-gtm.grubhub.com/tapingo/restaurants/v4/{STORE_ID_dc[store_name]}?hideChoiceCategories=true&hideOutOfStock=false&hideUnavailableMenuItems=true&location=POINT%28-71.09111786%2042.33698272%29&orderType=PICKUP&time={d}&variationId=default&zipCode=02115",
    
    # data needed by the API to allow access to data.
    headers={
        "Authorization": f"Bearer {TOKEN}",
        "User-agent": "GrubHub/2024.38 (iPhone; iOS 17.6.1; Scale/3.00)",
        "Data": TOKEN
    }
    
)

    api[store_name] = r.json()
    

# add the collected data into the output file in a JSON format.
with open('grubhub_neu_scrubbing.json', 'w') as w:
    json.dump(api, w, indent = 4)
