from enum import Enum
from time import sleep, strftime
from threading import Thread


class ProcessError(ValueError):
    pass


class ProcessState(Enum):

    STANDBY = -1
    INIT    = 0
    RUNNING = 1
    STOPPED = 2
    PAUSED  = 3

    def __str__(self):
        if self.value == 0:
            return "Process is Initializing"
        elif self.value == 1:
            return "Process is Running"
        elif self.value == 2:
            return "Process has been stopped"
        elif self.value == 3:
            return "Process has been paused"

    def can_resume(self) -> bool:
        if self.value != 3:
            raise ProcessError(self)
        else:
            return True


class Process(Thread):

    # last pid used (for autogen)
    LAST_PID = 0
    # process state, default is ProcessState.INIT
    state = ProcessState(0)

    # the command and params to be called
    process = None
    args = []
    kwargs = {}

    # update_rate is in milliseconds
    update_rate = 1000

    # time process was created
    created = "0:0:0"

    def __init__(self, command, args=[], kwargs={}, update_rate=-1, pid=None, daemon=True):
        if update_rate>0:
            self.set_update_rate(update_rate)
        if not pid:
            self.pid = Process.next_pid()
        else:
            self.pid = pid
            self.set_last_pid(pid)
        self.created = strftime("%H:%M:%S")
        self.process = command
        self.register(self.process, *args, **kwargs)
        super().__init__(target=self.run, args=args, kwargs=kwargs, daemon=daemon)
        self.set_state(1)

    def __repr__(self):
        return "<Process(pid=%d, STATE=%s (%s), created=%s)>" % \
               (self.pid, self.get_state().value, self.get_state().name, self.created)

    def get_state(self) -> ProcessState:
        return self.state

    def set_state(self, state: (ProcessState, int)):
        """state must be a ProcessState or a valid value of one"""
        if type(state) == ProcessState:
            self.state = state
        else:
            self.state = ProcessState(state)

    def stop(self):
        self.set_state(2)

    def pause(self, t=0):
        """pause for t milliseconds, or until resumed manually"""
        self.set_state(3)
        if t > 0:
            sleep(t / 1000)
            self.resume()

    def resume(self):
        s = self.get_state()
        if s.can_resume() is True:
            self.set_state(1)
        else:
            raise s.can_resume()

    def begin(self):
        """starts the process in a separate thread"""
        self.set_state(1)
        self.start()

    def run(self, debug=False) -> None:
        """attempts to run the process specified"""
        while 1:
            if self.get_state() == ProcessState(1):
                if debug:
                    print(str(self) + " is running " + str(self.process))

                if self.get_state() == ProcessState(2):
                    if debug:
                        print("Process has been stopped!")
                    self.stop()
                elif self.get_state() == ProcessState(3):
                    pass
                try:
                    self.process(*self.args, **self.kwargs)
                except Exception as e:
                    if debug:
                        print(e)
                    else:
                        raise e
                sleep(self.update_rate / 1000)

    def register(self, command, *args, **kwargs):
        """registers a command and parameters for this Process"""
        self.process = command
        self.args = args
        self.kwargs = kwargs

    def set_update_rate(self, m):
        """m is refresh rate in milliseconds"""
        self.update_rate = m

    @staticmethod
    def next_pid() -> int:
        Process.set_last_pid(Process.LAST_PID + 1)
        return Process.LAST_PID

    @staticmethod
    def set_last_pid(pid) -> None:
        Process.LAST_PID = pid


