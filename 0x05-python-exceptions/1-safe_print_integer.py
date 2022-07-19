def safe_print_integer(value):
    if (value):
        try:
            print("{:d}".format(value))
        except TypeError:
            return False
    return (True)
