# IMPORTS

# Datetime:
from datetime import datetime
# Selenium:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


# initializes webdriver
chrome_options = Options()
#chrome_options.add_argument("--headless")
browser = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)




# The following lines (24-278) are for collecting stock data/indicators from TradingView

def getTechnicals(ticker):
    browser.get("https://www.tradingview.com/symbols/"+str(ticker)+"/")
    browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/header/div/div[5]/div/div[1]/div/a[3]").click()

def getStockPrice(ticker):
    browser.get("https://www.tradingview.com/symbols/"+str(ticker)+"/")
    return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]/span").text)

def getPriceToEarnings(ticker):
    browser.get("https://www.tradingview.com/symbols/"+str(ticker)+"/")
    return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/header/div/div[3]/div[3]/div[5]/div[1]").text)

def getEarningsPerShare(ticker):
    browser.get("https://www.tradingview.com/symbols/" + str(ticker) + "/")
    return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/header/div/div[3]/div[3]/div[2]/div[1]").text)

# note for moving averages:
# length = time/bar on chart (ex. 1-min candles) (default: 1-day)
# period = # of bars (ex. 1-day EMA w/ period of 5 = the 5-day EMA) (NOTE: MUST BE SPECIFIED)

def getExponentialMovingAvg(ticker, period, length="1-day"):
    # fetch technicals
    getTechnicals(ticker)
    # adjust length if needed
    if (length == "1-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]").click()
    elif (length == "5-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]").click()
    elif (length == "15-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[3]").click()
    elif (length == "1-hr"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[4]").click()
    elif (length == "4-hr"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[5]").click()
    elif (length == "1-week"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[7]").click()
    elif (length == "1-month"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[8]").click()
    # get the proper EMA based off period
    if (period == 5):
        return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[2]/td[2]").text)
    elif (period == 10):
        return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[4]/td[2]").text)
    elif (period == 20):
        return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[6]/td[2]").text)
    elif (period == 30):
        return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[8]/td[2]").text)
    elif (period == 50):
        return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[10]/td[2]").text)
    elif (period == 100):
        return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[12]/td[2]").text)
    elif (period == 200):
        return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[14]/td[2]").text)


def getSimpleMovingAverage(ticker, period, length="1-day"):
    # fetch technicals
    getTechnicals(ticker)
    # adjust length if needed
    if (length == "1-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]").click()
    elif (length == "5-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]").click()
    elif (length == "15-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[3]").click()
    elif (length == "1-hr"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[4]").click()
    elif (length == "4-hr"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[5]").click()
    elif (length == "1-week"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[7]").click()
    elif (length == "1-month"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[8]").click()
    # get the proper SMA based off period
    if (period == 5):
        return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[3]/td[2]").text)
    elif (period == 10):
        return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[5]/td[2]").text)
    elif (period == 20):
        return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]").text)
    elif (period == 30):
        return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[9]/td[2]").text)
    elif (period == 50):
        return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[11]/td[2]").text)
    elif (period == 100):
        return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[13]/td[2]").text)
    elif (period == 200):
        return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[15]/td[2]").text)

# get Price:Rev. ratio
def getPriceToRevenue(ticker):
    browser.get("https://www.tradingview.com/symbols/" + str(ticker) + "/")
    return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[9]/span[2]").text)

# get Price:Book ratio
def getPriceToBook(ticker):
    browser.get("https://www.tradingview.com/symbols/" + str(ticker) + "/")
    return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[10]/span[2]").text)

# get Price:Sales ratio
def getPriceToSales(ticker):
    browser.get("https://www.tradingview.com/symbols/" + str(ticker) + "/")
    return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[11]/span[2]").text)

# get 1-year beta
def getBeta1yr(ticker):
    browser.get("https://www.tradingview.com/symbols/" + str(ticker) + "/")
    return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[3]/span[2]").text)

# get 52 week high
def getHigh52w(ticker):
    browser.get("https://www.tradingview.com/symbols/" + str(ticker) + "/")
    return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[4]/span[2]").text)

# get 52 week low
def getLow52w(ticker):
    browser.get("https://www.tradingview.com/symbols/" + str(ticker) + "/")
    return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[5]/span[2]").text)




# note for technicals:
# length = time/bar on chart (ex. 1-min candles) (default: 1-day)

# get volume weighted moving average (20)
def getVWMA(ticker, length):
    # fetch technicals
    getTechnicals(ticker)
    # adjust length if needed
    if (length == "1-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]").click()
    elif (length == "5-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]").click()
    elif (length == "15-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[3]").click()
    elif (length == "1-hr"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[4]").click()
    elif (length == "4-hr"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[5]").click()
    elif (length == "1-week"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[7]").click()
    elif (length == "1-month"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[8]").click()
    return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[17]/td[2]").text)


# get hull moving average (9)
def getHMA(ticker, length):
    # fetch technicals
    getTechnicals(ticker)
    # adjust length if needed
    if (length == "1-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]").click()
    elif (length == "5-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]").click()
    elif (length == "15-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[3]").click()
    elif (length == "1-hr"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[4]").click()
    elif (length == "4-hr"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[5]").click()
    elif (length == "1-week"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[7]").click()
    elif (length == "1-month"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[8]").click()
    return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[18]/td[2]").text)


# get relative strength index (14)
def getRSI(ticker, length):
    # fetch technicals
    getTechnicals(ticker)
    # adjust length if needed
    if (length == "1-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]").click()
    elif (length == "5-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]").click()
    elif (length == "15-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[3]").click()
    elif (length == "1-hr"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[4]").click()
    elif (length == "4-hr"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[5]").click()
    elif (length == "1-week"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[7]").click()
    elif (length == "1-month"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[8]").click()
    return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]").text)


# get ichimoku cloud base line (9, 26, 52, 26)
def getIchimoku(ticker, length):
    # fetch technicals
    getTechnicals(ticker)
    # adjust length if needed
    if (length == "1-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]").click()
    elif (length == "5-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]").click()
    elif (length == "15-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[3]").click()
    elif (length == "1-hr"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[4]").click()
    elif (length == "4-hr"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[5]").click()
    elif (length == "1-week"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[7]").click()
    elif (length == "1-month"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[8]").click()
    return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[16]/td[2]").text)


# get stochastic RSI fast (3,3,14,14)
def getStochRSI(ticker, length):
    # fetch technicals
    getTechnicals(ticker)
    # adjust length if needed
    if (length == "1-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]").click()
    elif (length == "5-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]").click()
    elif (length == "15-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[3]").click()
    elif (length == "1-hr"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[4]").click()
    elif (length == "4-hr"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[5]").click()
    elif (length == "1-week"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[7]").click()
    elif (length == "1-month"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[8]").click()
    return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[9]/td[2]").text)


# get MACD level (12,26)
def getMACD(ticker, length):
    # fetch technicals
    getTechnicals(ticker)
    # adjust length if needed
    if (length == "1-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]").click()
    elif (length == "5-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]").click()
    elif (length == "15-min"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[3]").click()
    elif (length == "1-hr"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[4]").click()
    elif (length == "4-hr"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[5]").click()
    elif (length == "1-week"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[7]").click()
    elif (length == "1-month"):
        browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[8]").click()
    return float(browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[2]").text)




# class defining a long stock position
class LongStockPosition:

    def __init__(self, ticker, qty):
        self.ticker = ticker
        self.qty = qty
        self.openStockPrice = getStockPrice(ticker)
        self.openValue = float(self.openStockPrice * self.qty)
        self.openDateTime = datetime.now()
        self.isOpenPosition = True
        self.closeDateTime = datetime.now()
        self.closeStockPrice = 0
        self.closeValue = 0

    def getCurrentValue(self):
        if (self.isOpenPosition):
            return float(self.qty * getStockPrice(self.ticker))
        else:
            return self.closeValue

    def closePosition(self):
        self.isOpenPosition = False
        self.closeDateTime = datetime.now()
        self.closeStockPrice = getStockPrice(self.ticker)
        self.closeValue = float(self.qty * self.closeStockPrice)




# class defining a stock-trading bot that utilizes the Investopedia trading simulator
class InvestopediaBot:

    #NOTE: ensure that the bot isn't logged into multiple games!

    def __init__(self, username, password):
        #initialize variables
        self.username = username
        self.password = password
        self.stock_positions = []

        #login the bot
        browser.get("https://www.investopedia.com/auth/realms/investopedia/protocol/openid-connect/auth?state=bdb56e685a7fae8f076d1b090cbba791&scope=name%2Cemail&response_type=code&approval_prompt=auto&redirect_uri=https%3A%2F%2Fwww.investopedia.com%2Fsimulator%2Fhome.aspx&client_id=inv-simulator-conf")
        browser.find_element_by_xpath("/html/body/div[1]/div/form/div[1]/input").send_keys(username)
        browser.find_element_by_xpath("/html/body/div[1]/div/form/div[2]/input").send_keys(password)
        browser.find_element_by_xpath("/html/body/div[1]/div/form/div[3]/input").click()

        #go to the portfolio page
        browser.get("https://www.investopedia.com/simulator/portfolio/")



    def isMarketOpen(self):
        #check if bot is on portfolio page
        if (browser.current_url == "https://www.investopedia.com/simulator/portfolio/"):
            #Click refresh
            browser.find_element_by_xpath("/html/body/div[3]/form/div/div[1]/div[1]/div[1]/span[2]/a[1]").click()
            #check if the market is open or closed
            if (browser.find_element_by_xpath("/html/body/div[3]/form/div/div[1]/div[1]/div[1]/span[1]/span[1]").text == "Market is Currently Closed"):
                return False
            else:
                return True
        else:
            #if not on portfolio, go to portfolio
            browser.get("https://www.investopedia.com/simulator/portfolio/")
            if (browser.find_element_by_xpath("/html/body/div[3]/form/div/div[1]/div[1]/div[1]/span[1]/span[1]").text == "Market is Currently Closed"):
                return False
            else:
                return True



    def getAccountBalance(self):
        #check if on portfolio page
        if (browser.current_url == "https://www.investopedia.com/simulator/portfolio/"):
            #refresh page
            browser.find_element_by_xpath("/html/body/div[3]/form/div/div[1]/div[1]/div[1]/span[2]/a[1]").click()
            # wait until xpath exists
            try:
                element_present = EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[3]/form/div/div[2]/div[1]/p/span"))
                WebDriverWait(browser, 5).until(element_present)
            except TimeoutError:
                print("Timed out.")
            #return account balance
            return float(browser.find_element_by_xpath("/html/body/div[3]/form/div/div[2]/div[1]/p/span").text[1:].replace(',',''))
        else:
            #if not on portfolio, go there
            browser.get("https://www.investopedia.com/simulator/portfolio/")
            # return account balance
            return float(browser.find_element_by_xpath("/html/body/div[3]/form/div/div[2]/div[1]/p/span").text[1:].replace(',',''))



    def getBuyingPower(self):
        # check if on portfolio page
        if (browser.current_url == "https://www.investopedia.com/simulator/portfolio/"):
            # refresh page
            browser.find_element_by_xpath("/html/body/div[3]/form/div/div[1]/div[1]/div[1]/span[2]/a[1]").click()
            # wait until xpath exists
            try:
                element_present = EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/form/div/div[2]/div[1]/p/span"))
                WebDriverWait(browser, 5).until(element_present)
            except TimeoutError:
                print("Timed out.")
            # return account balance
            return float(browser.find_element_by_xpath("/html/body/div[3]/form/div/div[2]/div[2]/p/span").text[1:].replace(',',''))
        else:
            # if not on portfolio, go there
            browser.get("https://www.investopedia.com/simulator/portfolio/")
            # return account balance
            return float(browser.find_element_by_xpath("/html/body/div[3]/form/div/div[2]/div[2]/p/span").text[1:].replace(',',''))



    def getCash(self):
        # check if on portfolio page
        if (browser.current_url == "https://www.investopedia.com/simulator/portfolio/"):
            # refresh page
            browser.find_element_by_xpath("/html/body/div[3]/form/div/div[1]/div[1]/div[1]/span[2]/a[1]").click()
            # wait until xpath exists
            try:
                element_present = EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/form/div/div[2]/div[1]/p/span"))
                WebDriverWait(browser, 5).until(element_present)
            except TimeoutError:
                print("Timed out.")
            # return account balance
            return float(browser.find_element_by_xpath("/html/body/div[3]/form/div/div[2]/div[3]/p/span").text[1:].replace(',',''))
        else:
            # if not on portfolio, go there
            browser.get("https://www.investopedia.com/simulator/portfolio/")
            # return account balance
            return float(browser.find_element_by_xpath("/html/body/div[3]/form/div/div[2]/div[3]/p/span").text[1:].replace(',',''))



    def getAnnualReturn(self):
        # check if on portfolio page
        if (browser.current_url == "https://www.investopedia.com/simulator/portfolio/"):
            # refresh page
            browser.find_element_by_xpath("/html/body/div[3]/form/div/div[1]/div[1]/div[1]/span[2]/a[1]").click()
            # wait until xpath exists
            try:
                element_present = EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/form/div/div[2]/div[1]/p/span"))
                WebDriverWait(browser, 5).until(element_present)
            except TimeoutError:
                print("Timed out.")
            # return account balance
            return float(browser.find_element_by_xpath("/html/body/div[3]/form/div/div[2]/div[4]/p/span").text[:4])
        else:
            # if not on portfolio, go there
            browser.get("https://www.investopedia.com/simulator/portfolio/")
            # return account balance
            return float(browser.find_element_by_xpath("/html/body/div[3]/form/div/div[2]/div[4]/p/span").text[:4])



    def openStockPosition(self, ticker, qty, dayOrder=False, limitPrice=0, stopPrice=0):

        # check if on portfolio page
        if (browser.current_url == "https://www.investopedia.com/simulator/portfolio/"):
            # refresh page
            browser.find_element_by_xpath("/html/body/div[3]/form/div/div[1]/div[1]/div[1]/span[2]/a[1]").click()
            # wait until purchase button exists
            try:
                element_present = EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/form/div/div[4]/div[1]/ul/li[1]/a/span"))
                WebDriverWait(browser, 5).until(element_present)
            except TimeoutError:
                print("Timed out.")
            # make purchase
            browser.find_element_by_xpath("/html/body/div[3]/form/div/div[4]/div[1]/ul/li[1]/a/span").click()

            # wait until ticker symbol entry box exists
            try:
                element_present = EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[1]/td/input[1]"))
                WebDriverWait(browser, 5).until(element_present)
            except TimeoutError:
                print("Timed out.")

            # enter ticker symbol
            browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[1]/td/input[1]").send_keys(ticker)
            # enter QTY
            browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[3]/td/input[1]").send_keys(qty)
            # if limit is set, choose limit & enter price
            if (limitPrice > 0):
                browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[5]/td/label/input").click()
                browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[5]/td/input").send_keys(limitPrice)
            # if stop is set, choose stop & enter price
            if (stopPrice > 0):
                browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[6]/td/label/input").click()
                browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[6]/td/input").send_keys(stopPrice)
            # if day order, change duration
            if (dayOrder):
                select = Select(browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[8]/td/select"))
                select.select_by_visible_text("Day Order")
            # click preview order
            # browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/input").click()
            previewButton = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/input")
            browser.execute_script("arguments[0].click();", previewButton)
            # click submit order (executes via JSExecutor)
            submitButton = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[1]/div[3]/form/input[2]")
            browser.execute_script("arguments[0].click();", submitButton)
        else:
            # if not on portfolio, go there
            browser.get("https://www.investopedia.com/simulator/portfolio/")
            # make purchase
            browser.find_element_by_xpath("/html/body/div[3]/form/div/div[4]/div[1]/ul/li[1]/a/span").click()

            # wait until ticker symbol entry box exists
            try:
                element_present = EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[1]/td/input[1]"))
                WebDriverWait(browser, 5).until(element_present)
            except TimeoutError:
                print("Timed out.")

            # enter ticker symbol
            browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[1]/td/input[1]").send_keys(ticker)
            # enter QTY
            browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[3]/td/input[1]").send_keys(qty)
            # if limit is set, choose limit & enter price
            if (limitPrice > 0):
                browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[5]/td/label/input").click()
                browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[5]/td/input").send_keys(limitPrice)
            # if stop is set, choose stop & enter price
            if (stopPrice > 0):
                browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[6]/td/label/input").click()
                browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[6]/td/input").send_keys(stopPrice)
            # if day order, change duration
            if (dayOrder):
                select = Select(browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[8]/td/select"))
                select.select_by_visible_text("Day Order")
            # click preview order
            # browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/input").click()
            previewButton = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/input")
            browser.execute_script("arguments[0].click();", previewButton)
            # click submit order (executes via JSExecutor)
            submitButton = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[1]/div[3]/form/input[2]")
            browser.execute_script("arguments[0].click();", submitButton)


        # adds a LongStockPosition object to the list of stock positions
        newStockPosition = LongStockPosition(ticker, qty)
        self.stock_positions.append(newStockPosition)



    def closeStockPosition(self, position, dayOrder=False, limitPrice=0, stopPrice=0, trailingStopType="none", trailingStop=0):

        # check if on portfolio page
        if (browser.current_url == "https://www.investopedia.com/simulator/portfolio/"):

            # refresh page
            browser.find_element_by_xpath("/html/body/div[3]/form/div/div[1]/div[1]/div[1]/span[2]/a[1]").click()
            # wait until trade-stock button exists
            try:
                element_present = EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[3]/form/div/div[4]/div[1]/ul/li[1]/a/span"))
                WebDriverWait(browser, 5).until(element_present)
            except TimeoutError:
                print("Timed out.")

        else: # if not on portfolio, open it
            browser.get("https://www.investopedia.com/simulator/portfolio/")

        # click button to place order
        browser.find_element_by_xpath("/html/body/div[3]/form/div/div[4]/div[1]/ul/li[1]/a/span").click()

        # wait until ticker symbol entry box exists
        try:
            element_present = EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[1]/td/input[1]"))
            WebDriverWait(browser, 5).until(element_present)
        except TimeoutError:
            print("Timed out.")

        # change transaction type to "sell"
        select = Select(browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[2]/td/select"))
        select.select_by_visible_text("Sell")

        # enter ticker
        browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[1]/td/input[1]").send_keys(position.ticker)
        # enter QTY
        browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[3]/td/input[1]").send_keys(position.qty)
        # if day order, set as such
        if (dayOrder):
            select = Select(browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[8]/td/select"))
            select.select_by_visible_text("Day Order")
        # if applicable, set limit
        if (limitPrice > 0):
            browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[5]/td/label/input").click()
            browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[5]/td/input").send_keys(limitPrice)
        # if applicable, set stop
        if (stopPrice > 0):
            browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[6]/td/label/input").click()
            browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[6]/td/input").send_keys(stopPrice)
        # if trailing stop, set it up
        if (trailingStopType == "%"):
            browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[7]/td/div[1]/div[1]/input").click()
            browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[7]/td/div[1]/div[2]/div[1]/input").click()
            browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[7]/td/div[1]/div[2]/div[2]/input").send_keys(trailingStop)
        elif (trailingStopType == "$"):
            browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[7]/td/div[1]/div[1]/input").click()
            browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[7]/td/div[1]/div[2]/div[3]/input").click()
            browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/table/tbody/tr[7]/td/div[1]/div[2]/div[4]/input").send_keys(trailingStop)

        # click preview order
        previewButton = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/input")
        browser.execute_script("arguments[0].click();", previewButton)
        # click submit order (executes via JSExecutor)
        submitButton = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[1]/div[3]/form/input[2]")
        browser.execute_script("arguments[0].click();", submitButton)

        # closes longStockPosition obj. & removes from list of bot's positions
        position.closePosition()
        self.stock_positions.remove(position)

    # TODO: implement verifyPositions()
    # this method would return all current stock positions by checking the Investopedia website
    # use cases: if a bot were to be shut off, this could allow it to restart w/o saving a separate txt file of positions
    def verifyPositions(self):
        pass