import yfinance as yf
from utils.sanitizar import sanitizar

COMPANY_TICKERS = {
    "microsoft": "MSFT",
    "apple": "AAPL",
    "google": "GOOGL",
    "amazon": "AMZN",
    "tesla": "TSLA",
    "meta": "META",
    "netflix": "NFLX",
    "nvidia": "NVDA"
}


def obtener_precio_accion(driver, user_input):
    try:
        texto = sanitizar(user_input)

        company = None

        for nombre in COMPANY_TICKERS:
            if nombre in texto:
                company = nombre
                break

        if company is None:
            return "No encontré la empresa"

        ticker = COMPANY_TICKERS[company]

        stock = yf.Ticker(ticker)

        data = stock.history(period="1d")

        if data.empty:
            return f"No hay datos para {ticker}"

        price = data["Close"].iloc[-1]

        currency = stock.info.get("currency", "USD")

        return f"{company} ({ticker}) → ${price:.2f} {currency}"

    except Exception as e:
        return f"Error yfinance: {e}"