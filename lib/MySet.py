class MySet:
    def __init__(self, initial_values=None):
        """Initialize the set with unique values from a list."""
        self.dictionary = {}
        if initial_values is not None:
            for value in initial_values:
                self.add(value)

    def add(self, value):
        """Add a value to the set if it is not already present."""
        if value not in self.dictionary:
            self.dictionary[value] = True

    def delete(self, value):
        """Remove a value from the set if it exists."""
        if value in self.dictionary:
            del self.dictionary[value]

    def has(self, value):
        """Check if the set contains a value."""
        return value in self.dictionary

    def size(self):
        """Return the number of elements in the set."""
        return len(self.dictionary)

    def clear(self):
        """Clear all elements from the set."""
        self.dictionary.clear()

    def __str__(self):
        """Return a string representation of the set."""
        elements = ','.join(map(str, self.dictionary.keys()))
        return f'MySet: {{{elements}}}'
