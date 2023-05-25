from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class DepositProducts(models.Model):
    
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    customers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='subscriped_products', null=True)

    def __str__(self):
        return self.fin_prdt_nm

class DepositOptions(models.Model):
    fin_co_no = models.TextField()
    fin_prdt_cd = models.TextField()
    intr_rate_type = models.CharField(max_length=100)
    intr_rate_type_nm = models.CharField(max_length=100)
    save_trm = models.TextField()
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField()

    def __str__(self):
        return f"{self.fin_prdt_cd} - {self.intr_rate_type_nm}"