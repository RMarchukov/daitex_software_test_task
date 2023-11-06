class CSVWriter:
    def __init__(self, data):
        self.data = data

    def write_to_file(self):
        with open('candles.csv', 'w') as file:
            for candles in self.data:
                file.write("".join(str(candles)))
