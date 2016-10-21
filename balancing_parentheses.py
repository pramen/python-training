#!/usr/bin/env python2.7

def is_balanced(source, caps):
    """Check string for containing balanced parenthises.

    All that is open is then closed,
    and nothing is closed which is not already open!

    Will be given a string to validate, and a second string,
    where each pair of characters defines an opening and closing sequence that needs balancing.

    Assume that the second string always has an even number of characters.

    In this case '(' opens a section, and ')' closes a section:
    >>> is_balanced("(Sensei says yes!)", "()")
    True
    >>> is_balanced("(Sensei says no!", "()")
    False

    In this case '(' and '[' open a section, while ')' and ']' close a section:
    >>> is_balanced("(Sensei [says] yes!)", "()[]")
    True
    >>> is_balanced("(Sensei [says) no!]", "()[]")
    False

    In this case a single quote (') both opens and closes a section:
    >>> is_balanced("Sensei says 'yes'!", "''")
    True
    >>> is_balanced("Sensei say's no!", "''")
    False
    
    In this case a dash (-) both opens and closes a section:
    >>> is_balanced("Sensei says -yes-!", "--")
    True
    >>> is_balanced("Sensei -says no!", "--")
    False

    Should it be True for strings contain scheme below?
    >>> is_balanced("(Sensei (says)) no!", "()")
    True
    >>> is_balanced("(Sensei) (says) no!", "()")
    True
    >>> is_balanced("(Sensei) [says] no!", "()[]")
    True

    Too many closes:
    >>> is_balanced("(Sensei says))) no!", "()")
    False
    >>> is_balanced("(Sensei says)) no!", "()")
    False

    >>> is_balanced("'//'", "''//")
    True
    >>> is_balanced("'/'/", "''//")
    False
    >>> is_balanced("))]]", "()[]")
    False
    >>> is_balanced("(([[", "()[]")
    False
    >>> is_balanced(")])]", "()[]")
    False
    >>> is_balanced(")(", "()")
    False
    """

    data = filter(lambda c: c in caps, source)

    # Optimization (optional - all works without it)
    if len(data) % 2 != 0:
        return False

    opens_closes = {o: c for o, c in zip(caps[::2], caps[1::2])}

    unclosed = []

    for c in data:

        # open == close
        if c == opens_closes.get(c):

            if not unclosed:
                unclosed.append(c)
            elif unclosed and unclosed[-1] != c:
                unclosed.append(c)
            elif unclosed and unclosed[-1] == c:
                unclosed.pop()
            else:
                raise 'Unexpected'

        else:

            if c in opens_closes:
                unclosed.append(c)
            elif c in opens_closes.values():
                if not unclosed:
                    return False
                elif not c == opens_closes[unclosed[-1]]:
                    return False
                elif c == opens_closes[unclosed[-1]]:
                    unclosed.pop()
                else:
                    raise 'Unexpected'
            else:
                raise 'Unexpected'

    if unclosed:
        return False
    else:
        return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
