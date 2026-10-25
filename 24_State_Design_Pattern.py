class StoppedState:
    def play(self,player):
        print("Music Player")
        player.state=PlayingState()
    def pause(self, player):
        print("Cannot pause. Music is already stopped.")

    def stop(self, player):
        print("Music is already stopped.")
class PlayingState:
    def play(self,player):
         print("Music is already playing.")
    def pause(self, player):
        print("Music paused")
        player.state = PausedState()

    def stop(self, player):
        print("Music stopped")
        player.state = StoppedState()

class PausedState:
    def play(self, player):
        print("Music resumed")
        player.state = PlayingState()

    def pause(self, player):
        print("Music is already paused.")

    def stop(self, player):
        print("Music stopped")
        player.state = StoppedState()



class MusicPlayer:
    def __init__(self):
        self.state = StoppedState()

    def press_play(self):
        self.state.play(self)

    def press_pause(self):
        self.state.pause(self)

    def press_stop(self):
        self.state.stop(self)


player = MusicPlayer()

player.press_play()
player.press_pause()
player.press_play()
player.press_stop()
player.press_stop()