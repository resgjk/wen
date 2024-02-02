from utils import config

from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware


app = FastAPI(title="SWEN")
app.add_middleware(SessionMiddleware, secret_key=config.SECRET_KEY)
templates = Jinja2Templates(directory="frontend/templates")
app.mount(
    "/app/frontend/static", StaticFiles(directory="frontend/static"), name="static"
)


@app.get("/airdrop", response_class=HTMLResponse)
@app.get("/", response_class=HTMLResponse)
async def airdop_page(request: Request):
    context = {
        "title": "$WEN AIRDROP",
        "choise": "airdrop",
        "wallet_is_correct": True,
        "is_airdrop_time": True,
    }
    return templates.TemplateResponse(
        request=request,
        name="airdrop.html",
        context=context,
    )


@app.get("/claim", response_class=HTMLResponse)
async def calim_page(request: Request):
    context = {
        "title": "$WEN CLAIM",
        "choise": "airdrop",
        "all_tweets_is_subscribe": True,
    }
    return templates.TemplateResponse(
        request=request,
        name="claim.html",
        context=context,
    )


@app.get("/farm", response_class=HTMLResponse)
async def farm_page(request: Request):
    context = {"title": "$WEN FARM", "choise": "farm", "is_all_connect": True}
    return templates.TemplateResponse(
        request=request,
        name="farm.html",
        context=context,
    )
