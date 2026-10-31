from dataclasses import dataclass

class ValidString:
    """Descriptor"""

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, obj, obj_type=None):
        if obj is None:
            return self
        return obj.__dict__[self._name]

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError(f'{self._name} must be a string')

        elif not value.strip():
            raise ValueError(f'{self._name} must not be an empty string')

        elif not any(c.isalpha() for c in value):
            raise ValueError(f'{self._name} must contain only letters, numbers, and  characters')

        else:
            obj.__dict__[self._name] = value

@dataclass
class Card:
    """Class a card object"""
    rus: str = ValidString()
    eng: str = ValidString()
    category: str = ValidString()
    level: float = 1.0

    def __str__(self):
        return f'{self.rus}:{self.eng}'

    def __repr__(self):
        return f'Card(rus = {self.rus}, eng = {self.eng}, category = {self.category}, level = {self.level})'

















