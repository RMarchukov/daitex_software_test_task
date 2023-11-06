from binance.client import Client
import datetime
from csv_writer import CSVWriter


class Candles:
    today = datetime.datetime.today()
    all_candles = []
    client = Client()

    def __init__(self):
        self.start_time = self.get_start_time()
        self.end_time = self.get_end_time()

    def get_end_time(self):
        end_time = int(self.today.timestamp()) * 1000
        return end_time

    def get_start_time(self):
        start_time = self.today.replace(self.today.year - 1)
        res = int(start_time.timestamp() * 1000)
        return res

    def get_all_candles(self):
        while self.start_time <= self.end_time:
            result = self.client.get_klines(symbol='USDTUAH',
                                            interval=Client.KLINE_INTERVAL_1MINUTE,
                                            startTime=self.start_time,
                                            limit=1000)
            self.all_candles.append(result)
            self.start_time = result[-1][6]
        return self.all_candles


candles = Candles()
writer = CSVWriter(candles.get_all_candles())
writer.write_to_file()
