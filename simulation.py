
class Broker:
    def __init__(self, broker, method, startDebut=None, endDate=None):
        self.name = name

    def buy(self, symbol, quantity):
        print("BUY {} {}".format(quantity, symbol))

    def sell(self, symbol, quantity):
        print("SELL {} {}".format(quantity, symbol))


class Yahoo(Broker):
    def __init__(self, method):
        self.method = method

class Oanda(Broker):
    def __init__(self):
        self.arg = arg

class Algo:
    def __init__(self, algo, symbol, broker, method, stopLoss, stopGain, quantity, startDebut=None, endDate=None):
        self.broker = broker.Broker(broker, method) # yahoo, oanda
        if algo == "SMA" or algo == "SimpleMovingAverage":
            self.algo = SimpleMovingAverage(symbol, quantity)
    def run(self):
        self.algo.run()

class SimpleMovingAverage(Algo):
    def __init__(self, quantity):
        self.quantity = quantity

    def run(arg):
        pass


class Simulation:
    def __init__(self, algo, symbol, broker, method, quantity,
        startDebut=None, endDate=None):
        self.algo = algo.Algo(algo, symbol, self.broker, stopLoss, stopGain, quantity)

    def getStability(accuracy):
        pass

    def getGraphResult(arg):
        pass
        
    def run(self):
        self.algo.run()

    def fname(arg):
        pass
