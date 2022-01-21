import urllib

from fastapi import FastAPI
import json
from services.scraper import Scraper

app = FastAPI()


@app.get("/")
async def root():
    return str()


@app.get("/str")
async def test_request():
    scraper = Scraper(2022)
    scraper.download_pdfs()
    return "a"


