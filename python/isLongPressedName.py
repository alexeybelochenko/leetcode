# Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

# You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

def isLongPressedName(name, typed):
    i = j = 0
    
    while i < len(name) and j < len(typed):
        if name[i] == typed[j]:
            i += 1
            j += 1
        else:
            if typed[j] != typed[j - 1] or j == 0:
                return False
            else:
                j += 1
    
    return i == len(name)