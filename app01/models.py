from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=2)

# UserInfo.objects.create(name="小路",password="asdf",age=19)



"""以上UserInfo相當於在MySQL輸入以下:
create table app01_userinfo(
    id bignit auto_increment primary key,    <<<Django自動創建的
    name varchar(32),
    password varchar(64),
    age int
)
"""

class Department(models.Model):
    title = models.CharField(max_length=16)


