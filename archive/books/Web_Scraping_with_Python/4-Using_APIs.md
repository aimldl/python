데이터 수집을 위해서 일반적으로 쓰이는 방법은 API와 Web Scraping이 있습니다. 이렇게 얻은 정보는 별도로 이용되기도 하지만, API와 스크랩된 정보를 합쳐서 더 유용한 정보로 만들기도 합니다.

API는 HTTP로 특정 데이터를 요청 (Request)하고, XML이나 JSON형태로 데이터를 리턴 (Return) 받습니다. JSON이 인코딩 방식으로 많이 쓰이고 있지만, 아직도 많은 API들이 XML을 지원합니다. JSON은 데이터를 딕셔너리 (Dictionary)와 같은 포맷으로 구성됩니다. 그러므로 Key: Value로 값을 받게 됩니다.

ESPN APIs: 운동선수, 경기 점수 등 정보
Google APIs: 

https://console.developers.google.com/apis/dashboard?project=lid-test-01-1566455036696

API 사용예

API는 일반적으로 따르는 형태가 있지만, 어떤 API는 이런 형태에서 약간 벗어날 수 있으므로 API에 관해 많은 경험이 있더라도 목표로 하는 API의 문서를 읽는 것이 중요해집니다.

Methods
* GET, POST, PUT DELETE
* GET은 HTTP 호출을 할 때 쓰인다.
* POST는 폼 (Form)을 채우거나 정보를 제출할 때 쓰인다.
* PUT은 object나 정보를 업데이트할 때 쓰인다.
* DELETE은 object를 지울 때 쓰인다.

인증 (Authentication)
http://your.web.site/api/version/item?api_key=<your_api_key>%itemname=value_item&format=json&start=0&results=100

응답 (Response)

