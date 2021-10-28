# (c) Copyright 21-22 lucifeermorningstar@GitHub, < https://GitHub.com/lucifeermorningstar >
# written By Devil


import sys
import glob
import logging
import importlib
from pathlib import Path
from . import tbot

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


def load_plugins(plugin_name):
    path = Path(f"BD/plugins/{plugin_name}.py")
    name = "BD.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["BD.plugins." + plugin_name] = load
    print("IMPORTED --> " + plugin_name)


path = "BD/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        thepath = Path(a.name)
        plugin_name = thepath.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Bot Started Successfully ")


if __name__ == "__main__":
    tbot.run_until_disconnected()
