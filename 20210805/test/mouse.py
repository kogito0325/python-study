from handler import Handler


class Mouse(Handler):
    def handle(self, event):
        print(f'{event} handled')
