from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

#models의 baseUserManager를 상속받아 커스텀 userManager를 만듬. 이를 통해 user를 생성할 수 있다.
    
#user를 저장하는 테이블
class User(AbstractBaseUser):

    #user 기본정보
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    area = models.ForeignKey('Area', on_delete=models.CASCADE, null=True)
    job = models.ForeignKey('Job', on_delete=models.CASCADE, null=True)
    #키워드, site개수
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #다대다 관계는 테이블이 추가되는데 자동으로 생성된다. 하지만 중간 테이블을 직접 만들면 추가적인 정보를 저장할 수 있다.

    USERNAME_FIELD = 'user_id'

    class Meta:
        db_table = 'User'

    def __str__(self):
            """String for representing the Model object."""
            return self.username

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module(self, app_label):
        return True
    
    
    
class Job(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'Job'

    def __str__(self):
        return self.name

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    province = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    details = models.CharField(max_length=200, null=True)
    class Meta:
        db_table = 'Area'
    def __str__(self):
        return self.province + ' ' + self.city + ' ' + self.details
    