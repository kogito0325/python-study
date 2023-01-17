def run_n_times(function, times: int = 1) -> None:
    for _ in range(times):
        function()


run_n_times(lambda: print('Hello, world!'), 10)
