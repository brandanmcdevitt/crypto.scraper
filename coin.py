class Coin:
    def __init__(self, rank, name, symbol, mcap, price):
        self.__rank = rank
        self.__name = name
        self.__symbol = symbol
        self.__mcap = mcap
        self.__price = price

    def get_price(self):
        return self.__price

    def get_all_data(self):
        return [self.__rank, self.__name, self.__symbol, self.__mcap, self.__price]
        
    def get_all_data_json(self):
        return {
                "rank": self.__rank, 
                "name": self.__name, 
                "symbol": self.__symbol, 
                "market-cap": self.__mcap, 
                "price": self.__price
                }