# Создай класс Store:
# Создай класс Store:
# -Атрибуты класса:
# name: название магазина.
# address: адрес магазина.
# items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
# Методы класса:
# __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для items`.
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
        self.name = name
        self.address = address
        self.items = items

    def entr(self):
        #print(self.name,self.address,self.items)
        self.items["apples"] = 60
        self.items["bananas"] = 80
        self.items["oranges"] = 130
        # print(self.name, self.address, self.items)

    def exit(self):
        # print(self.name,self.address,self.items)
        if "apples" in self.items:
            del self.items["apples"]
        if "bananas" in self.items:
            del self.items["bananas"]
        # print(self.name, self.address, self.items)

    def priсe(self):
        # print(self.name,self.address,self.items)
        for key in self.items:
            print(f"в продаже есть - {key} по цене - {self.items[key]}")

    def change(self):
        if "apples" in self.items:
            self.items["apples"] = 55
        if "bananas" in self.items:
            self.items["bananas"] = 78
        if "oranges" in self.items:
            self.items["oranges"] = 145


stor1 = Store(name = "Универмаг 1", address = "Мира 5" ,items={})
stor2 = Store(name = "Универмаг 2", address = "Спортивная 8" ,items={"bananas":75,"apples":65, "oranges":150})
stor3 = Store(name = "Универмаг 3", address = "Липовая 1" ,items={"bananas":85,"apples":70, "oranges":140})
stor1.entr()
stor1.priсe()
stor1.exit()
stor1.priсe()
stor1.change()
stor1.priсe()