from weakref import WeakKeyDictionary


class Positive:

    def __init__(self) -> None:
        self._instance_data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self._instance_data[instance]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"Value {value} is not positive")
        self._instance_data[instance] = value

    def __delete__(self, instance):
        self._instance_data.pop(instance)
        

class Negative:

    def __init__(self) -> None:
        self._instance_data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self._instance_data[instance]

    def __set__(self, instance, value):
        if value >= 0:
            raise ValueError(f"Value {value} is not negative")
        self._instance_data[instance] = value

    def __delete__(self, instance):
        self._instance_data.pop(instance)
