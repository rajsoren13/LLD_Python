#demonstrates an LSP violation
class Worker:
    def work(self):
        raise NotImplementedError
    def eat(self):
        raise NotImplementedError
class HumanWorker(Worker):
    def work(self):
        print("Human i working")

    def eat(self):
        print("Human is eating")
class Robot(Worker):
    def work(self):
        print("Robot working")

    def eat(self):
        raise NotImplementedError("Robots don't eat")     # forced to write this


def WorkerAndRobot(wr:Worker):
    wr.work()
    wr.eat()


hw=HumanWorker()
rw=Robot()
WorkerAndRobot(hw)
try:
    WorkerAndRobot(rw)
except NotImplementedError as e:
    print(f"Error: {e}")

