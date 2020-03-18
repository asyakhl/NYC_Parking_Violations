import urllib3
import json

http = urllib3.PoolManager()
data={"plate": "HND4749"}
encoded_data = json.dumps(data).encode('utf-8')
endpoint = "http://localhost:9200/parking_violation_records/records"
r = http.request('POST', endpoint, body=encoded_data, headers={'Content-Type': 'application/json'})
print(r.data)

