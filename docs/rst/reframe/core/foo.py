"""foo module."""

def square(a):
    """short description of the function square

    longish explanation: returns the square of a: :math:`a^2`

    :param a: an input argument

    :returns: a*a
    """
    return a*a

def hello(name):
    """Print hello addressed to *name*.

    Args:
      name (str): Name to address.
    """
    print('hello', name)

class Foo:

    """Foo class."""

    def bye(self, name):
        """Print bye addressed to *name*.

        Args:
          name (str): Name to address.
        """
        print('bye', name)

if __name__ == '__main__':
    hello('world')
    Foo().bye('python')
