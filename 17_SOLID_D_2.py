
class NotificationService:
    def send(self, message):
        raise NotImplementedError

class EmailService(NotificationService):
    def send(self, message):
        print(f"Sending email: {message}")


class SMSService(NotificationService):
    def send(self, message):
        print(f"Sending SMS: {message}")

class Notification:
    def __init__(self, service: NotificationService):
        self.service = service

    def notify(self, message):
        self.service.send(message)

# Use email
email = EmailService()
notification = Notification(email)
notification.notify("Your order has been shipped!")

# Use SMS
sms = SMSService()
notification = Notification(sms)
notification.notify("Your order has been shipped!")
