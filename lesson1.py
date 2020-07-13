import time

import sys


# def foo():
#     for i in range(100**10):
#         yield i
# for i in foo()

# for i in foo():
#     print(i)


##############################################################
# Generators
##############################################################
# Example how generator works
# def bar():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield 2
#     print('step 3')
#     yield 3
#
#
# for x in bar():
#     print(x)
#

# ##############################################################
# # Generator style
#
# gen = (i for i in range(10 ** 100))
#
#
# def foo():
#     for i in range(10 ** 100):
#         yield i
#
#
# for i in foo():
#     print(i)
#
# lst = []
# for i in range(100*100):
#     lst.append(i)
#
# # compare size of taken memory
#
# lst = [i for i in range(100*100)]
# lst1 = (i for i in range(100*100))
#
# print(sys.getsizeof(lst))
# print(sys.getsizeof(lst1))
#
#
# ################################################################
#
# # file example
#
file = 'files/lesson1/unformed_names.txt'


# def lazy_file_read(file_path):
#     with open(file_path, 'r') as my_file:
#         for line_ in my_file.read().split(';'):
#             yield line_
#
#
# for line in lazy_file_read(file):
#     print(
#         line.replace('_', ' ')
#     )

# alternative 2
# with open(file, 'r') as f:
#     lines = (l for l in f.read().split(';'))
#
#     for line in lines:
#         print(
#             line
#                 .replace('_', ' ')
#                 .title()
#         )

#
#
#
# def funy(funnu_place):
#     print()
#
#
# def callback(*args, **kwargs):
#     print(kwargs)
#
#
# def hand_made_gen(start, stop, cb, *cb_args, **cb_kwargs):
#     while start < stop:
#         cb(start, *cb_args, **cb_kwargs)
#         start += 1
#
#
# callback(1, 2)
#
# hand_made_gen(0, 10 ** 100, callback, 1)
#
#
# ##############################################################
# # Decorators
# ##############################################################
def profile(f):
    def any_function_name(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        elapsed = time.time() - start
        print(f'Cat sleep during : {elapsed}s')
        return ret

    return any_function_name


def error_handler(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            print('Please change your input next time because cat say meow')

        finally:
            print('Cat go away but promise return to us')
    return inner


@error_handler
@profile
def sleepy_cat_say(replica):
    print(replica)



# @profile
# @error_handler
def sleepy_cat_go_upstairs(stairs_count):
    assert type(stairs_count) == int
    if stairs_count > 2:
        print('It so difficult, I`m better back to sleep')
    elif stairs_count > 0:
        print('It still too difficult, leave me alone')
    else:
        raise ValueError('You maybe crazy')


sleepy_cat_say('meow')










#
#
# @profile
# def foo():
#     time.sleep(2)
#
#     return 42
#
#
# # foo_decorated = profile(foo)
#
# # @profile
# @cache
# def fib(n):
#     result = 1 if n <= 2 else fib(n - 1) + fib(n - 2)
#     return result
#
#
# print(fib(140))


# is_finish = True
#
# while is_finish:
#     try:
#         a = int(input('Please enter number(): '))
#         is_finish = False
#     except:
#         print('Try again')
#     finally:
#         break


