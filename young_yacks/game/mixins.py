from weakref import WeakSet
from typing import ClassVar


class Queryable:
    """Adds a Class.all() method to get all in-memory instances of the class."""
    _instances: ClassVar = WeakSet()

    def __post_init__(self):
        self._instances.add(self)

    @classmethod
    def all(cls):
        return list(cls._instances)

    @classmethod
    def all_as_dict(cls, key):
        """Return a dict of all instances of the class, using key 'key'."""
        return {getattr(inst, key) for inst in cls._instances}
