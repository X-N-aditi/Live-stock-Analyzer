from django.shortcuts import render

def home(request):
    stock_symbols = ["AAPL", "MSFT", "TSLA", "GOOGL", "AMZN", "META", "NFLX", "NVDA", "ADBE", "INTC"]
    return render(request, 'analyzer/dashboard.html', {'stock_symbols': stock_symbols})
