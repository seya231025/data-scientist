from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
import os
from app.services.titanic import analyze_titanic_data

# テンプレートディレクトリの設定
templates = Jinja2Templates(directory="app/templates")

app = FastAPI()

# 静的ファイル（CSS, JSなど）の設定
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    ホームページにタイタニック号データの分析結果を表示するルート。
    """
    # タイタニックデータの解析を実行
    result = analyze_titanic_data("csv/titanic.csv")

    # 結果をHTMLで表示
    return templates.TemplateResponse("result.html", {"request": request, "result": result})

@app.get("/routes")
async def list_routes():
    """
    アプリケーション内のすべてのルートをリスト表示するルート。
    """
    routes = [{"path": route.path, "name": route.name} for route in app.router.routes]
    return {"routes": routes}

@app.get("/boston", response_class=HTMLResponse)
async def boston(request: Request):
    return templates.TemplateResponse("boston.html", {"request": request})

@app.get("/customer", response_class=HTMLResponse)
async def customer(request: Request):
    return templates.TemplateResponse("customer.html", {"request": request})

@app.get("/iris", response_class=HTMLResponse)
async def iris(request: Request):
    return templates.TemplateResponse("iris.html", {"request": request})

@app.get("/store", response_class=HTMLResponse)
async def store(request: Request):
    return templates.TemplateResponse("store.html", {"request": request})
