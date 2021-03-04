CONNECTORS = {
    'h': '─',
    'd1': '/',
    'd2': '\\',

}

class View:
    def __init__(self, flow):
        self.flow = flow
        self.assemble()
        
    @property
    def connections(self):
        conns = {}
        for line in self.flow.descendant_lines:
            for i in range(len(line)):
                conn = line[i:i + 2]
                if len(conn) > 1:
                    a, b = conn
                    conns[a] = conns.get(a, set())
                    conns[a].add(b)
        return conns

    def assemble(self):
        conns = self.connections
        



