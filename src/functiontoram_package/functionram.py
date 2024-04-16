class func_to_ram():
    def use(func):
        cache = {}
        def wrapper(*args):
            if args in cache:
                return cache[args]
            else:
                result = func(*args)
                cache[args] = result
                return result
        return wrapper