import requests
from fastapi import FastAPI, HTTPException
from starlette import status

from presentation.const import API_PREFIX

app = FastAPI()


@app.get("/{country_code}/{postal_code}")
async def get_location_information(country_code: str, postal_code: str):
    url = f"{API_PREFIX}/{country_code}/{postal_code}"
    response = requests.get(url=url)
    if response.status_code != status.HTTP_200_OK:
        raise HTTPException(status_code=response.status_code, detail=response.reason)
    return response.json()
