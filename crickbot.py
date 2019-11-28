import requests
from datetime import datetime
class Scoreget:
    def __init__(self):
        self.url_get_all_matches = 'https://www.cricapi.com/member-test.aspx'
        self.get_score = "https://cricapi.com/api/cricketScore?apikey"
        self.api_key = "YOUR_CRICAPI_KEY"
        self.unique_id = "" #UNIQUE FOR EVERY MATCH
    def get_unique_id(self):
        uri_params = {"apikey": self.api_key}
        resp = requests.get(self.url_get_all_matches, params=uri_params)
        resp_dict = resp.json
        uid_found=0

        for i in resp_dict['matches']:
            if(i['team-1'] == 'india' or ['team-2']=='india' and i['matchStarted']):
             todays_date = datetime.today().strftime('%y-%m-%d')
             if todays_date == i['date'].split("T")[0]:
                uid_found=1
                self.unique_id=i['unique_id']
                print(self.unique_id)
                break
        if not uid_found:
            self.unique_id=-1
        send_data=self.get_score_current(self.unique_id)
        return send_data
    def get_score_current(self,unique_id):
       data=""
       if unique_id==-1:
           data='no india matches today'
       else:
           uri_params = {'apikey':self.api_key,"unique_id": self.unique_id}
           resp=requests.get(self.get_score,params=uri_params)
           data_json=resp.json()
           try:
               data=" here's the score :  "+" \n"+data_json['stat']+"\n"+data_json['score']

           except KeyError as e:
               print(e)
       return data

if __name__== "__main__":
 match_obj=Scoreget()
 send_message = match_obj.get_unique_id()
 print(send_message)
 from twilio.rest import Client
 account_sid ='YOUR_TWILIO_KEY'
 auth_token="YOUR_AUTH_KEY"
 client = Client(account_sid, auth_token)
 message = client.message.create(body=send_message, from_ ='WHATSAPP:+1205*****', to='WHATSAPP:+9172******')