''' api routing '''
from rest_framework import routers

from .views import (VDayGroupByDayTargetViewSet, VDayGroupByDayViewSet,
                    VDayofweekGroupByDowTargetViewSet,
                    VDayofweekGroupByDowViewSet, VDayofweekViewSet,
                    VDayViewSet, VMonthGroupByMonthTargetViewSet,
                    VMonthGroupByMonthViewSet, VMonthViewSet,
                    VWeekGroupByWeekTargetViewSet, VWeekGroupByWeekViewSet,
                    VWeekViewSet,VWeekGroupByWeekTargetDetailViewSet)

router = routers.DefaultRouter()

# ViewSetのquerysetが一致するとapi一覧のURLが正しく登録されない(Distinctされてしまう)ので、
# base_nameを指定することにより区別している
# base_nameを指定しなくてもそれぞれのapiのURL自体は問題ない（api一覧ページ上の問題）
# 同じquerysetを異なるViewSetで扱うユースケースが妥当ではないのかもしれない

router.register(r'vdays', VDayViewSet, base_name='vdays')
router.register(r'vdays_day', VDayGroupByDayViewSet, base_name='vdays_day')
router.register(r'vdays_daytarget', VDayGroupByDayTargetViewSet, base_name='vdays_daytarget')

router.register(r'vdayofweeks', VDayofweekViewSet, base_name='vdayofweeks')
router.register(r'vdayofweeks_dow', VDayofweekGroupByDowViewSet, base_name='vdayofweeks_dow')
router.register(r'vdayofweeks_dowtarget', VDayofweekGroupByDowTargetViewSet, base_name='vdayofweeks_dowtarget')

router.register(r'vweeks', VWeekViewSet, base_name='vweeks')
router.register(r'vweeks_week', VWeekGroupByWeekViewSet, base_name='vweeks_week')
router.register(r'vweeks_week_detail' , VWeekGroupByWeekTargetDetailViewSet,base_name='vweeks_week_detail')
router.register(r'vweeks_weektarget', VWeekGroupByWeekTargetViewSet, base_name='vweeks_weektarget')


router.register(r'vmonths', VMonthViewSet, base_name='vmonth')
router.register(r'vmonths_month', VMonthGroupByMonthViewSet, base_name='vmonth_month')
router.register(r'vmonths_monthtarget', VMonthGroupByMonthTargetViewSet, base_name='vmonth_monthtarget')
