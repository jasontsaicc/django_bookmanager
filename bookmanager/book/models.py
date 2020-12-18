from django import models

# Create your models here.

# """"
# # 1.定義模型
# # 2.模型遷移
# # 3.操作數據庫
#
# 要知道
# 1.在那裡定義模型 (model)
# 2.模型繼承自誰
# 3.ORM對應關係
# 表 》類
# 字段 》屬性

class BookInfo(models.Model):
    name = models.CharField(max_length=10)

class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    #性別
    gender = models.BooleanField()
    # 外鍵
    book = models.ForeignKey(BookInfo)