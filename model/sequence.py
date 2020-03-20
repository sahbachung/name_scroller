

class Sequence:

    def __init__(self, length=5, data=[]):
        self.__height = 5
        if not all(len(x)==5 for x in data):
            self._cols = [[False, False, False, False, False] for _ in range(length)]
            self.__length = length
        else:
            self._cols = data
            self.__length = len(data)

    def __len__(self):
        return self.__length

    def set_length(self, length:int) -> None:
        self.__length = length

    def get_height(self):
        return self.__height

    def __str__(self):
        s = "\t" + "%s\t" * len(self) + "\n"
        ordered = (l for l in zip(*self._cols))
        string = ""
        for r in ordered:
            string += s % r
        return string

    def add_column(self, data, index=-1):
        assert type(data) == list and len(data) == self.get_height()
        if index == -1:
            self._cols.append(data)
        else:
            self._cols.insert(index, data)
        self.set_length(len(self)+1)

    def remove_column(self, index=-1) -> bool:
        try:
            self._cols.pop(index=index)
            self.set_length(len(self)-1)
            return True
        except IndexError:
            return False

    def set_sequence(self, data) -> bool:
        if all(len(x) == 5 for x in data):
            self._cols = data
            self.set_length(len(data))
            return True
        return False

    def set_xy(self, x, y, value) -> bool:
        """set the value `x` units right and `y` down from the top right corner"""
        try:
            self._cols[x][y] = value
            return True
        except IndexError:
            return False

    def set_col(self, index, data):
        try:
            self._cols[index] = data
            return True
        except IndexError:
            return False

    def set_row(self, index, data) -> bool:
        assert len(self) == len(data)
        try:
            for col, val in zip(self._cols, data):
                col[index] = val
            return True
        except Exception:
            return False

    def __getitem__(self, item):
        if type(item) == slice:
            raise NotImplementedError
        elif item == 0:
            print(self._cols)
            return self._cols[item]
        else:
            return self._cols[item % len(self._cols)]

    def __setitem__(self, key, value):
        self._cols[key % len(self._cols)] = value


class Square(Sequence):

    def __init__(self, data=[]):
        super().__init__(length=5, data=data)
