import urllib

from fastapi import FastAPI
import json
from services.scraper import Scraper
from services.dataformater import Formater

app = FastAPI()


@app.get("/")
async def root():
    return str()


@app.get("/str")
async def test_request():
    # scraper = Scraper(2021)
    # scraper.download_pdfs()
    formatter = Formater(2022)
    formatter.create_csvs_from_text()
    return "a"


