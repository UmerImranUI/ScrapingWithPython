import requests
import json

res=requests.get('https://www.brewersassociation.org/wp-content/themes/ba2019/json-store/breweries/breweries.json?nocache=1656785349608')

res.status_code

len(res.text)

res.text[:100]

res.json()[:100]

type(json.loads(res.json()))

data=json.loads(res.join())

data['ResultMessage']

type(data['ResultData'][0])

data['ResultDara'][0].keys()

data['ResultDara'][0]

import pandas as pd
df=pd.DataFrame(data)

df.head()
df= pd.DataFrame(data['ResultData'])

df.head()

df.shape

df.to_csv('beer.csv', index=False)
