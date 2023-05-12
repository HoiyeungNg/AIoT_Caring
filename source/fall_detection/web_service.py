import datetime
import requests
import json

def upload_body(body):
    try:
        # local server ip
        base_uri = 'http://192.168.50.209:8000/'
        globalbody_uri = base_uri + 'mycare/body'
        headers = {'content-type': 'application/json'}
        timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

        gbody = {
            "body_status": str(body),
            "update_time": timestamp
        }
        print(gbody)
        req = requests.post(globalbody_uri, headers=headers, data=json.dumps(gbody))
        print(req)
        if req.status_code >= 200 and req.status_code < 300:
            print("Body data uploaded successfully.")
        else:
            print("Failed to upload body data. Status code: ", req.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred during the HTTP POST request:", e)
    except ValueError as ve:
        print("Error converting temperature to float:", ve)
    except Exception as ex:
        print("An unexpected error occurred:", ex)

