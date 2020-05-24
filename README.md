# Twilio-Covid SMS Notifier

This project is based on an api that serves data regarding the covid-19 cases of Kerala(which can be changed according to requirement) and sends it to your mobile via SMS everyday at 20:30 (The time can be changed using crontab)

# Current-Covid World Stats

![Covid-19 Cases](https://covid19-badges.herokuapp.com/confirmed/latest)  ![Covid-19 Deaths](https://covid19-badges.herokuapp.com/deaths/latest)

## Installation
Installation of the required libraries
```bash
pip install -r requirements.txt
```
## Setting up your Twilio Account
* [SignUp your first twilio account](https://www.twilio.com/try-twilio)   

* You will be provided with a dashboard.

* Go to Settings and you will see your 'ACCOUNT SID' and 'AUTH TOKEN' under 'LIVE CREDENTIALS'.

![Verified Number](/img/img2.png)

* Go to 'Products and Services' on the left dashboard.

* Then go to 'Phone numbers' under Super Network in order to get the numbers verified that you need to send the SMS update.<br />
* You need to manually verify the numbers you need by clicking the '+'.<br />

![Verified Number](/img/img1.png)

* Then go your active numbers and in the messaging section setup your webhook by entering your domain in the 'A Message comes in" section.

![Webhook](/img/img3.png)

## Setting up the Program

Add your Account SID and Auth Token
```python
ACCOUNT_SID = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
AUTH_TOKEN= 'your_auth_token' 
```
Then add the trial number created for your Account and your verified number
```python
from_='+15017122661' #YOUR TRIAL PHONE NUMBER
to=' ' #THE VERIFIED NUMBER THAT YOU NEED TO SEND THE SMS
```
This is only a trial account so you can send SMS to only a single number at a time.

## Covid India API

I have used [covidindia](https://github.com/covid19india/api) API for getting the covid stats for my state.You can modify the JSON query to fetch your states data.See their [documentation](https://github.com/covid19india/api/blob/master/README.md) for more details

## Usage
Run the development server using 
```python
flask run
```
## Send GET request
You can manually send a request to recieve an SMS by running

```python
python schedule.py
```

![SMS](/img/sms.jpeg)




## Scheduling SMS
If you feel like you need to change the time for recieving updates. 
 
```bash
crontab -e
```
Then append the following line and save
```bash
* * * * *  /usr/bin/python /path/to/schedule.py
```
where the parameters are as 

![param](/img/param.png)

Give a ⭐ if you like my project


Feel free to comment your feedback❤️


 
