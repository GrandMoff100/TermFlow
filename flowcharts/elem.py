from .errors import ParentError
from .utils import truecenter

class Elem(object):
    def __init__(self, string):
        self.string = string
        self.children = []
        self.parents = []

    def __repr__(self):
        return f"<Elem string='{self.string}'>"

    # self >> other, self: parent, other: child
    def __rshift__(self, other):
        if not isinstance(other, Elem):
            other = Elem(str(other))

        if len(other.parents) > 2:
            raise ParentError('Cannot have more than two parents per element.')
        if len(self.children) > 2:
            raise ParentError(
                'Cannot have more than two children per element.')

        self.children.append(other)
        other.parents.append(self)
        return other

    # self << other, other: parent, self: child
    def __lshift__(self, other):
        if not isinstance(other, Elem):
            other = Elem(str(other))

        if len(self.parents) > 2:
            raise ParentError('Cannot have more than two parents per element.')

        if len(other.children) > 2:
            raise ParentError(
                'Cannot have more than two children per element.')

        other.children.append(self)
        self.parents.append(other)
        return other

    def __eq__(self, other):
        return other.parents == self.parents and other.children == self.children and self.string == other.string

    def center(self, length):
        return truecenter(self.string, length)
