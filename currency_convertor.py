import requests
url="https://api.exchangerate-api.com/v4/latest/USD"
response=requests.get(url)
data=response.json()
From_currency=input("Enter the from_currency:")
to_currency=input("Enter the to_currency:")
Amount=float(input("How Much:"))
#print(data['rates'])
rate=data['rates']
converted_currency=(rate[to_currency]*Amount)/rate[From_currency]
print("The amount in ",to_currency,"is",converted_currency)

