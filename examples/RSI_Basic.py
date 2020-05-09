import paperhft
import time
import math

# NOTE: Remember to have chromedriver.exe within the same directory!

# STRATEGY SUMMARY:
# This strategy enters a stock position when RSI falls below a certain value (indicating it is oversold).
# It then closes the position when RSI rises above a certain value (indicating it is overbought).
# This version of the RSI example is considered to be "basic", as it will not set stop losses, or account for previous RSI activity.
# By default, the bot will buy when RSI <= 30, and sell when RSI >= 70. These values can be modified below.

# RSI Indicator of Long or Short Position
RSI_LONG_INDICATOR = 30
RSI_SHORT_INDICATOR = 70

# candle length (shorter length generally = more signals)
CANDLE_LENGTH = "15-min"

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
        # go through each stock, and check for RSI trade signal
        for stock in watchlist:
            # ensure that the stock isn't involved in a current/open position
            if stock not in currentPositionTickers:
                # if criteria are met to enter trade, it will enter the trade using the per-trade amount
                if (paperhft.getRSI(stock, CANDLE_LENGTH) <= RSI_LONG_INDICATOR):
                    # but first, the bot needs to check how many of the stock it can afford using the per-trade amount (rounded down to an integer)
                    maximumStocks = math.floor(perTrade / paperhft.getStockPrice(stock))
                    bot.openStockPosition(stock, maximumStocks)
        # after opening positions, the bot will check all open positions and see which should be closed
        for position in bot.stock_positions:
            if (paperhft.getRSI(position.ticker, CANDLE_LENGTH) >= RSI_SHORT_INDICATOR):
                # if criteria are met, it will close the trade
                bot.closeStockPosition(position)
    # if closed, it will sleep for 2 minutes (this else statement is optional & can be removed)
    else:
        time.sleep(120)
