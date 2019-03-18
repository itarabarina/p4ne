#!/usr/local/bin/python3

import requests
import json
import pprint
import glob

banks=set()
cards_number = []
cards=[]

for current_file in glob.glob("/home/irina/Projects/python/Seafile/p4ne_training/*.json"):
    with open(current_file) as f:
        l = json.load(f)
        cards_number = cards_number + [str(j['CreditCard']['CardNumber'])[0:8] for j in l]

print(cards_number)


for i in cards_number:
   l='https://lookup.binlist.net/' + i
   #print(l)
   r=requests.get(l, headers={'Accept-Version': "3"})
   if 200 <= r.status_code <= 299:
        number = r.json()
        pprint.pprint(number)
        if number['bank']:
            if 'name' in number['bank']:
                bank = number['bank']['name']
                print(bank)
                banks.add(bank)
            else: print("Имя банка отсутствует")
   else: print("Запрос по карте с номером: ", i, "вернул ошибку", r.status_code)

print(sorted(banks))

