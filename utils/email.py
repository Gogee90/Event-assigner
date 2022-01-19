from django.core.mail import get_connection, EmailMessage
from django.http import JsonResponse


def send_email(sender, receiver, topic, message, file=None):
    try:
        connection = get_connection()
        connection.open()
        email = EmailMessage(f"{topic}", f"{message}.", f"{sender}", receiver)
        if file:
            email.attach_file(file.path)
        connection.send_messages([email])
    except Exception as e:
        return JsonResponse({"data": str(e)})
    finally:
        connection.close()
