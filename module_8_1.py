def add_everything_up(item_1, item_2):
    try:
        result = item_1 + item_2
        if isinstance(result, float):
            result = round(result, 6)
            return result
        return result
    except TypeError:
        return str(item_1)+str(item_2)
    


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))