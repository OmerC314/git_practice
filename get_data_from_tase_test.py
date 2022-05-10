from calendar import month
from urllib.parse import urlencode
import requests
import http.client
import datetime
import json

def get_tase_data(index_name):
    conn = http.client.HTTPSConnection("openapigw.tase.co.il")
    body_requests= json.dumps({'grant_type':'client_credentials', 'scope':'tase'})
    tokenreq = conn.request("POST", f"/tase/prod/oauth/oauth2/token", headers={'Authorization':'Basic NjJhMjlkNzNmZjNhY2JiMzJmZDc4ZTdmMjcwODE2MmE6MDVhM2EwZDY5ZGNjZmRkNTQzNWQ3MWNjMTIzM2RmZjA=', 'Content-Type':'application/x-www-form-urlencoded'}, body=body_requests)
    #tokenres = conn.getresponse()
    #token = json.loads(tokenreq.text)['token']
    print("token: " + str(tokenreq))
    year = str(datetime.datetime.today().year)
    month = str(datetime.datetime.today().month)
    day = str(datetime.datetime.today().day)

    headers = {'Authorization': "Bearer REPLACE_BEARER_TOKEN",
    'accept-language': "he-IL",
    'accept': "application/json"
    }

    if index_name == 'tel bond 20':
        conn.request("GET", f"/tase/prod/api/v1/indices-end-of-day-data/index-end-of-day-data/{year}/{month}/{day}?indexId=142", headers=headers)
        res = conn.getresponse()
        data = res.read()
        print(data)

    else:
        return 'Enter Valid Index'

    # gov_bond_index_dict = req.json().get('Items')
    # gov_bond_index_data = pd.DataFrame.from_records(gov_bond_index_dict)

    # gov_bond_index_data = gov_bond_index_data.set_index('TradeDate')
    # gov_bond_index_data.index = pd.to_datetime(gov_bond_index_data.index, format='%d/%m/%Y')
    # gov_bond_index_data = gov_bond_index_data.sort_index()
    # gov_bond_index_data.index = gov_bond_index_data.index.strftime('%d/%m/%Y')
    # return gov_bond_index_data['CloseRate']

get_tase_data('tel bond 20')