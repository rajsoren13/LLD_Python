class UserValidator:
    def validate(self, email):
        if not email or "@" not in email:
            raise ValueError("Invalid email address")


class UserRepository:
    def save(self, username):
        print(f"[DB] Saving user {username} to database")


class EmailService:
    def send(self, email):
        print(f"Sending details to {email}")


class UserManager:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def register_user(self):
        validator = UserValidator()
        repository = UserRepository()
        email_service = EmailService()

        validator.validate(self.email)
        repository.save(self.username)
        email_service.send(self.email)


# Create UserManager
user_mgr = UserManager("alice_dev", "alice@example.com")

# Register user
user_mgr.register_user()