"""Exercise - One level of abstraction per function.

Focus on the function `process_user_data` and refactor it. (However, feel free to refactor other functions
if you find it necessary).

Make sure you take the following aspects into consideration:
    - Does the naming of variables and functions reveal their intention? Do they contain any noise words?
    - Do the functions do only one thing?
    - Level of abstractions in the function(s).
    - Are the functions ordered according to the decreasing level of abstraction (stepdown rule)?
"""

from datetime import date


class User:
    """Class that holds user information."""

    def __init__(
            self,
            first_name: str,
            last_name: str,
            is_active: bool,
            date_of_birth: str | None,
    ):
        """Initialize a User instance.

        :param first_name: First name of user.
        :param last_name: Last name of user.
        :param is_active: Equals to True if user is active.
        :param date_of_birth: User's date of birth.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = is_active
        self.date_of_birth = date_of_birth

    def __repr__(self) -> str:
        """Create custom representation of User class."""
        return f"User({str(self.__dict__)})"


def process_user_data(user: User) -> str:
    """Process user data."""
    validate_user_data(user)

    full_name = (f"{user.first_name.capitalize()} "
                 f"{user.last_name.capitalize()}")

    if not is_user_active(user):
        return f"User {full_name} is not active."

    dob = user.date_of_birth
    birth_day, birth_month, birth_year = map(int, dob.split("."))
    age = calculate_age(birth_day, birth_month, birth_year)

    return str({
        "name": full_name,
        "age": age,
        "status": "Active"
    })


def validate_user_data(user: User) -> None:
    """Check if user instance has birth of date set."""
    if user.date_of_birth is None:
        raise ValueError(f"Date of birth for {user} is not filled.")


def is_user_active(user: User) -> bool:
    """Check if user is active."""
    if user.is_active:
        return True
    else:
        return False


def calculate_age(birth_day: int, birth_month: int, birth_year: int) -> int:
    """Calculate age given a birthday day, month and year, respective to today's date."""
    today = date.today()
    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
    return age


if __name__ == "__main__":
    user_john = User("john", "doe", True, "12.12.1990")
    processed_user_john = process_user_data(user_john)
    print(processed_user_john)
