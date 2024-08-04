import threading
import queue
import time


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        for customer_id in range(1, 21):
            print(f"Посетитель номер {customer_id} прибыл.")
            customer_thread = Customer(customer_id, self)
            customer_thread.start()
            time.sleep(1)

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer.number} сел за стол {table.number}.")
                time.sleep(5)  # Время обслуживания 5 секунд
                table.is_busy = False  # Освободили столик после обслуживания
                print(f"Посетитель номер {customer.number} покушал и ушёл.")
                if not self.queue.empty():
                    next_customer = self.queue.get()
                    self.serve_customer(next_customer)                
                return
        print(f"Посетитель номер {customer.number} ожидает свободный стол.")
        self.queue.put(customer)


class Customer(threading.Thread):
    def __init__(self, number, cafe):
        super().__init__()
        self.number = number
        self.cafe = cafe

    def run(self):
        self.cafe.serve_customer(self)


# Создаем столы в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
