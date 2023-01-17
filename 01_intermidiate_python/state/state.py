from manager import ObjectManager


class State:
    def __init__(self):
        self.object_manager = ObjectManager()

    def tick(self):
        self.object_manager.tick()

    def render(self):
        self.object_manager.render()
