import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

def show_image_centered(func):

    image_path = "images/alt_loading.jpg"

    # Убираем рамки окна
    root.overrideredirect(1)

    # Загружаем изображение с использованием PIL
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # Получаем размеры экрана
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Получаем размеры изображения
    img_width, img_height = image.size

    # Вычисляем координаты для центрирования окна
    x = (screen_width - img_width) // 2
    y = (screen_height - img_height) // 2

    # Устанавливаем размеры и позицию окна
    root.geometry(f"{img_width}x{img_height}+{x}+{y}")

    # Создаем метку с изображением
    label = tk.Label(root, image=photo)
    label.pack()

    root.after(100, func)

    root.mainloop()