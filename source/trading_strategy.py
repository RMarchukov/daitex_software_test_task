import time


price = 100
commission = 0.05

if RSIBANDS_LB > 30:
    time.sleep(60)
    if RSIBANDS_LB < 30 and CCI < -100:
        print("відкрити LONG з TP 1% та SL 0.4%")
elif RSIBANDS_LB < 70:
    time.sleep(60)
    if RSIBANDS_LB > 70 and CCI > 120:
        print("відкрити SHORT з TP 1.1% та SL 0.5%")

