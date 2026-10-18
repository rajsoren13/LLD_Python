
class Email:
    def send(self):
        print("Sending Email")


class SMS:
    def send(self):
        print("Sending SMS")


# Factory
class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == "email":
            return Email()
        elif notification_type == "sms":
            return SMS()
        else:
            raise ValueError("Invalid notification type")


# Application code
notification = NotificationFactory.create_notification("email")
notification.send()

notification = NotificationFactory.create_notification("sms")
notification.send()
