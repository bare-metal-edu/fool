import time
import random
import threading
from typing import Any, Callable

class Pin:

    IN = 0
    OUT = 1
    PULL_UP = 1
    PULL_DOWN = 0

    def __init__(self, id: Any, mode: Any = IN, *args, **kwargs):
        self.id = id
        self.mode = mode
        self.level = 0

    def value(self, val: Any) -> int:
        if val:
            self.level = val
        return self.level

    def on(self):
        self.level = 1

    def off(self):
        self.level = 0

    def toggle(self):
        if self.level == 0:
            self.on()
        else:
            self.off()

    def irq(self,
        handler: Callable,
        trigger: Callable,
        priority: int = 1,
        wake: Any = None,
        hard: bool = False
    ):
        pass

    def low(self):
        self.off()

    def high(self):
        self.on()

class Timer:

    def __init__(self, **kwargs):
        self.caller = lambda *args: None
        self.process = threading.Thread(target = self.__create_timer)
        self.process.start()

    def __create_timer(self):
        while True:
            self.caller(self)
            time.sleep(1)

    def callback(self, func: Callable):
        self.caller = func

