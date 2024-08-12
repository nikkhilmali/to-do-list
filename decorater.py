def convert(fun):
    def shout(*args):
        return fun(*args).upper()
    return shout


@convert
def say_hello(text):
    return text + "!!!!"


print(say_hello("Hello"))
