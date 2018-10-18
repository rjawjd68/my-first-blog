from django.db import models
from django.utils import timezone

class Post(models.Model): #모델Object를 정의하는 코드
    #modles은 Post가 장고 모델임을 의미함. 장고 Post가 DB에 저장 되어야 한다고 알게 된다.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #Foreignkey: 다른 모델에 대한 링크
    title = models.CharField(max_length=200)
    #modles.CharField:글자 수 제한된 텍스트를 정의
    text = models.TextField()
    #글자 수 제한이 없는 긴 텍스트를 위한 속성
    created_date = models.DateTimeField(
        default=timezone.now) #날짜와 시간
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
