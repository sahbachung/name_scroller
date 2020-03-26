from controller.engine import Engine, SequenceEngine
try:
    from sense_hat import SenseHat
except ImportError:
    from model.dummy_hat import SenseHat


class Controller:

    CURR_PROCESS = None

    def __init__(self, engine: Engine, hat: SenseHat):
        self.hat = hat
        self.engine = engine
        self.start()

    def start(self):
        self.CURR_PROCESS = self.engine.start(
            cmd=(lambda: self.hat.set_pixels(self.engine.get_next().to_array(attr="get_val"))),
            daemon=False
        )
        self.CURR_PROCESS.begin()


def main():
    engine = SequenceEngine()
    engine.load("../model/default.json")
    hat = SenseHat()
    controller = Controller(engine, hat)
    controller.start()


if __name__ == "__main__":
    main()