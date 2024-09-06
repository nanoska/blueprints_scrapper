# Importo librerias

import requests
import os
from dotenv import load_dotenv

# %%
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", None)
GOOGLE_SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID", None)

# %%

google_api_url = "https://www.googleapis.com/customsearch/v1?"
lang = "lang_es"
init_page = 1
query = "blueprints"

# %%

url = f"{google_api_url}key={GOOGLE_API_KEY}&cx={GOOGLE_SEARCH_ENGINE_ID}&q={query}&start={init_page}&{lang}"
response = requests.get(url)
data = response.json()

# %%

results = data["items"]

for result in results:
    print(result["title"])
    print(result["link"])
    print(result["snippet"])
    print("\n")


# %%

