import multiprocessing

class WarehouseManager:
    data = {}

    def __str__(self):
        return str(self.data)

    def process_request(self, request):
        if request[1] == 'receipt':
            if request[0] in self.data:
                self.data[request[0]] += request[2]
            else:
                self.data[request[0]] = request[2]
        elif request[1] == 'shipment':
            if request[0] in self.data and self.data[request[0]] > 0:
                self.data[request[0]] -= request[2]
        return self.data

    def run(self, request):
        with multiprocessing.Pool(processes=5) as pool:
            self.data = pool.map(self.process_request, request)[-1]


if __name__ == '__main__':
    # Создаем менеджера склада
    manager = WarehouseManager()

    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]
    # Запускаем обработку запросов
    manager.run(requests)

    # Выводим обновленные данные о складских запасах
    print(manager)