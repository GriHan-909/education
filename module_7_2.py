def custom_write(file_name, strings):
    my_dict={}
    with open(file_name, 'a', encoding='utf-8') as file:
        for ind, string in enumerate(strings):
            position = file.tell()
            file.write(f'{string}\n')
            my_dict[(ind+1, position)] = string
    return my_dict


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
