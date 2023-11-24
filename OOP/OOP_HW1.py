class Book:

    def __init__(self, name, autor, year, num_of_pages):
        self.name = name
        self.autor = autor
        self.year = year
        self.num_of_pages = num_of_pages
    def out(self):
        print(f'Название книги: {self.name}')
        print(f'Автор книги: {self.autor}')
        print(f'Год издания книги: {self.year}')
        print(f'Кол-во страниц книги: {self.num_of_pages}')

    def change_pages(self, new_pages):
        self.num_of_pages = new_pages
    def __str__(self):
        return f'Название книги: {self.name}, Автор книги: {self.autor}, Год издания книги: {self.year}, Кол-во страниц книги: {self.num_of_pages}'

#Создание экземпляров

book1 = Book('Евгуний Онегин', 'АС Пушкин', '2011', '339')
book2 = Book('Война и мир', 'Лэв Толстой', '2013', '10')
print(book1)
print("_______________________________________")
print(book2)
print("_______________________________________")

#Поверка методов (book1)

book1.out()
print(book1)
print("_______________________________________")

book1.change_pages(434)
print(book1)
print("_______________________________________")

#Поверка методов (book2)

book2.out()
print(book2)
print("_______________________________________")

book2.change_pages(693)
print(book2)
print("_______________________________________")

