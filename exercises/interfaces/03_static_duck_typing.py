"""Example for static duck typing in Python. An external static type checker is required."""

import random
from typing import Any, Iterable, Protocol, runtime_checkable


@runtime_checkable
class RandomPicker(Protocol):
    """Random Picker Interface."""

    def pick(self) -> Any:
        """Pick at random."""
        pass


class SimplePicker:
    """A simple random picker."""

    def __init__(self, items: Iterable) -> None:
        """Instantiate a simple picker."""
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self) -> Iterable:
        """Pick an element."""
        return self._items.pop()


if __name__ == "__main__":
    simple_picker = SimplePicker(items=[1, 5, 7, 20])
    print(isinstance(simple_picker, RandomPicker))
    print(issubclass(SimplePicker, RandomPicker))
