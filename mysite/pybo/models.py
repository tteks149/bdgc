from django.db import models

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    # __str__ 메서드 추가. id 값 대신에 제목을 표시.
    def __str__(self):
        return self.subject
# 제목 subject , 내용 content , 작성일시 create_date 
# max_length=200 말그대로 글자수 200자 ,  CharField 글자수 제한이면 사용
# TextField 글자수 제한 없음



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

# ForeignKey 다른 모델과 연결.  
#  on_delete=models.CASCADE 질문 삭제시 답변 삭제 .. 부모 삭제시 자식 삭제
