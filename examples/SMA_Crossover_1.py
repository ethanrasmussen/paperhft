import paperhft
import time
import math

# NOTE: Remember to have chromedriver.exe within the same directory!

# STRATEGY SUMMARY:
# This strategy uses the simple moving average & is designed to trade quickly.
# Please note that this bot uses 1-min candles for speed. This results in more signals, but not necessarily better signals.
# This bot uses the 10-min and 50-min SMA's.
# When the 10-min SMA > 50-min SMA, the bot will enter into a bullish long stock position.
# When the 10-min SMA < 50-min SMA on an open position, the bot will close the position.
# The bot will determine how much money to spend per trade by taking its cash balance and dividing by the number of stocks on its watchlist.
# It will also adjust its per-trade amount via the variable below (RISK). When RISK = 1, the bot will risk 100% of its account value.
# Additionally, for simplicity and to avoid duplicity, the bot will NOT enter more than 1 position per stock on its watchlist.

# percentage of cash to bot account value to risk (1 = 100%, 0.5 = 50%, 0 = 0%)
RISK = 1

# bot credentials for Investopedia.com
EMAIL_ADDRESS = "example@example.com"
PASSWORD = "password"

# create a bot instance
bot = paperhft.InvestopediaBot(EMAIL_ADDRESS, PASSWORD)

# designate a list of stocks to check for this strategy
watchlist = ["msft", "amzn", "fb", "aapl", "tsla", "goog", "jnj", "wmt", "pg", "v",
             "jpm", "bac", "unh", "intc", "amd", "vz", "hd", "t", "pep", "pfe"]

# starts an infinite while loop
while True:
    # check if market is open
    if (bot.isMarketOpen()):
        # check which stocks the bot currently has open positions in (to avoid duplicate positions)
        currentPositionTickers = []
        for position in bot.stock_positions:
            currentPositionTickers.append(position.ticker)
        # determine what to spend per-trade (accounting for pre-determined risk tolerance variable)
        perTrade = (bot.getCash() / (len(watchlist) - len(bot.stock_positions))) * RISK
        # go through each stock, and check for 10/50 SMA crossover
        for stock in watchlist:
            # ensure that the stock isn't involved in a current/open position
            if stock not in currentPositionTickers:
                # if criteria are met to enter trade, it will enter the trade using the per-trade amount
                if (paperhft.getSimpleMovingAverage(stock, 10, "1-min") > paperhft.getSimpleMovingAverage(stock, 10, "1-min")):
                    # but first, the bot needs to check how many of the stock it can afford using the per-trade amount (rounded down to an integer)
                    maximumStocks = math.floor(perTrade / paperhft.getStockPrice(stock))
                    bot.openStockPosition(stock, maximumStocks)
        # after opening positions, the bot will check all open positions and see which should be closed
        for position in bot.stock_positions:
            if (paperhft.getSimpleMovingAverage(position.ticker, 10, "1-min") < paperhft.getSimpleMovingAverage(position.ticker, 10, "1-min")):
                # if criteria are met, it will close the trade
                bot.closeStockPosition(position)
    # if closed, it will sleep for 2 minutes (this else statement is optional & can be removed)
    else:
        time.sleep(120)
