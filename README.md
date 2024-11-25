仮想環境起動　venv\Scripts\activate
パッケージインストール　pip install -r requirements.txt
定期更新　pip freeze > requirements.txt
起動方法　uvicorn app,main:app --reload