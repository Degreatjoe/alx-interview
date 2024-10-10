#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    the can unlock function checks if
    boxes can be unlocked
    """
    unlocked = [False] * len(boxes)  # Track unlocked boxes
    unlocked[0] = True  # First box is unlocked by default
    keys = [0]  # Start with the first box's keys
    
    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if 0 <= key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)
    
    return all(unlocked)
