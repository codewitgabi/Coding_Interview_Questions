#!/usr/bin/python


class BitArray:
    def __init__(self, size: int) -> None:
        self.__size = size
        self.__array = []

        # fill the array
        self.__fill()

    def __fill(self):
        """ Initializes the array with zeros """
        for i in range(self.__size):
            self.__array.append(0)

    @property
    def array(self):
        return self.__array
    
    @property
    def size(self):
        return self.__size

    def set(self, index: int, value: int):
        # validate data
        assert isinstance(index, int), f"Type of {index} cannot be used as an index value. Use int instead"
        assert value in [0, 1], "Value must be either 0 or 1."
        assert index < self.__size, "List index out of range"
        self.__array[index] = value

    def get(self, index: int) -> int:
        assert index < self.__size, "List index out of range"
        return self.__array[index]


bitarray = BitArray(6)
bitarray.set(5, 1)
print(bitarray.array)
print(bitarray.get(5))
