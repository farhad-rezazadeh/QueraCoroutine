import asyncio
import random
from typing import List, Coroutine


def sleep_sort(numbers: List[int]) -> List[int]:
    result = []

    async def sleep_add(number: int) -> Coroutine:
        await asyncio.sleep(number)
        result.append(number)

    asyncio.run(asyncio.wait([sleep_add(number) for number in numbers]))
    return result


if __name__ == "__main__":
    range_10 = list(range(10))
    random.shuffle(range_10)
    print(f"range_10: {range_10}")
    print(f"sleep_sort(range_10): {sleep_sort(range_10)}")
