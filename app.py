import requests
import json
import os
from datetime import date
import datetime
from flask import Flask, request
from twilio.rest import Client
from twilio import twiml


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
ACCOUNT_SID =os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']

client = Client(ACCOUNT_SID,AUTH_TOKEN)

app = Flask(__name__)


def get_status():
    today = date.today().strftime("%d-%B-%y")
    previous_day = (datetime.date.today() -
                    datetime.timedelta(1)).strftime("%d-%B-%y")
    data = requests.get(
        'https://api.covid19india.org/states_daily.json').json()
    data2 = requests.get('https://api.track-covid19.in/reports_v2.json').json()

    if data2['states']['KL']['today']['confirmed'] != 0:
        updated=data2['updatedTime']
        confirmed=data2['states']['KL']['today']['confirmed']
        recovered=data2['states']['KL']['today']['recovered']
        deceased=data2['states']['KL']['today']['dead']
        return('\nCovid Stats-Kerala on {} \n Confirmed: {} \n Recovered: {} \n Deceased: {} \n Last Updated: {} '.format(today, confirmed, recovered, deceased,updated))

    else:
        for _ in data['states_daily'][-3:]:
            if _['date'] == previous_day:
                if _['status'] == "Confirmed":
                    confirmed = _['kl']
                    continue
                if _['status'] == "Recovered":
                    recovered = _['kl']
                    continue                
                if _['status'] == "Deceased":
                    deceased = _['kl']
                return('\nCovid Stats-Kerala on {} \n Confirmed: {} \n Recovered: {} \n Deceased: {} \n Last Updated: {} 23:59:59 '.format(previous_day,confirmed,recovered,deceased,previous_day))

   

@app.route('/update', methods=['GET'])
def inbound_sms():

    message = client.messages \

        .create(
            body=get_status(),
            from_='twilio_no',  # add your twilio no. here
            to='your_no'  # add your verified number here
        )

    print(message.sid)
    return("Your request was send")

