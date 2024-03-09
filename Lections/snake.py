# Импорт необходимых модулей
from tkinter import *
import random

# Установка констант игры
GAME_WIDTH = 1600
GAME_HEIGHT = 900
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#0000FF"

# Класс Змеи
class Snake:

    def __init__(self):
        # Инициализация параметров змеи
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # Генерация начальных координат для змеи
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        # Создание квадратов (частей тела змеи)
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

# Класс Еды
class Food:

    def __init__(self):
        # Генерация случайных координат для еды
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        # Создание еды на холсте
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

# Функция для следующего хода в игре
def next_turn(snake, food):
    # Получение текущих координат головы змеи
    x, y = snake.coordinates[0]

    # Изменение координат в зависимости от направления движения
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Обновление координат головы змеи
    snake.coordinates.insert(0, (x, y))

    # Создание новой части змеи
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    # Проверка на столкновение с едой
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Очки:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        # Удаление хвоста змеи
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # Проверка на столкновение с собой
    if check_collisions(snake):
        game_over()
    else:
        # Вызов следующего хода
        window.after(SPEED, next_turn, snake, food)

# Функция для изменения направления движения змеи
def change_direction(new_direction):
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

# Функция для проверки столкновений
def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False

# Функция для завершения игры
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',65), text="ИГРА ЗАКОНЧЕНА", fill="white", tag="gameover")

# Создание основного окна игры
window = Tk()
window.title("Змейка")
window.resizable(False, False)

# Инициализация переменных
score = 0
direction = 'down'

# Создание метки для отображения очков
label = Label(window, text="Очки:{}".format(score), font=('consolas', 40))
label.pack()

# Создание холста для отображения игрового поля
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

# Размещение окна в центре экрана
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Привязка клавиш к изменению направления змеи
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Создание экземпляров змеи и еды
snake = Snake()
food = Food()

# Запуск игрового цикла
next_turn(snake, food)

# Запуск главного цикла приложения
window.mainloop()