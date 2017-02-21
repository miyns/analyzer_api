"""django rest_framework serializer"""
from rest_framework import serializers

from .models import VDay, VWeek, VMonth, VDayofweek


class VDaySerializer(serializers.ModelSerializer):

    class Meta:
        model = VDay
        fields = ('target', 'date', 'day', 'low', 'high',
                  'open', 'close', 'pips', 'pips_ratio')


class VDayGroupByDaySerializer(serializers.ModelSerializer):
    avg_pips_ratio = serializers.DecimalField(max_digits=10, decimal_places=4)
    cnt = serializers.IntegerField()
    up = serializers.IntegerField()
    down = serializers.IntegerField()
    equal = serializers.IntegerField()

    class Meta:
        model = VDay
        fields = ('day', 'avg_pips_ratio', 'cnt', 'up', 'down', 'equal')


class VDayGroupByDayTargetSerializer(serializers.ModelSerializer):
    avg_pips_ratio = serializers.DecimalField(max_digits=10, decimal_places=4)
    cnt = serializers.IntegerField()
    up = serializers.IntegerField()
    down = serializers.IntegerField()
    equal = serializers.IntegerField()

    class Meta:
        model = VDay
        fields = ('day', 'target', 'avg_pips_ratio',
                  'cnt', 'up', 'down', 'equal')

# VDayofweek


class VDayofweekSerializer(serializers.ModelSerializer):

    class Meta:
        model = VDayofweek
        fields = ('target', 'date', 'dow', 'low', 'high',
                  'open', 'close', 'pips', 'pips_ratio')


class VDayofweekGroupByDowSerializer(serializers.ModelSerializer):
    avg_pips_ratio = serializers.DecimalField(max_digits=10, decimal_places=4)
    cnt = serializers.IntegerField()
    up = serializers.IntegerField()
    down = serializers.IntegerField()
    equal = serializers.IntegerField()

    class Meta:
        model = VDayofweek
        fields = ('dow', 'avg_pips_ratio', 'cnt', 'up', 'down', 'equal')


class VDayofweekGroupByDowTargetSerializer(serializers.ModelSerializer):
    avg_pips_ratio = serializers.DecimalField(max_digits=10, decimal_places=4)
    cnt = serializers.IntegerField()
    up = serializers.IntegerField()
    down = serializers.IntegerField()
    equal = serializers.IntegerField()

    class Meta:
        model = VDayofweek
        fields = ('dow', 'target', 'avg_pips_ratio',
                  'cnt', 'up', 'down', 'equal')


# VWeek
class VWeekSerializer(serializers.ModelSerializer):

    class Meta:
        model = VWeek
        fields = ('target', 'yyyy_week', 'week', 'date_from', 'date_to',
                  'cnt', 'low', 'high', 'open', 'close', 'pips', 'pips_ratio')


class VWeekGroupByWeekSerializer(serializers.ModelSerializer):
    avg_pips_ratio = serializers.DecimalField(max_digits=10, decimal_places=4)
    cnt = serializers.IntegerField()
    up = serializers.IntegerField()
    down = serializers.IntegerField()
    equal = serializers.IntegerField()

    class Meta:
        model = VWeek
        fields = ('week', 'avg_pips_ratio', 'cnt', 'up', 'down', 'equal')


class VWeekGroupByWeekTargetSerializer(serializers.ModelSerializer):
    avg_pips_ratio = serializers.DecimalField(max_digits=10, decimal_places=4)
    cnt = serializers.IntegerField()
    up = serializers.IntegerField()
    down = serializers.IntegerField()
    equal = serializers.IntegerField()

    class Meta:
        model = VWeek
        fields = ('week', 'target', 'avg_pips_ratio',
                  'cnt', 'up', 'down', 'equal')

class VWeekGroupByWeekTargetDetailSerializer(serializers.ModelSerializer):
    date_from = serializers.DateField
    date_to = serializers.DateField

    class Meta:
        model = VDay
        fields = ('date','target','week','open', 'close','ema12','ema26','pips','pips_ratio')

# VMonth
class VMonthSerializer(serializers.ModelSerializer):

    class Meta:
        model = VMonth
        fields = ('target', 'yyyy_mm', 'mm', 'date_from', 'date_to',
                  'cnt', 'low', 'high', 'open', 'close', 'pips', 'pips_ratio')


class VMonthGroupByMonthSerializer(serializers.ModelSerializer):
    avg_pips_ratio = serializers.DecimalField(max_digits=10, decimal_places=4)
    cnt = serializers.IntegerField()
    up = serializers.IntegerField()
    down = serializers.IntegerField()
    equal = serializers.IntegerField()

    class Meta:
        model = VMonth
        fields = ('mm', 'avg_pips_ratio', 'cnt', 'up', 'down', 'equal')


class VMonthGroupByMonthTargetSerializer(serializers.ModelSerializer):
    avg_pips_ratio = serializers.DecimalField(max_digits=10, decimal_places=4)
    cnt = serializers.IntegerField()
    up = serializers.IntegerField()
    down = serializers.IntegerField()
    equal = serializers.IntegerField()

    class Meta:
        model = VMonth
        fields = ('mm', 'target', 'avg_pips_ratio',
                  'cnt', 'up', 'down', 'equal')
