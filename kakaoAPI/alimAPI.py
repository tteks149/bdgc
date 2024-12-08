import hashlib
import hmac
import base64
import requests  # pip install requests
import time
import json

# 사용 예시
 # order_info = "매콤한떡볶이(tteks149)\n"\
        #             + " • 짜장면(1)\n"\
        #             + " • 짬뽕(2)\n"\
        #             + "\n"\
        #             + "매콤한떡볶이(tteks151)\n"\
        #             + " • 볶음밥(1)\n"\
        #             + " • 공기밥(1)\n"

        # my_order_info = "매콤한떡볶이(tteks151)\n"\
        #             + " • 볶음밥(1)\n"\
        #             + " • 공기밥(1)\n"

        # fail_reason = "파티장이 파티를 종료시켰습니다."
        # sendHostMatchFinMsgKakaoAPI("01031309920","14:20", "맘터","디지털관",order_info,"1000","15000","https://open.kakao.com/o/gJFstFde")
        # sendMatchFinMsgKakaoAPI("01031309920", "14:20", "맘터","디지털관",order_info, my_order_info,"1000","8000","https://open.kakao.com/o/gJFstFde" )
        # sendMatchFailMsgKakaoAPI("01031309920",fail_reason,"14:20","맘터","디지털관" , my_order_info)


def	make_signature(timestamp):
	
	access_key = "FKvwFQaA2ZzcFbJnKyTO"
	secret_key = "vSR6Z3qI0iNU9BdKVpw2ZceGH3K5uNHK1isIMymv"
	secret_key = bytes(secret_key, 'UTF-8')

	method = "POST"
	uri = "/alimtalk/v2/services/ncp:kkobizmsg:kr:2669423:bdgc/messages"

	message = method + " " + uri + "\n" + timestamp + "\n" + access_key
	message = bytes(message, 'UTF-8')
	signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())

	return signingKey

def sendAuthCodeKakaoAPI(phoneNum ,randNum):

    apiUrl = "https://sens.apigw.ntruss.com/alimtalk/v2/services/ncp:kkobizmsg:kr:2669423:bdgc/messages"

    content = "인증번호 [ " + randNum + " ] 를 입력해 주세요"


    timestamp = str(int(time.time() * 1000))
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'x-ncp-apigw-timestamp': timestamp,
        'x-ncp-iam-access-key': 'FKvwFQaA2ZzcFbJnKyTO',
        'x-ncp-apigw-signature-v2': make_signature(timestamp),
    }

    body = {
        "plusFriendId": "@배달가치",
        "templateCode": "phoneAuth",
        "messages": [
            {
                "to": phoneNum,
                "content": content,
            }
        ],
    }

    apiData = json.dumps(body)

    response = requests.post(url= apiUrl, headers=headers, data=apiData)

def sendHostMatchFinMsgKakaoAPI(phone_num, order_time, store_name, delivery_place , order_info ,delivery_per_price , order_price , openkakao_url):

    apiUrl = "https://sens.apigw.ntruss.com/alimtalk/v2/services/ncp:kkobizmsg:kr:2669423:bdgc/messages"

    content = "매칭이 완료되었습니다.\n\n" \
        + "어플을 통해서 주문을 시작해주세요.\n" \
        + "■ 주문 예상시간: " + order_time +  "\n\n" \
        + "■ 가게이름: " + store_name + "\n"\
        + "■ 배달장소: " + delivery_place + "\n\n" \
        + "■ 주문내역\n" + order_info + "\n" \
        + "■ 1인당 배달비: " + delivery_per_price + "원 \n" \
        + "■ 총 가격: " + order_price + "원 \n\n" \
        + "오픈카톡주소: " + openkakao_url

    timestamp = str(int(time.time() * 1000))
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'x-ncp-apigw-timestamp': timestamp,
        'x-ncp-iam-access-key': 'FKvwFQaA2ZzcFbJnKyTO',
        'x-ncp-apigw-signature-v2': make_signature(timestamp),
    }

    body = {
        "plusFriendId": "@배달가치",
        "templateCode": "matchFin",
        "messages": [
            {
                "to": phone_num,
                "content": content,
            }
        ],
    }

    apiData = json.dumps(body)

    response = requests.post(url= apiUrl, headers=headers, data=apiData)
    


def sendMatchFinMsgKakaoAPI(phone_num, order_time, store_name, delivery_place , order_info ,my_order_info,delivery_per_price , my_order_price , openkakao_url):

    apiUrl = "https://sens.apigw.ntruss.com/alimtalk/v2/services/ncp:kkobizmsg:kr:2669423:bdgc/messages"

    content = "매칭이 완료되었습니다.\n\n"\
        + "■ 주문 예상시간: " + order_time + "\n"\
        + "■ 가게이름: " + store_name + "\n"\
        + "■ 배달장소: " + delivery_place + "\n\n"\
        + "■ 파티 주문내역\n" + order_info + "\n"\
        + "■ 내 주문내역\n" + my_order_info + "\n"\
        + "■ 1인당 배달비: " + delivery_per_price + "원\n"\
        + "■ 내 결제 금액: " + my_order_price + "원\n\n"\
        + "오픈카톡에 참여해 주세요. \n\n"\
        + "오픈카톡주소: " + openkakao_url

    timestamp = str(int(time.time() * 1000))
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'x-ncp-apigw-timestamp': timestamp,
        'x-ncp-iam-access-key': 'FKvwFQaA2ZzcFbJnKyTO',
        'x-ncp-apigw-signature-v2': make_signature(timestamp),
    }

    body = {
        "plusFriendId": "@배달가치",
        "templateCode": "matchFinPt",
        "messages": [
            {
                "to": phone_num,
                "content": content,
            }
        ],
    }

    apiData = json.dumps(body)

    response = requests.post(url= apiUrl, headers=headers, data=apiData)
        


def sendMatchFailMsgKakaoAPI(phone_num, fail_reason, order_time, store_name, delivery_place , my_order_info):

    apiUrl = "https://sens.apigw.ntruss.com/alimtalk/v2/services/ncp:kkobizmsg:kr:2669423:bdgc/messages"

    content = "매칭이 실패되었습니다.\n\n" \
        + "■ 실패 사유: " + fail_reason + "\n\n"\
        + "■ 주문 예상시간: " + order_time + "\n" \
        + "■ 가게이름: " + store_name + "\n"\
        + "■ 배달장소: " + delivery_place + "\n\n" \
        + "■ 내 주문내역\n" + my_order_info + "\n\n"

    timestamp = str(int(time.time() * 1000))
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'x-ncp-apigw-timestamp': timestamp,
        'x-ncp-iam-access-key': 'FKvwFQaA2ZzcFbJnKyTO',
        'x-ncp-apigw-signature-v2': make_signature(timestamp),
    }

    body = {
        "plusFriendId": "@배달가치",
        "templateCode": "matchFail",
        "messages": [
            {
                "to": phone_num,
                "content": content,
            }
        ],
    }

    apiData = json.dumps(body)

    response = requests.post(url= apiUrl, headers=headers, data=apiData)
    

        