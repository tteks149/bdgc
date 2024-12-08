from django.shortcuts import render, redirect
from django.http import HttpResponse,  JsonResponse
from .models import Report , User

# 시간 관련
from django.utils import timezone # settings 내에서 SET_TZ = False 필요. 아니면 시차생김
# create_date= timezone.now().strftime("%Y-%m-%d %H:%M:%S") 형식


#로깅설정
import logging
logger = logging.getLogger('common')

# 아이피 추출
from config.get_client_ip import get_client_ip

# json
import json

# QueryDict
from django.http import QueryDict

def uploadReport(request):
    # 현재 아무파일 올릴수 있게 했는데, 이미지만 가능하게 바꿀필요 있음.

    try:    # 요청시 로그인 체크
    
        user_id = request.session.get('user')
        login_user = User.objects.get(user_id=user_id)

        if request.method == "GET":
            return render(request, 'common/upload_report.html')

        elif request.method == "POST":

            try:
                logger.info(str(get_client_ip(request)) + " : 회원가입 이메일 전송 요청")

                data = json.loads(request.body.decode('utf-8'))
                
                input_title = data['input_title']
                input_type = data['input_type']
                input_reason = data['input_reason']

                report = Report(
                    upload_user_id = login_user.user_id,
                    title = input_title,
                    type = input_type,
                    reason = input_reason,
                    # file_path = upload_file,
                    created_time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
                )

                report.save()
           
                return JsonResponse({'message': '업로드 성공' , 'success': True})

            except:
                return JsonResponse({'message': '서버에러 발생' , 'success': False})

        else:
            return render(request, 'error.html', {"error" :"올바른 접근이 아닙니다"})

    except User.DoesNotExist:
       return render(request, 'error.html', {"error" :"로그인을 확인해 주세요"})

    except:
        return render(request, 'error.html', {"error" :"로그인을 확인해 주세요"})


def uploadReportSuccess(request):
    if request.method == "GET":   
        return render(request, 'common/upload_report_success.html')