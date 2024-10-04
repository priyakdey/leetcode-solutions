"""
1146. Snapshot Array

Implement a SnapshotArray that supports the following interface:

- SnapshotArray(int length) initializes an array-like data structure with the
  given length. Initially, each element equals 0.
- void set(index, val) sets the element at the given index to be equal to val.
- int snap() takes a snapshot of the array and returns the snap_id: the total
  number of times we called snap() minus 1.
- int get(index, snap_id) returns the value at the given index, at the time
  we took the snapshot with the given snap_id
"""

from typing import List


class SnapshotArray:

    def __init__(self, length: int):
        self.snaps: List[List[int]] = [[0] for _ in range(length)]
        self.snap_id = -1

    def set(self, index: int, val: int) -> None:
        self.snaps[index][-1] = val

    def snap(self) -> int:
        for snap in self.snaps:
            snap.append(snap[-1])
        self.snap_id += 1
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        return self.snaps[index][snap_id]
