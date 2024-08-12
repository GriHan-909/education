def introspection_info(obj):
    obj_type = type(obj)
    obj_module = obj_type.__module__
    obj_name = obj_type.__name__
    obj_dir = dir(obj)
    attributes = [attr for attr in obj_dir if not callable(getattr(obj, attr))]
    methods = [method for method in obj_dir if callable(getattr(obj, method))]

    info = {
        'type': obj_name,
        'module': obj_module,
        'attributes': attributes,
        'methods': methods
    }
    # Добавление информации о документации объекта, если она есть
    if hasattr(obj, '__doc__') and obj.__doc__:
        info['doc'] = obj.__doc__.strip()
    return info


number_info = introspection_info("42")
for key, value in number_info.items():
    print(f'{key}: {value}')
print('*'*200)

number_info_2 = introspection_info([4, 7, 10])
for key, value in number_info_2.items():
    print(f'{key}: {value}')
