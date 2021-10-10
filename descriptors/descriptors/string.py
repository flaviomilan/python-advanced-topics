from weakref import WeakKeyDictionary


class LowerCase:

    def __init__(self) -> None:
        self._instance_data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self._instance_data[instance]

    def __set__(self, instance, value):
        self._instance_data[instance] = str(value).lower()

    def __delete__(self, instance):
        self._instance_data.pop(instance)


class UpperCase:
    def __init__(self) -> None:
        self._instance_data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self._instance_data[instance]

    def __set__(self, instance, value):
        self._instance_data[instance] = str(value).upper()

    def __delete__(self, instance):
        self._instance_data.pop(instance)