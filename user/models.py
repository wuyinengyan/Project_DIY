from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=20, null=False, verbose_name="用户名")
    password = models.CharField(max_length=128, null=False, verbose_name="密码")
    create_datetime = models.DateTimeField(verbose_name="创建时间")

    class Meta:
        db_table = "user"

    def __repr__(self):
        return f"{self.id}/{self.name}"

    __str__ = __repr__
