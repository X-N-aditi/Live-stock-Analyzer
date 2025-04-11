from django.core.management.base import BaseCommand
import yfinance as yf
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import time

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        stock_symbols = ["AAPL", "MSFT", "TSLA", "GOOGL", "AMZN", "META", "NFLX", "NVDA", "ADBE", "INTC"]
        channel_layer = get_channel_layer()
        while True:
            for symbol in stock_symbols:
                print(f"⏳ Fetching {symbol}...")

                stock = yf.Ticker(symbol)
                info = stock.info
                try:
                    current_price = info.get('currentPrice', 0)
                    open_price = info.get('open', 0)
                    prev_close = info.get('previousClose', 0)
                    volume = info.get('volume', 0)
                    change = round(current_price - prev_close, 2)
                except:
                    current_price = open_price = prev_close = volume = change = "N/A"
                
                print(f"✅ {symbol} -> Price: {current_price}, Change: {change}")

                data = {
                    "symbol": symbol,
                    "price": current_price,
                    "open": open_price,
                    "close": prev_close,
                    "change": change,
                    "volume": volume,
                }

                # ✅ Correctly indented inside the loop
                async_to_sync(channel_layer.group_send)(
                    "stocks",
                    {
                        "type": "send_stock_update",
                        "data": data
                    }
                )

                time.sleep(3)
