import os

from flask import Flask

from flask import request

import requests, json

app = Flask(__name__)

@app.route('/')
def hello():
    default_t = 10
    degree = request.args.get('apparent_t')
    if degree is not None and len(degree) != 0:
        try:
            default_t = float(degree)
        except:
            print("degree is not float, ignore")
    createErrorResponse = request.args.get('createErrorResponse')
    url = "http://www.bom.gov.au/fwo/IDN60801/IDN60801.95765.json"
    if (createErrorResponse == "True"):
        url += ".error"
    user_agent = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
    response_obj = requests.get(url, headers = user_agent)
    if response_obj.status_code != 200:
        rsp = {
                'error': "Error Connecting to BOM. Reason: " + response_obj.reason
            }
        rsp_code = 503
    else:
        response_text = response_obj.text
        response = json.loads(response_text)
        station_list = []
        item = {}
        for station in response['observations']['data']:
            if station['apparent_t'] > default_t:
                item = {
                        'name': station['name'],
                        'apparent_t': station['apparent_t'],
                        'lat': station['lat'],
                        'lon': station['lon']
                    }
                station_list.append(item)
                station_list.sort(key=lambda x: x.get('apparent_t'))
        print(station_list)
        rsp = {
                'response': station_list
            }
        rsp_code = 200
    return json.dumps(rsp), rsp_code
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
