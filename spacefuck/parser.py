from spacefuck.language import Commands

class SFParser(object):
    _lines = None
    _tokens = []

    @classmethod
    def from_file(cls, path):
        with open(path, 'r') as f:
           content = f.read()
           lines = content.split("\n")
        
        return cls(lines)

    def __init__(self, lines):
        self._lines = lines

    def get_tokens(self):
        for line in self._lines:
            if len(line) in Commands:
                self._tokens.append(len(line))

        return self._tokens
