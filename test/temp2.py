def logger(function):
    def wrapper(*args, **kwargs):
        print("----- start -----")
        output = function(*args, **kwargs)
        print("-----  end  -----")
        return output

    return wrapper



def f(a):
    print(a ** 2)
    return 123


drugof = logger(f)

drugof(1)
