import random
import requests
import urllib3
import json
import time
import datetime

now = datetime.datetime.now().strftime('%H:%M:%S')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
if __name__ == '__main__':
    orderDate = '20230121'
    method = 'POST'
    url = 'https://www.bustago.or.kr/newweb/kr/ticket/ticketListJson3.do'
    data = {
        'startType': 'S',
        f'orderDate': {orderDate},
        'orderBackDate': '',
        'depTerId': '0001',
        'arrTerId': '5060',
        'depTime': '0000',
        'arrTime': '0000',
        'goBusGrade': '',
        'goBackBusGrade': ''
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'www.bustago.or.kr',
        'Origin': 'https://www.bustago.or.kr',
        'Referer': 'https://www.bustago.or.kr/newweb/kr/ticket/ticket.do'

    }
    while True:
        res = requests.request(method, url, data=data, headers=headers)
        json_object = json.loads(res.text)['ticketSingleList']
        for i in range(len(json_object)):
            if json_object[i]['REMAIN_CNT'] != '00':
                print(f'!!!!!!!!!! {now} ' + json_object[i]['DEP_TIME'] + '!!!!!!!!!!')
        print("Done")
        t = random.sample(range(5, 10), 1)[0]
        time.sleep(t)
