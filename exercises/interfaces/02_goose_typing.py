"""Example for goose typing in Python.

Implementation of a classical French card deck. The card deck has cards numbered from 1 to 10 and four additional
cards (jack, queen, kind, ace). The number corresponds to the card rank.
The card deck has four suits: clubs, spades, diamonds and hearts.

We use the ABC MutableSequence as interface and need to implement the following methods:
__getitem__, __setitem__, __delitem__, __len__, insert
"""

from collections import abc
from typing import Any, NamedTuple


class Card(NamedTuple):
    """A single French Deck card."""

    rank: str
    suit: str

# For virtual subsclassing use the 'register' decorator and class signature without inheritance
#@abc.MutableSequence.register
#class CardDeck:
class CardDeck(abc.MutableSequence):
    """A French Deck card sequence."""

    ranks = [str(rank) for rank in range(2, 11)] + list("JQKA")
    suits = ["clubs", "spades", "diamonds", "hearts"]

    def __init__(self) -> None:
        """Instantiate a French Deck."""
        self._cards = [Card(rank, suit) for rank in self.ranks
                       for suit in self.suits]

    def __getitem__(self, position) -> Any:
        """Return the position of a card."""
        return self._cards[position]

    def __setitem__(self, position, value) -> None:
        """Set the position of a card.

        All we need to enable shuffling.
        """
        self._cards[position] = value

    def __len__(self) -> int:
        """Calculate the length of the French Deck."""
        return len(self._cards)

    def __delitem__(self, position) -> None:
        """Delete a card from the French Deck."""
        del self._cards[position]

    def insert(self, position: int, value: Card):
        """Insert a new card into the French Deck."""
        self._cards.insert(position, value)


if __name__ == "__main__":
    card_deck = CardDeck()
    print(isinstance(card_deck, abc.MutableSequence))
    print(issubclass(CardDeck, abc.MutableSequence))
