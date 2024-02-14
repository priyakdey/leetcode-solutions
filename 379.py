"""
379. Design Phone Directory

Design a phone directory that initially has maxNumbers empty slots that can 
store numbers. 
The directory should store numbers, check if a certain slot is empty or not, and empty a given slot.

Implement the PhoneDirectory class:
- PhoneDirectory(int maxNumbers) Initializes the phone directory with the number of available slots maxNumbers.
- int get() Provides a number that is not assigned to anyone. Returns -1 if no number is available.
- bool check(int number) Returns true if the slot number is available and false otherwise.
- void release(int number) Recycles or releases the slot number.

"""


from typing import Set


class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        self.slots: Set[int] = set([i for i in range(maxNumbers)])

    def get(self) -> int:
        if len(self.slots) == 0:
            return -1
        return self.slots.pop()

    def check(self, number: int) -> bool:
        return number in self.slots

    def release(self, number: int) -> None:
        self.slots.add(number)
