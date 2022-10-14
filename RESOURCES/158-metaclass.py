from time import perf_counter


class LoadTimeMeta(type):
    base_time = perf_counter()

    def __new__(mcls, name, bases, body):
        body["load_time"] = mcls.base_time - perf_counter()

        return super().__new__(
            mcls, name, bases, body
        )


# Usage
class Sample(metaclass=LoadTimeMeta):
    pass