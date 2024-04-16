#!/usr/bin/python3
"""
Determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of list of int): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    # Initialize a set to keep track of visited boxes
    visited = set()

    # Initialize a queue with the first box (index 0)
    queue = [0]

    # Start BFS traversal
    while queue:
        current_box = queue.pop(0)
        visited.add(current_box)

        # Check keys in the current box
        for key in boxes[current_box]:
            # If the key opens a new box and it hasn't been visited yet, add it to the queue
            if key < len(boxes) and key not in visited:
                queue.append(key)

    # If all boxes have been visited, return True
    return len(visited) == len(boxes)


if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # False
