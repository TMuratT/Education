class CinemaTicketSystem:
    def __init__(self):
        self.movies = {}
        self.users = {}
        self.tickets = {}
        self.movie_counter = 1
        self.user_counter = 1
        self.ticket_counter = 1

    def addMovie(self, movieName):
        movie_id = self.movie_counter
        self.movies[movie_id] = movieName
        self.movie_counter += 1  
        return movie_id

    def showAllMovies(self):
        if self.movies:
            for movie_id, movie_name in self.movies.items():
                print(f"ID: {movie_id}, {movie_name}")
        else:
            print("Нет доступных фильмов.")

    def addUser(self, userName):
        user_id = self.user_counter
        self.users[user_id] = userName
        self.user_counter += 1
        return user_id 

    def buyTicket(self, userId, movieId):
        if userId in self.users and movieId in self.movies:
            ticket_id = self.ticket_counter
            self.tickets[ticket_id] = {'userId': userId, 'movieId': movieId}
            self.ticket_counter += 1 
            return ticket_id 
        else:
            return None

    def cancelTicket(self, ticketId):
        if ticketId in self.tickets:
            del self.tickets[ticketId]
            return True 
        else:
            return False

def menu():
    cinema_system = CinemaTicketSystem()

    cinema_system.addMovie("Titanic")
    cinema_system.addMovie("Fight club")
    cinema_system.addMovie("Forrest Gump")

    while True:
        print("\nДоступны следующие действия:")
        print("1. Показать все доступные фильмы")
        print("2. Добавить новый фильм")
        print("3. Добавить нового пользователя")
        print("4. Купить билет")
        print("5. Отменить покупку билета")
        print("6. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            cinema_system.showAllMovies()

        elif choice == '2':
            movie_name = input("Введите название фильма: ")
            movie_id = cinema_system.addMovie(movie_name)
            print(f"Фильм '{movie_name}' добавлен с ID: {movie_id}")

        elif choice == '3':
            user_name = input("Введите имя пользователя: ")
            user_id = cinema_system.addUser(user_name)
            print(f"Пользователь '{user_name}' добавлен с ID: {user_id}")

        elif choice == '4':
            user_id = int(input("Введите ID пользователя: "))
            cinema_system.showAllMovies()
            movie_id = int(input("Введите ID фильма: "))
            ticket_id = cinema_system.buyTicket(user_id, movie_id)
            if ticket_id:
                print(f"Билет с ID: {ticket_id} успешно куплен.")
            else:
                print("Ошибка: неверный ID пользователя или фильма.")

        elif choice == '5':
            ticket_id = int(input("Введите ID билета для отмены: "))
            if cinema_system.cancelTicket(ticket_id):
                print(f"Билет с ID: {ticket_id} успешно отменен.")
            else:
                print("Ошибка: билет с таким ID не найден.")

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Ошибка: неверный выбор. Попробуйте снова.")

menu()