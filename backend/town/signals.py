from apscheduler.schedulers.background import BackgroundScheduler
import logging
from .models import Town
from django.db.models import Avg

logger = logging.getLogger(__name__)

def update_town_rank():
    # town 평점을 업데이트하는 시그널 핸들러
    # 모든 Town 인스턴스 가져오기
    all_towns = Town.objects.all()

    for town in all_towns:
        town_review_avg = town.town_review_set.aggregate(
            area_welfare_avg=Avg('area_welfare'),
            town_welfare_avg=Avg('town_welfare'),
            town_culture_avg=Avg('town_culture'),
            town_facility_avg=Avg('town_facility'),
            town_citizen_avg=Avg('town_citizen')
        )
        if None in town_review_avg.values():
            continue
        area_welfare_avg = town_review_avg['area_welfare_avg']
        town_welfare_avg = town_review_avg['town_welfare_avg']
        town_culture_avg = town_review_avg['town_culture_avg']
        town_facility_avg = town_review_avg['town_facility_avg']
        town_citizen_avg = town_review_avg['town_citizen_avg']

        # 각 필드의 평균을 더해서 전체 평균 계산
        total_avg = (area_welfare_avg + town_welfare_avg + town_culture_avg + town_facility_avg + town_citizen_avg) / 5
        town.star = total_avg
        town.area_welfare = area_welfare_avg
        town.town_welfare = town_welfare_avg
        town.town_culture = town_culture_avg
        town.town_facility = town_facility_avg
        town.town_citizen = town_citizen_avg
        
        town.save(update_fields=['star', 'area_welfare', 'town_welfare', 'town_culture', 'town_facility', 'town_citizen','update_at'])
    print('update town rank')

def start():
    scheduler=BackgroundScheduler()
    scheduler.add_job(
        update_town_rank,
        'interval',
        minutes = 3,
        id="crawler",
        misfire_grace_time=200,
        replace_existing=True,
    )
    try:
        logger.info("Starting scheduler...")
        scheduler.start()
        print(scheduler.get_jobs())
    except KeyboardInterrupt:
        logger.info("Stopping scheduler...")
        scheduler.shutdown()