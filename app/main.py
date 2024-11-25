from fastapi import FastAPI, UploadFile, File
from app.services.titanic import analyze_titanic_data
from app.api.endpoints import router  # エンドポイントのルーターをインポート

import os

app = FastAPI()

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "FastAPI is running!"}

@app.get("/routes")
async def list_routes():
    routes = [{"path": route.path, "name": route.name} for route in app.router.routes]
    return {"routes": routes}


@app.post("/analyze_titanic_data")
async def get_titanic_analysis(file: UploadFile = File(...)):
    # アップロードされたファイルを一時ファイルとして保存
    with open(f"temp/{file.filename}", "wb") as buffer:
        buffer.write(await file.read())

    # 一時ファイルのパスを関数に渡す
    result = analyze_titanic_data(f"temp/{file.filename}")

    # 一時ファイルを削除
    os.remove(f"temp/{file.filename}")

    return result