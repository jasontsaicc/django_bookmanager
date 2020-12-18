from django.db import models

# Create your models here.
"""
1.定義模型
2.模型遷移
    2.1 生成遷移文件（只會創建一個 數據表和模型對應關係
     python manage.py makemigrations
    2.2在遷移（在數據庫生成表）
    python manage.py migrate
  3.操作數據庫

 要知道
 1.在那裡定義模型 (model)
 2.模型繼承自誰
 3.ORM對應關係
    表 》類
    字段 》屬性
"""

class BookInfo(models.Model):
    # 创建字段，字段类型...
    name = models.CharField(max_length=10)

# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo)