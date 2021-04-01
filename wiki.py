#위키 백과 api

#-*- coding:utf-8 -*-
import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/WikiQA"
accessKey = "e307a6dd-d1ee-4123-8c43-5956d1e396c3"
question = "기리보이가 누구야?"
type = "hybridqa"
 
requestJson = {
"access_key": accessKey,
"argument": {
    "question": question,
    "type": type
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
                               