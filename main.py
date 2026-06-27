from fastapi import FastAPI
import yfinance as yf
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 加上 CORS，讓 GitHub Pages 可以呼叫
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/history/{ticker}")
def get_history(ticker: str, start: str, end: str):
    data = yf.download(ticker, start=start, end=end)
    close_prices = data['Close'].to_dict()
    return {"ticker": ticker, "close": close_prices}
