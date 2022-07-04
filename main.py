
import logging

def loger(path_to_log):
    def decor(func):
        def sub_decor(*args, **kwargs):
            result = func(*args, **kwargs)
            logging.basicConfig(level=logging.INFO, filename=f'{path_to_log}', filemode='w',
                                format=f'%(asctime)s - %(message)s - {args} - {result}')
            logging.info(func.__name__)
            return result

        return sub_decor
    return decor

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

@loger('new.log')
def flat_generator(my_list):
    my = (item for el in my_list for item in el)
    return list(my)

flat_generator(nested_list)

