from django.apps import AppConfig


class TownConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'town'
    def ready(self):
        from . import signals  # 시그널 파일을 임포트합니다.
        signals.start()