# Создай класс Store:
# Создай класс Store:
# -Атрибуты класса:
# name: название магазина.
# address: адрес магазина.
# items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
# Методы класса:
# __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь дляitems`.
# -  метод для добавления товара в ассортимент.
# метод для удаления товара из ассортимента.
# метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
# метод для обновления цены товара.
# 2. Создай несколько объектов класса Store:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.

class Store():
    def __init__(self,name,address,items=()):
        self.name=name
        self.address=address
        self.items=items

    def entrence(self):
        print(self.name,self.address,self.items)
        self.items["apples"] = 60
        self.items["bananas"] = 100
        self.items["oranges"] = 200
        print(self.name, self.address, self.items)

    def exit(self):
        print(self.name,self.address,self.items)
        del self.items["apples"]
        del self.items["bananas"]
        self.items["oranges"] = 200
        print(self.name, self.address, self.items)

    def prise(self):
        print(self.name,self.address,self.items)
        for key in self.items:
            print(f"в продаже есть - {key} по цене - {self.items[key]}")

    store1 = Store(name: "Универмаг№1", address)