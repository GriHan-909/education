from termcolor import cprint
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    
    def __repr__(self) -> str:
        return f'{self.nickname}'



class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"Video('{self.title}', {self.duration} seconds)"

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if user.nickname == login and user.password == hash(password):
                self.current_user = user
                cprint(f'Пользователь {user.nickname} вошел в систему', color='green')
                return
            else:
                cprint('Неверные логин или пароль', color='light_red')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                cprint(f"Пользователь {nickname} уже существует", color='dark_grey')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user        

    def log_out(self):
        self.current_user = None
        print("Пользователь вышел из системы")

    def add(self, *videos):
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)
                cprint(f'Видео "{video.title}" добавлено', color='green')
            else:
                cprint(f'{video.title} уже существует', color='dark_grey')

    def get_videos(self, word):
        return [video.title for video in self.videos if word.lower() in video.title.lower()]
    
    def watch_video(self, title):
        if not self.current_user:
            cprint('Войдите в аккаунт чтобы смотреть видео', color='light_red')
            return
        
        for video in self.videos:            
            if video.title.lower() == title.lower():
                if video.adult_mode and self.current_user.age < 18:
                    cprint('Вам нет 18 лет, пожалуйста покиньте страницу', color='light_red')
                    return
                for second in range(1, video.duration+1):
                    print(second, end=' ', flush=True)
                    time.sleep(1)
                print('Конец видео')
                return
        cprint('Видео не найдено', color='dark_grey')
                


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)
ur.add(v1)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
