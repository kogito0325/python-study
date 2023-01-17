class ObjectManager:
    def __init__(self):
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)
        return self

    def remove(self, obj):
        self.objects.remove(obj)
        return self

    def tick(self):
        for obj in self.objects:
            obj.tick()

    def render(self):
        for obj in self.objects:
            obj.render()
