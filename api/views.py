import django_filters
from rest_framework import viewsets, filters
from .models import VDay
from .serializer import VDaySerializer, VDayAnnotateSerializer
from django.db.models import Avg,Count,Case,Value,When,IntegerField
from django.shortcuts import render

# Create your views here.


class VDayViewSet(viewsets.ModelViewSet):
    queryset = VDay.objects.all()
    serializer_class = VDaySerializer

# dateでGroupBy


class VDayAnnotateViewSet(viewsets.ModelViewSet):
    queryset = VDay.objects.all()
    serializer_class = VDayAnnotateSerializer

    def get_queryset(self):
        return VDay.objects.values('date').annotate(
            avg_pips_ratio=Avg('pips_ratio'),
            cnt=Count('day'),
            #.extra(select={'is_recent': 'pips_ratio > 0 or NULL'})
            #up=Count('is_recent') / Count('day') * 100
            up=Count(
                Case(
                    When(pips_ratio__gt=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('day') * 100,
            down=Count(
                Case(
                    When(pips_ratio__lt=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('day') * 100,
            equal=Count(
                Case(
                    When(pips_ratio=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('day') * 100,
        )


# select
# day ,
# avg(pips_ratio) avg_pips_ratio ,
# count(*) cnt ,
# count(pips_ratio > 0 or NULL) / count(*) * 100 up , count(pips_ratio < 0 or NULL) / count(*) * 100 down , count(pips_ratio = 0 or NULL) / count(*) * 100 equal
# from v_day
# where target like '%/JPY'
# group by day order by up desc , avg_pips_ratio desc;
