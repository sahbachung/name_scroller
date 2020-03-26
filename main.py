from model.sequence import Sequence
from model.process import Process
from controller.engine import SequenceEngine
from time import sleep


def main():
    # s = Sequence(10)
    # print(s)
    # s.add_column([1, 2, 3, 4, 5])
    # print(s)
    # s.set_xy(3, 2, True)
    # print(s)

    # scr = Process(lambda x,y: print(x*y), [4, 3], pid=1)
    # i = input("\nseconds?: ")
    # i = int(i)
    # scr.start()
    # sleep(i)
    # scr.pause()
    # print("Paused")
    # i = input("\nseconds?: ")
    # i = int(i)
    # scr.resume()
    # sleep(i)
    # scr.pause()
    # print("Paused")
    # input()

    e = SequenceEngine(10)
    e.load("./model/default.json")
    # p = Process((lambda: print(e.get_next())))
    p = e.start(lambda: print(e.get_next().to_array()), daemon=False)
    p.begin()


if __name__ == "__main__":
    main()