from django.db import models


# Create your models here.
class User(models.Model):
    # 用户账号、要唯一
    userId = models.CharField(max_length=20, unique=True)
    # 名字
    userName = models.CharField(max_length=20)
    # 国家
    userPlace = models.CharField(max_length=20)
    # token 验证值，每次登陆后都会更新
    userToken = models.CharField(max_length=50)

    @classmethod
    def createuser(cls, user_id, user_name, user_place, token):
        u = cls(userId=user_id, userName=user_name, userPlace=user_place, userToken=token)
        return u

    def __str__(self):
        return self.userId
