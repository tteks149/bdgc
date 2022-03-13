from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date') 
        # 질문 목록 데이터. order_by = 조회결과 정렬 , -create_date 작성일시 역순(-) 즉, 최신순.
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


# 템플릿 파일 작성. config/settings.py TEMPLATES 항목