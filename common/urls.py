from django.urls import path
from . import views, activate , mypage, report, signup

app_name = 'common'

urlpatterns = [
   
    path('login/', views.login, name='login'), # 로그인 
    path('logout/', views.logout, name='logout'), # 로그아웃

    path('withdrawal/', views.withdrawal, name='withdrawal'), # 회원탈퇴

    path('signup/', signup.signup, name='signup'), # 회원가입 . 맨처음 이메일 전송부분.
    path('activate_signup/<str:uid64>/<str:token>/', activate.activateSignUp, name='activateSignUp'), # 회원가입 . 
    path('activate_signup/<str:uid64>/<str:token>/send_auth_code_kakaoApi', activate.sendAuthCodeKakaoApi, name='sendAuthCodeKakaoApi'), # 아이디 중복 검사
    path('activate_signup/<str:uid64>/<str:token>/check_auth_code', activate.checkAuthCode, name='sendAuthCodeKakaoApi'), # 아이디 중복 검사
    

    path('signup/id_duplicate_check/', signup.idDuplicateCheck, name='idDuplicateCheck'), # 아이디 중복 검사
    path('signup/email_duplicate_check/', signup.emailDuplicateCheck, name='emailDuplicateCheck'), # 이메일 중복 검사
    path('signup/email_submit/', signup.signUpEmailSubmit, name='signUpEmailSubmit'), # 회원가입 링크 이메일 전송

    path('find_id/', views.findId, name='findId'), # 아이디 찾기
    path('change_password/', views.changePassword, name='changePassword'), # 비밀번호 변경
    path('activate_pwd/<str:uid64>/<str:token>/', activate.activatePassword, name="activatePassword"), # 메일 확인후, 비밀번호 변경 페이지 이동.

    path('myPage/', mypage.mainPage, name='mainPage'), # 내정보
    path('myPage/check_myinfo', mypage.checkMyInfo, name='checkMyInfo'), # 내정보 조회
    path('myPage/validate_password', mypage.validatePassword, name='validatePassword'), # 비밀번호 검증
    path('myPage/modify_nick_name', mypage.modifyNickname, name='modifyNickName'),  # 닉네임 변경
    path('myPage/modify_place', mypage.modifyPlace, name='modifyPlace'),            # 장소 변경
    path('myPage/modify_password', mypage.modifyPassword, name='modifyPassword'),   # 비밀번호 변경 변경

    # path('upload_report/', report.uploadReport, name='uploadReport'), # 신고 업로드
    # path('upload_report/success', report.uploadReportSuccess, name='uploadReportSuccess'), # 신고 업로드


]
