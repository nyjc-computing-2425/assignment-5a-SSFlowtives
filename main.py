def to_hms(seconds: int) -> list:
    """
    Converts seconds to hours, minutes, and seconds, and returns it as a list.

    Parameters
    ---------
    seconds: int
        the seconds to be calculated

    Returns
    ---------
    list
        a list of integers representing hours, minutes, seconds

    Example:
    >>> to_hms(10)
    [0, 0, 10]
    >>> to_hms(61)
    [0, 1, 1]
    >>> to_hms(7199)
    [1, 59, 59]
    """
    # Type your code below
    valid = False
    if str(seconds).isnumeric() and type(seconds) == int:
        if seconds > 0:
          valid = True
          
    if valid:
      mins, secs = divmod(seconds, 60)
      hours, mins = divmod(mins, 60)
      return [hours, mins, secs]
    else:
      print("Unsupported input type.")