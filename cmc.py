import coinmarketcap
import json
import pandas as pd
import time

market = coinmarketcap.Market()
coin = market.ticker('ethereum')
print (json.dumps(coin))

