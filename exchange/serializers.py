from rest_framework import serializers

class ExchangeRateSerializer(serializers.Serializer):
    cur_unit = serializers.CharField()
    ttb = serializers.CharField()
    tts = serializers.CharField()
    deal_bas_r = serializers.CharField()
    bkpr = serializers.CharField()
    yy_efee_r = serializers.CharField()
    ten_dd_efee_r = serializers.CharField()
    kftc_bkpr = serializers.CharField()
    kftc_deal_bas_r = serializers.CharField()
    cur_nm = serializers.CharField()

