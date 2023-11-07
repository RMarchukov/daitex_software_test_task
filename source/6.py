from binance.client import Client

# api_key = 'your_api_key'
# api_secret = 'your_api_secret'

client = Client()


def open_long_position(symbol, quantity, entry_price, TP, SP):
    order = client.create_oco_order(
        symbol=symbol,
        # side=Client.SIDE_BUY,
        quantity=quantity,
        price=entry_price,
        stopPrice=entry_price,
        stopLimitPrice=entry_price,
        stopLimitTimeInForce=Client.TIME_IN_FORCE_GTC,
        stopLimitResponseTime=Client.TIME_IN_FORCE_GTC,
        takeProfitPrice=TP,
        stopLossPrice=SP,
    )


def open_short_position(symbol, quantity, entry_price, TP, SP):
    order = client.create_oco_order(
        symbol=symbol,
        # side=Client.SIDE_SELL,
        quantity=quantity,
        price=entry_price,
        stopPrice=entry_price,
        stopLimitPrice=entry_price,
        stopLimitTimeInForce=Client.TIME_IN_FORCE_GTC,
        stopLimitResponseTime=Client.TIME_IN_FORCE_GTC,
        takeProfitPrice=TP,
        stopLossPrice=SP,
    )


symbol = 'USDTUAH'
quantity = 0.05
entry_price = 100
TP = 125
SP = 75

open_short_position(symbol, quantity, entry_price, TP, SP)
open_long_position(symbol, quantity, entry_price, TP, SP)
