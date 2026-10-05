#defiing the class of instragram(template for intagram user)
class User:
    def __init__(self,username,bio,profilepicture):
        self.username=username
        self.bio=bio
        self.profilepicture=profilepicture
    #Method:every user can perform
    def follow(self,another_user):
        return f"{self.username} followed {another_user.username}"
    #creating object(individual User)
usr1=User("Raj","Love Coding","raj.png")
usr2=User("Tara","coffy Lover","Tara.png")

    #accessing attribute
print(usr1.username)
print(usr2.bio)

    #calling method
result=usr1.follow(usr2)
print(result)
    