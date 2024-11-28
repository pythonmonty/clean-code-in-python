"""Exercise 01_process_user_data.py - Refactored."""
from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    """Class that holds user information."""

    first_name: str
    last_name: str
    is_active: bool
    date_of_birth: date

    # You could think about removing the generate_capitalized_user_full_name function and capitalizing the
    # first_name and last_name directly in the __post_init__ method.
    # def __post_init__(self):
    #     """Capitalizes the first and last name of a user instance."""
    #     self.first_name = self.first_name.capitalize()
    #     self.last_name = self.last_name.capitalize()


class UserNotActiveError(Exception):
    """User is not active Exception."""

    def __init__(self, user: User):
        """Instantiate the UserNotActiveException class."""
        super().__init__(f"User {user} is not active.")


def format_active_user_information_as_string(user: User) -> str:
    """Format active user information and return as string."""
    check_is_user_active(user)

    full_name = generate_capitalized_user_full_name(user)

    age = calculate_user_age(user.date_of_birth)

    user_information = generate_user_string_representation(full_name, age, "Active")

    return user_information


def check_is_user_active(user: User) -> None:
    """Check if user is active."""
    if not user.is_active:
        raise UserNotActiveError(user)


def generate_capitalized_user_full_name(user: User) -> str:
    """Capitalize the first and last name of a user instance and returns the full name."""
    first_name = user.first_name.capitalize()
    last_name = user.last_name.capitalize()
    return f"{last_name}, {first_name}"


def calculate_user_age(birth_date: date) -> int:
    """Calculate age given a birthday date, respective to today's date."""
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


def generate_user_string_representation(full_name: str, age: int, status: str) -> str:
    """Generate string representation of user information."""
    user_information = str({
        "name": full_name,
        "age": age,
        "status": status,
        })
    return user_information


if __name__ == "__main__":
    user_john = User("john", "doe", True, date(1990, 12, 12))
    processed_user_data = format_active_user_information_as_string(user_john)
    print(processed_user_data)
