
#-*- coding:utf-8 -*-
#기계 독해 api

import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/MRCServlet"
accessKey = "e307a6dd-d1ee-4123-8c43-5956d1e396c3"
question = "구어의 반댓말은 무엇인가?"
passage = "문어(文語)란 문자를 매개로 한 언어이며, 구어의 반댓말이다. 문어는 고정된 문법 체계를 가지고 있으므로 구어에 비해 변화가 적고 시공을 초월해 전달될 수 있다. 현대의 일상회화에서 사용되는 구어체에 비해 잘 쓰이지 않는다. 구시대의 표현이 많은 글을 문어문이라고 하며, 이런 문장양식을 문어체라고 한다. 한국어의 경우, 1894년 갑오개혁 이전 언문일치가 이루어지기 전의 문자언어는 거의 한문투였으므로, 구어체와 다른 이중언어생활이 이루어졌다. 그 뒤 언론매체에 구어체를 사용한 문학작품들이 발표되면서 언문일치가 이루어졌으나, 구어체를 사용한 글이 경박하다는 인식으로 인해 의고체에 바탕을 둔 문어체는 권위를 요구하는 글에 주로 사용되고 있다."
 
requestJson = {
"access_key": accessKey,
    "argument": {
        "question": question,
        "passage": passage
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
                                  