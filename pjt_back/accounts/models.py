from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass

class DetailUser(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    GENDER_CHOICES = [
        ("남성", "남성"),
        ("여성", "여성"),
    ]

    GOAL_CHOICES = [
        ("내 집 마련", "내 집 마련"),
        ("내 차 마련", "내 차 마련"),
        ("목돈 마련", "목돈 마련"),
        ("여행 경비", "여행 경비"),
    ]
    BANK_CHOICES = (
        # ('모델에 설정할 값', '사람이 읽을수 있는 이름')
        ('우리은행','우리은행'),
        ('한국스탠다드차타드은행','한국스탠다드차타드은행'),
        ('대구은행','대구은행'),
        ('부산은행','부산은행'),
        ('광주은행','광주은행'),
        ('제주은행','제주은행'),
        ('전북은행','전북은행'),
        ('경남은행','경남은행'),
        ('중소기업은행','중소기업은행'),
        ('한국산업은행','한국산업은행'),
        ('국민은행','국민은행'),
        ('신한은행','신한은행'),
        ('농협은행','농협은행'),
        ('KEB하나은행','KEB하나은행'),
        ('수협은행','수협은행'),
        ('주식회사 카카오뱅크','주식회사 카카오뱅크'),
        ('주식회사 케이뱅크','주식회사 케이뱅크'),
        ('토스뱅크 주식회사','토스뱅크 주식회사'),
        ('기타','기타')
    )
    nickname = models.CharField(max_length=20, null=True)
    birthday = models.CharField(max_length=8, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=255, null=True)
    main_bank = models.CharField(max_length=12, choices=BANK_CHOICES, null=True)
    asset = models.IntegerField(null=True)
    salary = models.IntegerField(null=True)
    goal = models.CharField(max_length=10, choices=GOAL_CHOICES, null=True)