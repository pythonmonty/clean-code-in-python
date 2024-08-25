"""Exercise - Liskov Substitution Principle and Dependency Inversion Principle.

Make sure you take the following aspects into consideration:
    - Does the current implementation violate the Dependency Inversion Principle?
        - If yes how would you change the Ellipse / Circle implementation to comply with the principle?
    - Does the current implementation violate the Liskov Substitution Principle?
        - If yes how would you change the Ellipse / Circle implementation to comply with the principle?

Function `double_ellipse_semi_major_axis` is a user implementation. If you modify it, think about the implications
that your modification might have for the user.
"""

import math


class Ellipse:
    """Ellipse in Cartesian coordinates."""

    def __init__(self, semi_major_axis: float, semi_minor_axis: float):
        """Initialize Ellipse instance by passing the semi axes."""
        self._semi_major_axis = semi_major_axis
        self._semi_minor_axis = semi_minor_axis

    def __repr__(self) -> str:
        """Create the string representation of an Ellipse instance."""
        return (f"{self.__class__.__name__}(semi-major-axis: {self._semi_major_axis}, "
                f"semi-minor-axis: {self._semi_minor_axis})")

    @property
    def semi_major_axis(self) -> float:
        """Semi major axis property method."""
        return self._semi_major_axis

    @property
    def semi_minor_axis(self) -> float:
        """Semi minor axis property method."""
        return self._semi_minor_axis

    @property
    def area(self) -> float:
        """Calculates the Ellipse area as property."""
        area = math.pi * self._semi_major_axis * self._semi_minor_axis
        return area

    def set_semi_major_axis(self, semi_major_axis: float) -> None:
        """Set semi major axis to a new value."""
        self._semi_major_axis = semi_major_axis

    def set_semi_minor_axis(self, semi_minor_axis: float) -> None:
        """Set semi minor axis to a new value."""
        self._semi_minor_axis = semi_minor_axis


class Circle(Ellipse):
    """Circle as a special case of the Ellipse."""

    def __init__(self, radius: float):
        """Initialize the Circle instance given a radius."""
        super().__init__(radius, radius)


def double_ellipse_semi_major_axis(ellipse: Ellipse) -> None:
    """Change the semi major axis of an Ellipse instance by doubling the value.

    This function is a user implementation that uses the Ellipse / Circle classes.
    """
    ellipse.set_semi_major_axis(ellipse.semi_major_axis * 2)


if __name__ == "__main__":
    semi_major_ax = 3
    semi_minor_ax = 2

    # Does the user code work with Ellipse?
    e = Ellipse(semi_major_ax, semi_minor_ax)
    print(e)
    print(f"Ellipse area: {e.area}")
    double_ellipse_semi_major_axis(e)
    print(e)
    print(f"Ellipse area: {e.area}")
    print(f"Is ellipse? {isinstance(e, Ellipse)}")

    # Does it work with the Ellipse subclass Circle?
    radius = 3
    c = Circle(radius)
    print(c)
    print(f"Circle area: {c.area}")
    double_ellipse_semi_major_axis(c)
    print(c)
    print(f"Circle area: {c.area}")
    print(f"Is circle? {isinstance(c, Circle)}")
