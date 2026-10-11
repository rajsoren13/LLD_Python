
# violation DIP
class EmailService:
    def send_email(self, message):
        print(f"Sending email: {message}")


class Notification:
    def __init__(self):
        self.email_service = EmailService()

    def notify(self, message):
        self.email_service.send_email(message)


notification = Notification()
notification.notify("Your order has been shipped!")
