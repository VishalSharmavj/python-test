from nsepy import get_history as gh
from datetime import date
import pandas as pd

# Importing Nifty IT Data
nifty = gh(symbol="NIFTY IT", 
                    start=date(2015,1,1), 
                    end=date(2016,1,1),
					index=True)

# Adjusting date time to fill in holidays as Weekly Data is required
idx = pd.date_range('01-01-2015', '01-01-2016')
nifty.index = pd.DatetimeIndex(nifty.index)
nifty = nifty.reindex(idx, fill_value=0)


# Finding Moving Average
nifty["4weekMA"]=nifty["Close"].rolling(28).mean()
nifty["16weekMA"] = nifty["Close"].rolling(112).mean()
nifty["28weekMA"] = nifty["Close"].rolling(196).mean()
nifty["40weekMA"] = nifty["Close"].rolling(280).mean()
nifty["52weekMA"] = nifty["Close"].rolling(364).mean()
nifty[nifty.Open != 0]

""" Note : 
1> This code do not give correct result as I was unable to find a logic with which I can account for holidays as well as complete week
2> A week can have 5 data point in general but if there is a national holiday, there will be less than 5 data points in that week.
3> Because of this I chose to fullfil the week requirement even though it is giving wrong moving average as it counts values that have 0 closing value."""