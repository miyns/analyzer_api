import django_filters
import logging
from django.db.models import Avg, Case, Count, IntegerField, Value, When
from django.shortcuts import render
from rest_framework import filters, viewsets

from .models import VDay, VDayofweek, VMonth, VWeek
from .serializer import (VDayGroupByDaySerializer,
                         VDayGroupByDayTargetSerializer,
                         VDayofweekGroupByDowSerializer,
                         VDayofweekGroupByDowTargetSerializer,
                         VDayofweekSerializer, VDaySerializer,
                         VMonthGroupByMonthSerializer,
                         VMonthGroupByMonthTargetSerializer, VMonthSerializer,
                         VWeekGroupByWeekSerializer,
                         VWeekGroupByWeekTargetSerializer, VWeekSerializer,
                         VWeekGroupByWeekTargetDetailSerializer)


# Create your views here.


class VDayViewSet(viewsets.ModelViewSet):
    queryset = VDay.objects.all()
    serializer_class = VDaySerializer

# dayでGroupBy


class VDayGroupByDayViewSet(viewsets.ModelViewSet):
    queryset = VDay.objects.all()
    serializer_class = VDayGroupByDaySerializer

    def get_queryset(self):
        return VDay.objects.filter(target__contains='/JPY').values('day').annotate(
            avg_pips_ratio=Avg('pips_ratio'),
            cnt=Count('day'),
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
        ).order_by('-up', '-avg_pips_ratio')

# dayとtaretでGroupBy


class VDayGroupByDayTargetViewSet(viewsets.ModelViewSet):
    queryset = VDay.objects.all()
    serializer_class = VDayGroupByDayTargetSerializer

    def get_queryset(self):
        return VDay.objects.filter(target__contains='/JPY').values('day', 'target').annotate(
            avg_pips_ratio=Avg('pips_ratio'),
            cnt=Count('day'),
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
        ).order_by('-up', '-avg_pips_ratio')

# VDayofweek


class VDayofweekViewSet(viewsets.ModelViewSet):
    queryset = VDayofweek.objects.all()
    serializer_class = VDayofweekSerializer

# dowでGroupBy


class VDayofweekGroupByDowViewSet(viewsets.ModelViewSet):
    queryset = VDayofweek.objects.all()
    serializer_class = VDayofweekGroupByDowSerializer

    def get_queryset(self):
        return VDayofweek.objects.filter(target__contains='/JPY').values('dow').annotate(
            avg_pips_ratio=Avg('pips_ratio'),
            cnt=Count('dow'),
            up=Count(
                Case(
                    When(pips_ratio__gt=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('dow') * 100,
            down=Count(
                Case(
                    When(pips_ratio__lt=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('dow') * 100,
            equal=Count(
                Case(
                    When(pips_ratio=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('dow') * 100,
        ).order_by('-up', '-avg_pips_ratio')

# dowとtaretでGroupBy


class VDayofweekGroupByDowTargetViewSet(viewsets.ModelViewSet):
    queryset = VDayofweek.objects.all()
    serializer_class = VDayofweekGroupByDowTargetSerializer

    def get_queryset(self):
        return VDayofweek.objects.filter(target__contains='/JPY').values('dow', 'target').annotate(
            avg_pips_ratio=Avg('pips_ratio'),
            cnt=Count('dow'),
            up=Count(
                Case(
                    When(pips_ratio__gt=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('dow') * 100,
            down=Count(
                Case(
                    When(pips_ratio__lt=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('dow') * 100,
            equal=Count(
                Case(
                    When(pips_ratio=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('dow') * 100,
        ).order_by('-up', '-avg_pips_ratio')


# VWeek
class VWeekViewSet(viewsets.ModelViewSet):
    queryset = VWeek.objects.all()
    serializer_class = VWeekSerializer

# WeekでGroupBy


class VWeekGroupByWeekViewSet(viewsets.ModelViewSet):
    queryset = VWeek.objects.all()
    serializer_class = VWeekGroupByWeekSerializer

    def get_queryset(self):
        return VWeek.objects.filter(target__contains='/JPY').values('week').annotate(
            avg_pips_ratio=Avg('pips_ratio'),
            cnt=Count('week'),
            up=Count(
                Case(
                    When(pips_ratio__gt=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('week') * 100,
            down=Count(
                Case(
                    When(pips_ratio__lt=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('week') * 100,
            equal=Count(
                Case(
                    When(pips_ratio=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('week') * 100,
        ).order_by('-up', '-avg_pips_ratio')

# dayとtaretでGroupBy


class VWeekGroupByWeekTargetViewSet(viewsets.ModelViewSet):
    queryset = VWeek.objects.all()
    serializer_class = VWeekGroupByWeekTargetSerializer

    def get_queryset(self):
        return VWeek.objects.filter(target__contains='/JPY').values('week', 'target').annotate(
            avg_pips_ratio=Avg('pips_ratio'),
            cnt=Count('week'),
            up=Count(
                Case(
                    When(pips_ratio__gt=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('week') * 100,
            down=Count(
                Case(
                    When(pips_ratio__lt=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('week') * 100,
            equal=Count(
                Case(
                    When(pips_ratio=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('week') * 100,
        ).order_by('-up', '-avg_pips_ratio')


class VWeekGroupByWeekTargetDetailViewSet(viewsets.ModelViewSet):
    query = VDay.objects.all()
    serializer_class = VWeekGroupByWeekTargetDetailSerializer
    def get_queryset(self):
        # logger = logging.getLogger('command')
        # logger.error('self.request')
        # logger.error(self.request.query_params['target'])
        params = self.request.query_params
        target = params['target']#[0:3] + "/" + params['target'][3:6]
        return VDay.objects.filter(target=target,week=params['week']).order_by('date')

# VMonth
class VMonthViewSet(viewsets.ModelViewSet):
    queryset = VMonth.objects.all()
    serializer_class = VMonthSerializer

# MonthでGroupBy


class VMonthGroupByMonthViewSet(viewsets.ModelViewSet):
    queryset = VMonth.objects.all()
    serializer_class = VMonthGroupByMonthSerializer

    def get_queryset(self):
        return VMonth.objects.filter(target__contains='/JPY').values('mm').annotate(
            avg_pips_ratio=Avg('pips_ratio'),
            cnt=Count('mm'),
            up=Count(
                Case(
                    When(pips_ratio__gt=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('mm') * 100,
            down=Count(
                Case(
                    When(pips_ratio__lt=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('mm') * 100,
            equal=Count(
                Case(
                    When(pips_ratio=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('mm') * 100,
        ).order_by('-up', '-avg_pips_ratio')

# dayとtaretでGroupBy


class VMonthGroupByMonthTargetViewSet(viewsets.ModelViewSet):
    queryset = VMonth.objects.all()
    serializer_class = VMonthGroupByMonthTargetSerializer

    def get_queryset(self):
        return VMonth.objects.filter(target__contains='/JPY').values('mm', 'target').annotate(
            avg_pips_ratio=Avg('pips_ratio'),
            cnt=Count('mm'),
            up=Count(
                Case(
                    When(pips_ratio__gt=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('mm') * 100,
            down=Count(
                Case(
                    When(pips_ratio__lt=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('mm') * 100,
            equal=Count(
                Case(
                    When(pips_ratio=0, then=Value(1)),
                    defalut=Value(0),
                    # Case.output_field=IntegerField()
                )
            ) / Count('mm') * 100,
        ).order_by('-up', '-avg_pips_ratio')
