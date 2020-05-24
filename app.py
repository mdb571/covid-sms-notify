import requests,json,os
from datetime import date
import datetime
from flask import Flask,request
from twilio.rest import Client
from twilio import twiml


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
ACCOUNT_SID =os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
client = Client(ACCOUNT_SID, AUTH_TOKEN)


app=Flask(__name__)
       
def get_status():
    today=date.today().strftime("%d/%m/%Y") 
    
    data = requests.get('https://api.covid19india.org/states_daily.json').json()

    for _ in reversed(data['states_daily']):
        if _['date']=="23-May-20":
            if _['status']=="Confirmed":
                confirmed=_['kl']
            if _['status']=="Recovered":
                recovered=_['kl']
            if _['status']=="Deceased":
                deceased=_['kl']

    # if str(data['updatedTime'][:10])==today:
    #     confirmed=data['states']['KL']['today']['confirmed']
    #     recovered=data['states']['KL']['today']['recovered']
    #     deceased=data['states']['KL']['today']['dead']

    return('\nCovid Stats-Kerala on {} \n Confirmed: {} \n Recovered: {} \n Deceased: {}'.format(today,confirmed,recovered,deceased))


@app.route('/update',methods=['GET'])
def inbound_sms():

    message = client.messages \
                .create(
                     body=get_status(),
                     from_='+1 870 686 4040',
                     to='+919995153948'
                 )
    print(message.sid)
    return("Your request was send")


