import requests
from PyKakao import Message



api = Message(service_key=secrets.KEYS["restApi"])
auth_url = api.get_url_for_generating_code()
print(auth_url)


'https://localhost:5000/?code=rt2OifB7dmC4d5JTWy_B3HyzFP_BCeDMg4ZwqJj2qLuKEXWOMRu-EF04f4kIPDQPkZ4lVQo9dNsAAAGFw2-1Tg'

method = 'POST'
baseurl = 'https://kapi.kakao.com/v2/api/'
api_talktome = 'talk/memo/default/send'
headers = {
    'Content-Type: application/x-www-form-urlencoded'
    f'Authorization: Bearer ${secrets.KEYS['']}'
}

requests.request(method=method, url=baseurl+api_talktome, headers=headers)
'''

curl -v -X POST "https://kapi.kakao.com/v2/api/talk/memo/default/send" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}" \
    --data-urlencode 'template_object={
        "object_type": "text",
        "text": "텍스트 영역입니다. 최대 200자 표시 가능합니다.",
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
        "button_title": "바로 확인"
    }'

'''