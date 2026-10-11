#demonstrates a Fixed LSP violation
class workable:
    def work(self):
        raise NotImplementedError
class eatable:
    def eat(self):
        raise NotImplementedError
    
class HumanWorker(workable,eatable):
    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")
class Robot(workable):
    def work(self):
        print("Robot working")


def make_work(wr:workable):
    wr.work()
def make_eat(wr:eatable):
    wr.eat()


hw=HumanWorker()
rw=Robot()
make_work(hw)
make_eat(hw)

make_work(rw)
