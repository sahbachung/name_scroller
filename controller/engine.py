from abc import ABC, abstractmethod
from json import load, dump, JSONDecodeError

from model.process import Process
from model.sequence import Sequence, Square


class Engine(ABC):

    CURR_POS = -1
    DISPLAY_LENGTH: int
    LENGTH: int
    HATS: list

    def __init__(self, length, display_length=8):
        self.LENGTH = length
        self.DISPLAY_LENGTH = display_length

    @abstractmethod
    def load(self, view) -> None: ...

    @abstractmethod
    def save(self, location) -> bool: ...

    @abstractmethod
    def save_as(self, location) -> bool: ...

    @abstractmethod
    def new(self) -> None: ...

    @abstractmethod
    def start(self, cmd=None, refresh_rate=1000, autostart=False, daemon=True) -> Process: ...

    @abstractmethod
    def get_next(self) -> Square: ...

    def increment(self) -> None:
        self.CURR_POS = (self.CURR_POS + 1) % self.LENGTH

    def get_next_pos(self) -> tuple:
        return self.CURR_POS, (self.CURR_POS + self.DISPLAY_LENGTH) % self.LENGTH


class SequenceEngine(Engine):

    def __init__(self, length=16):
        super().__init__(length=length)
        self._sequence = Sequence(length=length)

    def load(self, location) -> None:
        print("Loading")
        with open(location) as jsonfile:
            s = Sequence.from_json(load(jsonfile))
            self._sequence = s

    def save(self, location) -> bool:
        try:
            with open(location, "w") as jsonfile:
                dump(self._sequence.get_cols(), jsonfile)
        except FileNotFoundError:
            return self.save_as(location)
        except JSONDecodeError:
            return False
        return True

    def save_as(self, location) -> bool:
        try:
            with open(location, "x") as jsonfile:
                dump(self._sequence.get_cols(), jsonfile)
        except JSONDecodeError:
            return False
        return True

    def new(self) -> None:
        self._sequence = Sequence()

    def start(self, cmd=None, refresh_rate=1000, autostart=False, daemon=True) -> Process:
        if cmd:
            p = Process(cmd, refresh_rate=refresh_rate, daemon=daemon)
            return p
        else:
            p = Process(self.get_next, refresh_rate=refresh_rate, daemon=daemon)
            return p

    def get_next(self) -> Square:
        self.increment()
        return Square(
            [self._sequence[l] for l in SequenceEngine.resolve_range(*self.get_next_pos(), self.LENGTH)]
        )

    @staticmethod
    def resolve_range(first, final, length):
        assert all(type(i) == int for i in (first, final))
        length = length
        if not first < length:
            first = first % length
        if not final < length:
            final = final % length
        if first <= final:
            for i in range(first, final):
                yield i
        else:
            for i in (*list(range(first, length)), *list(range(0, final))):
                yield i
