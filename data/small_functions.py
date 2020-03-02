from data.imports import *


def get_factorio_version(path):
    path = Path(path)
    infofilepath = Path.joinpath(path, "data\\base\\info.json")
    with open(infofilepath) as json_file:
        data = json.load(json_file)
    return data["version"]

