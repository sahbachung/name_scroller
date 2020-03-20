from abc import ABC, abstractmethod
from model.process import Process
from model.sequence import Sequence, Square


class Engine(ABC):

    CURR_POS = 0

    def __init__(self):
        pass

    @abstractmethod
    def load(self, view) -> None: ...

    @abstractmethod
    def save(self, location) -> bool: ...

    @abstractmethod
    def new(self) -> None: ...

    @abstractmethod
    def start(self) -> Process: ...

    def get_curr_pos(self) -> int:
        return self.CURR_POS

    def update_curr_pos(self, i) -> None:
        self.CURR_POS = i

    def next_curr_pos(self) -> int:
        self.CURR_POS += 1
        return self.CURR_POS - 1


class SequenceEngine(Engine):

    def __init__(self):
        super().__init__()
        self._sequence = Sequence(data=[
            [True, False, True, True, False],
            [False, False, False, True, False],
            [True, False, True, False, True],
            [True, True, True, True, False],
            [True, False, True, False, False],
            [False, False, True, False, False],
            [True, False, False, False, True],
            [False, False, True, False, False]])

    def load(self, view) -> None:
        pass

    def save(self, location) -> bool:
        pass

    def new(self) -> None:
        pass

    def start(self) -> Process:
        pass

    def get_next(self) -> Square:
        return Square(
            [self._sequence[l] for l in range(self.get_curr_pos(), self.next_curr_pos() + 5)]
        )


if __name__ == "__main__":
    e = SequenceEngine()
    while 1:
        print(e.get_next())
        print("\n")