import os


class Config:
    def __init__(self, filename, prefix=""):
        self._ini_file = filename
        self._config = {}
        self._read_ini(self._ini_file)
        self._read_env(prefix)

    def _read_ini(self, filename):
        with open(filename) as f:
            for line in f:
                prop, val = line.strip().split("=")
                self._config[prop] = val

    def _read_env(self, prefix):
        env = os.environ
        for key in env:
            if key.startswith(prefix):
                config_key = key[len(prefix):]
                self._config[config_key] = env[key]

    def get(self, prop):
        return self._config.get(prop, None)

    def __repr__(self):
        return f"<xconf.Config at {hex(id(self))}: {self._config}>"
