import base64
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime

business_short_code = "174379"#paybill number
phone_number = "254740364413"
lipa_na_mpesa_passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
consumer_secret = "GUleOW9tNaFZ3R7A" #consumer secret
consumer_key = "JJDgTelBboJwGbnxnAekn7ajiDlEBlZm"

api_Url = ("https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials")
r = requests.get(api_Url, auth=HTTPBasicAuth(consumer_key, consumer_secret))

formated_time = datetime.now().strftime("%Y%m%d%H%M%S")
encoded = base64.b64encode((business_short_code + lipa_na_mpesa_passkey + formated_time).encode()).decode("utf-8")

def lipa_na_mpesa():
    
    access_token = r.json()['access_token']
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" %access_token}
    request = {    
    "BusinessShortCode": business_short_code,    
    "Password": encoded,
    "Timestamp":formated_time,    
    "TransactionType": "CustomerPayBillOnline",    
    "Amount": "1",    
    "PartyA":phone_number,    
    "PartyB":business_short_code,    
    "PhoneNumber":phone_number,    
    "CallBackURL": "http://ccmrs.ac.ke/pages/courses",    
    "AccountReference":"12345678",    
    "TransactionDesc":"Test",
    }
    
    response = requests.post(api_url, json =request, headers = headers)
    print(response.text)
    
lipa_na_mpesa()