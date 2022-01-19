from datetime import timedelta, datetime
from .models import Event, Request
from celery import shared_task
from utils.email import send_email


@shared_task
def create_reminder():
    for event in Event.objects.filter(
        event_date__gte=datetime.now() - timedelta(days=2),
    ):
        today = datetime.now().strftime("%Y-%m-%d")
        event_date = (event.event_date - timedelta(days=1)).strftime("%Y-%m-%d")
        if event_date == today:
            receivers = set(
                [
                    request.participant.email
                    for request in Request.objects.filter(event=event)
                ]
            )
            try:
                topic = "Напоминание"
                message = (
                    f"Напонминаем, что {event.event_date} стартует событие {event.name}"
                )
                send_email(
                    event.assigner.username,
                    receivers,
                    topic,
                    message,
                )
            except Exception as e:
                send_email(
                    event.assigner.username,
                    event.assigner.email,
                    "Ошибка",
                    f"Произошла ошибка при отправке сообщений! {str(e)}",
                )
