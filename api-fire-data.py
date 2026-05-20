# Let's set your map key that was emailed to you. It should look something like 'abcdef1234567890abcdef1234567890'MAP_KEY = '01b9b20f1c9e80d44560acd21f5a79a7'
MAP_KEY = "01b9b20f1c9e80d44560acd21f5a79a7"

# now let's check how many transactions we have
import pandas as pd
import requests
url = 'https://firms.modaps.eosdis.nasa.gov/mapserver/mapkey_status/?MAP_KEY=' + MAP_KEY
try:
  response = requests.get(url)
  data = response.json()
  df = pd.Series(data)
  display(df)
except:
  # possible error, wrong MAP_KEY value, check for extra quotes, missing letters
  print ("There is an issue with the query. \nTry in your browser: %s" % url)