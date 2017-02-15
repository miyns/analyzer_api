from rest_framework import serializers

from .models import VDay


class VDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = VDay
        fields = ('target','date','day','low','high','open','close','pips','pips_ratio')

class VDayAnnotateSerializer(serializers.ModelSerializer):
    avg_pips_ratio = serializers.IntegerField()
    cnt = serializers.IntegerField()
    up = serializers.IntegerField()
    down = serializers.IntegerField()
    equal = serializers.IntegerField()
    
    class Meta:
        model = VDay
        fields = ('date','avg_pips_ratio','cnt','up','down','equal')