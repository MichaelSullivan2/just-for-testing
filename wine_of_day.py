
import csv
import random
import tweepy
import datetime
import requests
import os
from PIL import Image

import schedule
import time
ACCESS_TOKEN = "955952796154687488-GToKSC3V29kRdaGjTNpn8UirBYjaLg7"
ACCESS_TOKEN_SECRET = "2CrblwUHnJi0IMp7IfXSCR4CamJ8jU8VOTUGrvRmEJZDx"
CONSUMER_KEY = "1TFKQvWQ4XajgmdaJTgZijsUc"
CONSUMER_SECRET = "7GAryxmYY3imtaXr1XBURzc8yoFFG6astmpYlE7Ipx3L9bZ0A3"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAP31KwEAAAAAtrPTi1N3akbyUvf2W0%2Bn27m5S0E%3DuQEqIgDWgqr8X6mJnheYcn4ho3HDiH1WmsssdtHwlzncrcmnZj"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

path = "m1.PNG"
path2 = "m2.PNG"
path3 = "m3.PNG"
path4 = "m4.PNG"

fpath = "f1.PNG"
fpath2 = "f2.PNG"
fpath3 = "f3.PNG"
fpath4 = "f4.PNG"
fpath5 = "f5.PNG"



random_list = list()
random_list2 = list()

random_list.append(path)
random_list.append(path2)
random_list.append(path3)
random_list.append(path4)

random_list2.append(fpath)
random_list2.append(fpath2)
random_list2.append(fpath3)
random_list2.append(fpath4)
random_list2.append(fpath5)




media_list = list()
media_list2 = list()




#api.update_status(data)

def my_job():
    with open('SQL_Query.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0

        if line_count == 0:
            chosen_row=random.choice(list(csv_reader))

        chem = (f'Congratulations to {chosen_row["first_name"]} {chosen_row["last_name"]}, who works in {chosen_row["dept_name"]} as a(n) {chosen_row["title"]} and joined us on {chosen_row["hire_date"]}.')
        line_count += 1
        if chosen_row["gender"] == 'M':
            print("WOW")
            newRand = random.choice(random_list) # 1 image

            response = api.media_upload(newRand) # 1 image

            media_list.append(response.media_id_string)
            api.update_status(status=chem, media_ids=media_list)
            media_list.pop()
        else:
            print("oh")
            newRand2 = random.choice(random_list2)

            response2 = api.media_upload(newRand2)

            media_list2.append(response2.media_id_string)
            api.update_status(status=chem, media_ids=media_list2)
            media_list2.pop()
        print(chem)

schedule.every().day.at("10:30").do(my_job)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute