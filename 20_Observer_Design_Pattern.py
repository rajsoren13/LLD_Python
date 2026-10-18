class Subscriber:
    def __init__(self,name):
        self.name=name
        
    def notify(self,video):
        print(f"{video} uploaded and {self.name} received notification")

class YouTubeChannel:
    def __init__(self):
        self.listofsubscriber=[]
        self.listofunsubscriber=[]

    def subscribe(self,subscribername):
        self.listofsubscriber.append(subscribername)

    def unsubscribe(self,subscribername):
            #self.listofunsubscriber.append(subscribername)
            if subscribername in self.listofsubscriber:
                self.listofsubscriber.remove(subscribername)
                print(f"{subscribername.name} has un-subscribed")
            else:
                print(f"{subscribername.name} is not subscribed")
           

    def upload_video(self, video):
        print(f"\nNew video uploaded: {video}")
        for sub in self.listofsubscriber:
            sub.notify(video)
        for unsub in self.listofunsubscriber:
            self.listofunsubscriber.remove()

# Create the channel
channel = YouTubeChannel()

# Create subscribers
alice_obj = Subscriber("Alice")
bob_obj = Subscriber("Bob")
charlie_obj = Subscriber("Charlie")
raj_obj = Subscriber("Raj")

# Subscribe them to the channel
channel.subscribe(alice_obj)
channel.subscribe(bob_obj)
channel.subscribe(charlie_obj)
#unsubscribe
channel.unsubscribe(raj_obj)
channel.unsubscribe(charlie_obj)

# Upload a video
channel.upload_video("Python Tutorial")
