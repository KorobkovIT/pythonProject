#Свой YouTube

class User:
    user = []
    def __init__(self, nickname, password, age):
        self.nickname = nickname                    #nickname(имя пользователя, строка)
        self.password = password                    #password(в хэшированном виде, число)
        self.age = age                              #age(возраст, число)

class Video:
    video = []
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title                          #title(заголовок, строка)
        self.duration = duration                    #duration(продолжительность, секунды)
        self.time_now = time_now                     #time_now(секунда остановки (изначально 0))
        self.adult_mode = adult_mode                #adult_mode(ограничение по возрасту, bool (False по умолчанию))
        self.video.append(title)

class UrTube:
    def __init__(self):
        self.users = User.user                         #users(список объектов User)
        self.videos = Video.video                        #videos(список объектов Video)
        self.current_user = None                        #current_user(текущий пользователь, User)

    def log_in(self, nickname, password ):
        if nickname in User.nickname and password in User.password:
            self.current_user = user

    def register(self, nickname, password, age):
        if nickname in User.user:
            print(f"Пользователь {nickname} уже существует")
        else:
            User.user.append(nickname)

    def log_out(self):
        current_user = None
        return current_user

    def add(self, *title):
        if title not in Video.video:
            Video.video.append(title)

    def get_videos(self, title):
        getVideos = []
        title_lower = title.lower()
        for elem in Video.video:
            if isinstance(elem, str):
                videos_lower = []
                videos_lower.append(elem.lower())
                str_videos_lower = str(videos_lower)
                if title_lower in str_videos_lower:
                    getVideos.append(elem)
        return getVideos

    # def watch_video(self):

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# # Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')
#
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')