from model.sequence import Sequence


def main():
    s = Sequence(10)
    print(s)
    s.add_column([1, 2, 3, 4, 5])
    print(s)
    s.set_xy(3, 2, True)
    print(s)


if __name__ == "__main__":
    main()