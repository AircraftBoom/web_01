from django.db import models    # 数据库的基类
from django.utils import timezone

class FamilyMember(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateTimeField(default=timezone.now)
    age = models.IntegerField(default=0)
    height = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.name)