from .utils import collapse_list

class Flow:
    def __init__(self, elem):
        self.initial_elem = elem

    def get_relatives(self, elem, found=None):
        if found is None:
            found = {}
        for member in elem.children + elem.parents:
            if found.get(member.string) is None:
                yield member
                found[member.string] = True
                yield from self.get_relatives(member, found)

    def get_starts(self):
        return [
            e for e in self.get_relatives(self.initial_elem)
            if len(e.parents) == 0
        ]

    def get_ends(self):
        return [
            e for e in self.get_relatives(self.initial_elem)
            if len(e.children) == 0
        ]

    def trace_descendants(self, elem, line=None):
        if line is None:
            line = [elem.string]

        for child in elem.children:
            path = line + [child.string]
            if len(child.children) == 0:
                yield path
            elif len(child.children) > 0:
                yield from self.trace_descendants(child, path)

    @property
    def descendant_lines(self):
        return collapse_list([
            list(self.trace_descendants(start)) for start in self.get_starts()
        ])
      
    @property
    def max_elem_w(self):
        return max([len(x) for x in collapse_list([elem.string.split('\n') for elem in self.get_relatives(self.initial_elem)])])

    @property
    def max_elem_h(self):
        return max([len(x) for x in [elem.string.split('\n') for elem in self.get_relatives(self.initial_elem)]])