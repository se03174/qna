
#-*- coding:utf-8 -*-
#질의응답 api

import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/WiseQAnal"
accessKey = "e307a6dd-d1ee-4123-8c43-5956d1e396c3"
text = "한복은 어느 나라의 옷인가요?"
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        "text": text
    }
}
 
http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)
 
print("[responseCode] " + str(response.status))
print("[responBody]")
print(str(response.data,"utf-8"))
                                  