import os
import json
import hashlib

def addArgs(filename, args):
    if len(args)>0 and filename.find("%") == -1:
        raise Exception("Filename must contain a '%' if the function has arguments")
    if filename.find("%") == -1:
        return filename

    m = hashlib.sha256()
    for arg in args:
        m.update(str(arg).encode("ASCII"))

    return filename.replace("%", m.hexdigest())

def JSONMemoize(jsonFilename):
    """Memoize the result of the function in a JSON file."""
    def decorator(func):
        def memoizer(*args):
            filename = addArgs(jsonFilename, args)
            if os.path.exists(filename):
                with open(filename) as f:
                    return json.load(f)
            result = func(*args)
            with open(filename, "w") as f:
                json.dump(result, f)
            return result
        return memoizer
    return decorator
