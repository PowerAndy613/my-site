# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import yfinance as yf
import os

app = FastAPI(title="yfinance proxy")

# 允許前端網址（測試可先用 '*'，上線請改成你的 Pages 網域如 https://PowerAndy613.github.io）
allowed = os.getenv("ALLOWED_ORIGINS", "*")
if allowed == "*":
    origins = ["*"]
else:
    origins = [o.strip() for o in allowed.split(",")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/history/{ticker}")
def get_history(ticker: str, start: str = None, end: str = None):
    """
    GET /history/AAPL?start=YYYY-MM-DD&end=YYYY-MM-DD
    Returns JSON: {"data": [{"date": "YYYY-MM-DD", "close": 123.45}, ...]}
    """
    try:
        t = yf.Ticker(ticker)
        df = t.history(start=start if start else None, end=end if end else None)
        if df is None or df.empty:
            return {"data": []}
        df = df.reset_index()
        rows = []
        for _, row in df.iterrows():
            date_val = row["Date"]
            try:
                date_str = str(date_val.date())
            except Exception:
                date_str = str(date_val)
            rows.append({"date": date_str, "close": float(row["Close"])})
        return {"data": rows}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
