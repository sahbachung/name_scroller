from model.sequence import Sequence
from model.process import Process
from controller.engine import SequenceEngine
from time import sleep


def main():

    e = SequenceEngine(10)
    e.load("./model/default.json")
    e.start(lambda: print(e.get_next().to_array()), daemon=False)


if __name__ == "__main__":
    main()