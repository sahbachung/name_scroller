from model.values import RGBValue


class Sequence:

    _cols: list = []

    def __init__(self, length=8, data: list = None, json=False):
        self.__height = 8
        if data is None or not all(len(x) == 8 for x in data):
            self.__length = length
            self._cols = [
                [RGBValue(), RGBValue(), RGBValue(), RGBValue(), RGBValue(), RGBValue(), RGBValue(), RGBValue()] for _
                in range(length)]
        elif json:
            print("ELSE BLOCK")
            print("DATA",data)
            for i, col in enumerate(data):
                self._cols.append([])
                for v in col:
                    self._cols[i].append(RGBValue(r=v[0], g=v[1], b=v[2]))
            self.__length = len(data)
        else:
            self._cols = data
            self.__length = length

    def __len__(self):
        return self.__length

    def set_length(self, length: int) -> None:
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
        self.set_length(len(self) + 1)

    def remove_column(self, index=-1) -> bool:
        try:
            self._cols.pop(index=index)
            self.set_length(len(self) - 1)
            return True
        except IndexError:
            return False

    def set_sequence(self, data) -> bool:
        if all(len(x) == 8 for x in data):
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
            return self._cols[item]
        else:
            return self._cols[item % len(self._cols)]

    def __setitem__(self, key, value):
        self._cols[key % len(self._cols)] = value

    def get_cols(self):
        return self._cols

    def get_rows(self):
        rows = []
        for row in zip(*self._cols):
            rows.append(row)
        return rows

    @classmethod
    def from_json(cls, data):
        """returns a Sequence generated from a json structured array"""
        def _r_g_b(t):
            assert type(t) in (list, tuple)
            assert len(t) == 3
            return {"r": t[0], "g": t[1], "b": t[2]}
        s = cls(length=len(data))
        for c_i, column in enumerate(data):
            col = []
            for v in column:
                col.append(RGBValue(**_r_g_b(v)))
            s.set_col(c_i, col)
        return s


class Square(Sequence):

    def __init__(self, data=None):
        if data:
            assert len(data) == 8
            assert all(len(c) == 8 for c in data)
        super().__init__(length=8, data=data)

    def to_array(self, cmd=None, attr=None) -> []:
        assert not (cmd and attr)
        if cmd:
            return [cmd(cell) for cell in self._cell_gen()]
        elif attr:
            return [getattr(cell, attr)() for cell in self._cell_gen()]
        else:
            return [cell for cell in self._cell_gen()]

    def _cell_gen(self):
        for col in self.get_rows():
            for cell in col:
                yield cell
