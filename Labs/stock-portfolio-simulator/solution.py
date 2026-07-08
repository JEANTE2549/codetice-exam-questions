class Portfolio:
    def __init__(self, cash, stocks):
        self.cash = cash
        self.stocks = stocks

    def buy_stock(self, ticker, qty, price):
        cost = qty * price
        if self.cash < cost:
            print(f"Failed: Not enough cash to buy {qty} {ticker}.")
            return

        self.cash -= cost
        self.stocks[ticker] = self.stocks.get(ticker, 0) + qty
        print(f"Bought {qty} {ticker} for {cost:.2f} Baht. Cash: {self.cash:.2f} Baht.")

    def sell_stock(self, ticker, qty, price):
        if self.stocks.get(ticker, 0) < qty:
            print(f"Failed: Not enough {ticker} shares to sell {qty}.")
            return

        income = qty * price
        self.cash += income
        self.stocks[ticker] -= qty
        if self.stocks[ticker] == 0:
            del self.stocks[ticker]

        print(f"Sold {qty} {ticker} for {income:.2f} Baht. Cash: {self.cash:.2f} Baht.")

    def show_portfolio(self):
        print(f"Cash: {self.cash:.2f} Baht")
        print("Stocks:")
        if not self.stocks:
            print("None")
            return

        for ticker in sorted(self.stocks):
            print(f"{ticker}: {self.stocks[ticker]}")


cash = float(input())
stock_count = int(input())
stocks = {}

for _ in range(stock_count):
    ticker, qty = input().split()
    stocks[ticker] = int(qty)

portfolio = Portfolio(cash, stocks)
command_count = int(input())

for _ in range(command_count):
    command = input().split()
    action = command[0]

    if action == "BUY":
        portfolio.buy_stock(command[1], int(command[2]), float(command[3]))
    elif action == "SELL":
        portfolio.sell_stock(command[1], int(command[2]), float(command[3]))
    elif action == "SHOW":
        portfolio.show_portfolio()
