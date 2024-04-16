#!/usr/bin/python3
"""
Determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of list of int): A list of lists representing the
        boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if (len(boxes) == 0):
        return True

    visited = set()
    queue = set(boxes[0])

    while (len(queue)):
        visited = visited | queue
        queue = set()

        if (visited & set(range(1, len(boxes))) == set(range(1, len(boxes)))):
            return True

        for k in visited:
            if (k < len(boxes)):
                for new_key in boxes[k]:
                    if new_key not in visited:
                        queue.add(new_key)

    return False
