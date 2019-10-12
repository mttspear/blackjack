from googlefinance import getQuotes
import json

stockName = 'LOW'

foo = getQuotes(stockName)
print foo[0]['LastTradePrice']



