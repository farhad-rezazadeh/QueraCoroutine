import time
import random
from typing import Iterable, Generator, List, Any


def wait(tasks: Iterable[Generator]) -> List[Any]:
    pending = list(tasks)
    tasks = {task: None for task in pending}
    before = time.time()

    while pending:
        for gen in pending:
            try:
                tasks[gen] = gen.send(tasks[gen])
            except StopIteration as e:
                tasks[gen] = e.value
                pending.remove(gen)

    print(f"duration: {time.time() - before:.3}")
    return list(tasks.values())


def sleep(duration: float) -> None:
    now = time.time()
    threshold = now + duration
    while now < threshold:
        yield
        now = time.time()


def sleep_sort(numbers: List[int]) -> List[int]:
    result = []

    def sleep_add(number: int) -> Generator:
        yield from sleep(number)
        result.append(number)

    wait([sleep_add(number) for number in numbers])
    return result


if __name__ == "__main__":
    range_10 = list(range(10))
    random.shuffle(range_10)
    print(f"range_10: {range_10}")
    print(f"sleep_sort(range_10): {sleep_sort(range_10)}")
