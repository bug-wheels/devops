import zmail

from .settings import NOTIFICATION_MAIL


def send_mail(recipients, message):
    server = zmail.server(NOTIFICATION_MAIL['USER_NAME'], NOTIFICATION_MAIL['PASSWORD'])
    server.send_mail(recipients, message)
