from django.db import models

# Create your models here.

class AppUserInfo(models.Model):
    """

    """
    user_id = models.AutoField(primary_key=True)#用户id
    name = models.CharField(max_length=200, blank=True, null=False)#用户名称
    age = models.IntegerField(null=False, blank=False)#用户年龄
    gender = models.CharField(max_length=200, blank=True, null=False)#用户性别
    agreement = models.PositiveIntegerField(default=0)
    account = models.IntegerField(null=False, blank=False)#账号
    password = models.IntegerField(null=False, blank=False)#密码
    del_flag = models.PositiveIntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'app_user_info'


class UserClassInfo(models.Model):
    info_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=False, blank=False)
    stair_class = models.IntegerField(null=False, blank=False)  # 一级分类
    second_class = models.IntegerField(null=False, blank=False)  # 二级分类
    del_flag = models.PositiveIntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'user_class_info'