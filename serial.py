"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        """Creates a new generator, and starting point"""
        self.start = self.next = start

    def __repr__(self):
        """Show Representation"""
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Return next serial"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset serial, and starts from original start point"""
        self.next = self.start
