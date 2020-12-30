from django.db import models


# Create your models here.


class BookInfo(models.Model):
    # 创建字段，字段类型...
    name = models.CharField(max_length=20)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0)
    description = models.CharField(max_length=200, null=True)
    # 下面是外键设置
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'peopleinfo'

    def __str__(self):
        return self.name
