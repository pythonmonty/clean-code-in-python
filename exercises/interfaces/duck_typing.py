"""An example for duck typing in Python. The type of the object is determined by the methods it implements."""

class Artist:
    """Artist implementation."""

    def draw(self) -> None:
        """Draw a painting."""
        print("Draw a painting.")


class Lottery:
    """Lottery implementation."""

    def draw(self) -> None:
        """Draw a lottery."""
        print("Draw lottery numbers.")


def draw_a_painting(painter: Artist):
    """Draw a painting.

    This function purposefully has no type hints.
    The type of `painter` is irrelevant, as long as it has a method `draw()`.
    """
    painter.draw()


if __name__ == "__main__":
    artist = Artist()
    # This runs:
    draw_a_painting(artist)

    lottery = Lottery()
    # This runs too:
    draw_a_painting(lottery)

    print(f"Is object artist of type Lottery? {isinstance(artist, Lottery)}")
    print(f"Is object lottery of type Artist?  {isinstance(lottery, Artist)}")
