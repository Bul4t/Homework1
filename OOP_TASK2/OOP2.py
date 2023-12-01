class Product:
    def __init__(self, name, id, price, rate, in_stock):
        self.name = name
        self.id = id
        self.price = price
        self.rate = rate
        self.in_stock = in_stock

    def add_stock(self, add_to_stock):
        self.in_stock += add_to_stock
        return self.in_stock

    def remove_stock(self, removed):
        if removed < self.in_stock:
            self.in_stock -= removed
            return self.in_stock
        else:
            print('Товар капут!')

    def update_rate(self, new_rate):
        self.rate = new_rate

    def update_price(self, new_price):
        self.price = new_price


class Category:
    def __init__(self, name, *list_of_items):
        self.name = name
        self.list_of_items = list(list_of_items)


    def add_item(self, to_be_added):
        self.list_of_items.append(to_be_added)
        return self.list_of_items

    def remove_item(self, to_be_removed):
        if to_be_removed in self.list_of_items:
            self.list_of_items.remove(to_be_removed)
        else:
            print('Элемента нет в списке')

    def get_item(self, item_id):
        for item in self.list_of_items:
            if item.id == item_id:
                return item
        return None


class Basket:
    def __init__(self):
        self.Basket_list = []

    def add_item(self, adding_item):
        self.Basket_list.append(adding_item)

    def remove_item(self, to_be_removed):
        self.Basket_list.remove(to_be_removed)

    def get_item(self, item_id):
        for item in self.Basket_list:
            if item.id == item_id:
                return item
        return None

    def make_purchase(self, id_list):
        buyed_items = []
        for item_id in id_list:
            for item in self.Basket_list:
                if item.id == item_id:
                    buyed_items.append(item.name)
                    self.Basket_list.remove(item)
                    break
        print('Купленные товары:', buyed_items)


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.Basket = Basket()


Laptop = Product('Laptop', 1, 10000, 4.5, 10)
T_Shirt = Product('T-Shirt', 2, 1500, 4.3, 15)
Jeans = Product('Jeans', 3, 2300, 4.0, 14)
PC = Product('PC', 4, 21300, 3.8, 4)

cat_clothes = Category("Clothes")
cat_clothes.add_item(T_Shirt)
cat_clothes.add_item(Jeans)

user1 = User("Us1", "qwerty")

user1.Basket.add_item(T_Shirt)
user1.Basket.add_item(Jeans)

print(user1.Basket.make_purchase([2, 3]))
