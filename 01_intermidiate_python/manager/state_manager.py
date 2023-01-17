class StateManager:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state
        return self

    def tick(self):
        if self.state is not None:
            self.state.tick()

    def render(self):
        if self.state is not None:
            self.state.render()
