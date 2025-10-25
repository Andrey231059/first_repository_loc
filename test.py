class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        descr = input("Введите описание задачи: ")
        date = input("Введите срок выполнения: ")
        self.tasks.append({"description": descr, "deadline": date, "status": False})

    def print_current_tasks(self):
        for t in self.tasks:
            if not t["status"]:
                print(t["description"], t["deadline"], "Не выполнено")


    def print_all_tasks(self):
        for t in self.tasks:
            if not t["status"]:
                print(t["description"], t["deadline"], "Не выполнено")
            else:
                print(t["description"], t["deadline"], "Выполнено")


    def mark_completed(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]["status"] = True
            print(f"индекс - {index}")
            print(f"всего индекс - {len(self.tasks)}")
        else:
            print("индекс не входить в диапазон списка")

tm = TaskManager()
tm.add_task()          # добавит задачу через ввод
tm.add_task()
tm.print_current_tasks()
number = int(input("Введите номер выполненной задачи: "))
tm.mark_completed(number)
tm.print_all_tasks()
tm.print_current_tasks()




# class Store():
#     def __init__(self,name,address,items=()):
#         self.name = name
#         self.address = address
#         self.items = items
#
#     def entr(self):
#         #print(self.name,self.address,self.items)
#         self.items["apples"] = 60
#         self.items["bananas"] = 80
#         self.items["oranges"] = 130
#         # print(self.name, self.address, self.items)
#
#     def exit(self):
#         # print(self.name,self.address,self.items)
#         if "apples" in self.items:
#             del self.items["apples"]
#         if "bananas" in self.items:
#             del self.items["bananas"]
#         # print(self.name, self.address, self.items)
#
#     def priсe(self):
#         # print(self.name,self.address,self.items)
#         for key in self.items:
#             print(f"в продаже есть - {key} по цене - {self.items[key]}")
#
#     def change(self):
#         if "apples" in self.items:
#             self.items["apples"] = 55
#         if "bananas" in self.items:
#             self.items["bananas"] = 78
#         if "oranges" in self.items:
#             self.items["oranges"] = 145
#
#
# stor1 = Store(name = "Универмаг 1", address = "Мира 5" ,items={})
# stor2 = Store(name = "Универмаг 2", address = "Спортивная 8" ,items={"bananas":75,"apples":65, "oranges":150})
# stor3 = Store(name = "Универмаг 3", address = "Липовая 1" ,items={"bananas":85,"apples":70, "oranges":140})
# stor1.entr()
# stor1.priсe()
# stor1.exit()
# stor1.priсe()
# stor1.change()
# stor1.priсe()