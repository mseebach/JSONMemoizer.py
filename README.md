JSONMemoizer.py
===============

A simple function decorator to cache the results of a function in a JSON file.

Usage:

    from JSONMemoizer import JSONMemoize

    @JSONMemoize("myFile.json")
    def memoizedFunction():
    	... (slow operation) ...	
        return result

    @JSONMemoize("myFile-%.json")  # % will be replaced with a hash of the values of a, b, c
    def memoizedFunction(a, b, c):
    	... (slow operation) ...	
        return result

Only results that can be serialized to json can be memoized. Similarly, any arguments to the function must have stable string representations. Finally, as always, memoization is pointless if the function has side effects.

There is no expiry on the cache, not even when your program finishes, as the memoized data is save to a file. The function will never be called again with the same arguments until the JSON file is deleted.