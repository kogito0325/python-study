# lambda 식

def run(function, times):
    for _ in range(times):
        function()


run(lambda: print('Hello, world'), 10)
