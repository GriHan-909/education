from time import sleep
from threading import Thread
from datetime import datetime


def wite_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово № {i}'+'\n')
            sleep(0.1)
        return f'Завершилась запись в файл {file_name}'

time_func_start = datetime.now()
print(wite_words(10, 'example1.txt'))
print(wite_words(30, 'example2.txt'))
print(wite_words(200, 'example3.txt'))
print(wite_words(100, 'example4.txt'))
time_func_end = datetime.now()
time_func_res = time_func_end - time_func_start
print(time_func_res)

time_thread_start = datetime.now()
thred_1 = Thread(target=wite_words, args=(10, 'example5.txt'))
thred_2 = Thread(target=wite_words, args=(30, 'example6.txt'))
thred_3 = Thread(target=wite_words, args=(200, 'example7.txt'))
thred_4 = Thread(target=wite_words, args=(100, 'example8.txt'))

thred_1.start()
thred_2.start()
thred_3.start()
thred_4.start()

thred_1.join()
thred_2.join()
thred_3.join()
thred_4.join()
time_thread_end = datetime.now()
time_thread_res = time_thread_end - time_thread_start
print(time_thread_res)