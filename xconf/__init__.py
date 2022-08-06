class Config:
    def __init__(self, filename):
        self._ini_file = filename
        self._config = {}
        self._read_ini(self._ini_file)

    def _read_ini(self, filename):
        with open(filename) as f:
            for line in f:
                prop, val = line.strip().split("=")
                self._config[prop] = val

    def get(self, prop):
        return self._config.get(prop, None)

    def __repr__(self):
        return f"<xconf.Config at {hex(id(self))}: {self._config}>"
