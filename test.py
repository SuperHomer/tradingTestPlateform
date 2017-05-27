import simulation
import ystockquote
from datetime import datetime
from yahoo_finance import Share

item = {
    "algo": "SMA",
    "broker": "YAHOO",
    "method": "HISTORICAL",
    "quantity": 10,
    "displayGraph": True,
    "stopLoss": None,
    "stopGain": None,
    "testStability": True
}

#sim = simulation.Simulation(item)
#print sim.item
quantity = 50
symbol = "AAPL"
print("BUY {} {}".format(quantity, symbol))

print(ystockquote.get_price('GOOGL'))

#print ystockquote.get_historical_prices('GOOGL', '2013-01-03', '2013-01-08')
yahoo = Share('GOOGL')
print yahoo.get_historical('2014-04-25', '2014-04-29')
