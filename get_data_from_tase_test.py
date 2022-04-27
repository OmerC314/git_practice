from calendar import month
from urllib.parse import urlencode
import requests
import http.client
import pandas as pd
import datetime


def get_tase_data(index_name):
    conn = http.client.HTTPSConnection("openapigw.tase.co.il")
    token = conn.request('POST', "/tase/prod/oauth/oauth2/token", headers={'Authorization': 'Basic NjJhMjlkNzNmZjNhY2JiMzJmZDc4ZTdmMjcwODE2MmE6MDVhM2EwZDY5ZGNjZmRkNTQzNWQ3MWNjMTIzM2RmZjA=', 'Content-Type':'application/x-www-form-urlencoded'}, body={'mode' : 'urlencoded', 'grant_type': 'client_credentials', 'scope': 'tase'})
    year = datetime.datetime.today().year
    month = datetime.datetime.today().month
    day = datetime.datetime.today().day

    headers = {'Authorization': "Bearer REPLACE_BEARER_TOKEN",
    'accept-language': "he-IL",
    'accept': "application/json"
    }

    if index_name == 'gov bond':
        req = requests.post(url, headers=headers, data={'pType': "1", 'TotalRec': 1, 'pageNum': 1, 'oId': "602", 'lang': "0"})

    elif index_name == 'tel aviv banks':
        req = requests.post(url, headers=headers, data={'pType': "1", 'TotalRec': 1, 'pageNum': 1, 'oId': "164", 'lang': "0"})

    elif index_name == 'tel bond 20':
        conn.request("GET", f"/tase/prod/api/v1/indices-end-of-day-data/index-end-of-day-data/{year}/{month}}/{day}?indexId=142", headers=headers)
        res = conn.getresponse()
        data = res.read()

    elif index_name == 'tel bond 40':
        req = requests.post(url, headers=headers, verify=False, data={'pType': "1", 'TotalRec': 1, 'pageNum': 1, 'oId': "708", 'lang': "0"})

    elif index_name == 'tel bond 60':
        req = requests.post(url, headers=headers, data={'pType': "1", 'TotalRec': 1, 'pageNum': 1, 'oId': "709", 'lang': "0"})

    elif index_name == 'Tel 125':
        req = requests.post(url, headers=headers, data={'pType': "1", 'TotalRec': 1, 'pageNum': 1, 'oId': "137", 'lang': "0"})

    elif index_name == 'Tel 35':
        req = requests.post(url, headers=headers, data={'pType': "1", 'TotalRec': 1, 'pageNum': 1, 'oId': "142", 'lang': "0"})

    else:
        return 'Enter Valid Index'

    gov_bond_index_dict = req.json().get('Items')
    gov_bond_index_data = pd.DataFrame.from_records(gov_bond_index_dict)

    gov_bond_index_data = gov_bond_index_data.set_index('TradeDate')
    gov_bond_index_data.index = pd.to_datetime(gov_bond_index_data.index, format='%d/%m/%Y')
    gov_bond_index_data = gov_bond_index_data.sort_index()
    gov_bond_index_data.index = gov_bond_index_data.index.strftime('%d/%m/%Y')
    return gov_bond_index_data['CloseRate']

