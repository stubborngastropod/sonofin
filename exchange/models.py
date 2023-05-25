from django.db import models

class ExchangeRate(models.Model):
    cur_unit = models.CharField(max_length=10)
    ttb = models.DecimalField(max_digits=10, decimal_places=2)
    tts = models.DecimalField(max_digits=10, decimal_places=2)
    deal_bas_r = models.DecimalField(max_digits=10, decimal_places=2)
    bkpr = models.DecimalField(max_digits=10, decimal_places=2)
    yy_efee_r = models.DecimalField(max_digits=10, decimal_places=2)
    ten_dd_efee_r = models.DecimalField(max_digits=10, decimal_places=2)
    kftc_bkpr = models.DecimalField(max_digits=10, decimal_places=2)
    kftc_deal_bas_r = models.DecimalField(max_digits=10, decimal_places=2)
    cur_nm = models.CharField(max_length=50)
