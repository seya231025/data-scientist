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
    ホームページにHTMLフォームを表示するルート。
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/routes")
async def list_routes():
    """
    アプリケーション内のすべてのルートをリスト表示するルート。
    """
    routes = [{"path": route.path, "name": route.name} for route in app.router.routes]
    return {"routes": routes}

@app.post("/analyze_titanic_data")
async def analyze_titanic_data_view(request: Request, file: UploadFile = File(...)):
    """
    アップロードされたタイタニックのデータCSVを解析し、その結果をHTMLで表示するルート。
    """
    # アップロードされたファイルを一時保存
    file_path = f"temp/{file.filename}"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # tempフォルダがない場合は作成
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # アップロードされたファイルのパスを使用して分析
    result = analyze_titanic_data(file_path)

    # 一時ファイルの削除
    os.remove(file_path)

    print(result)

    # 結果をHTMLで表示
    return templates.TemplateResponse("result.html", {"request": request, "result": result})
