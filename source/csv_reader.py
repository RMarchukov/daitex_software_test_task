class CSVReader:

    def read_file(self):
        with open('candles.csv', 'r') as file:
            data = file.readlines()
            print(data)
            return data


reader = CSVReader()
d = reader.read_file()
for i in d:
    print(i)
