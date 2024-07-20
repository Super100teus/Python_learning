import random
import tkinter as tk
import pygame
from tkinter import messagebox, filedialog
from tkinter import PhotoImage
from PIL import Image, ImageTk

try:
    resample_method = Image.Resampling.LANCZOS  # Pillow 8.0.0 o más reciente
except AttributeError:
    resample_method = Image.Resampling.LANCZOS  # En versiones recientes, usa esto en lugar de ANTIALIAS


class MemoryGame:
    def __init__(self, root, num_pairs):
        self.root = root
        self.num_pairs = num_pairs
        self.images_paths = []  # Lista para guardar las rutas de las imágenes seleccionadas
        self.images = []
        self.buttons = []
        self.selected = []
        self.pairs_found = 0
        back_image_path = "C:/Users/BatMa/OneDrive/Escritorio/mamada/goku.png"
        back_image = Image.open(back_image_path)
        back_image = back_image.resize((160, 160), resample_method)
        self.default_image = ImageTk.PhotoImage(back_image)
        self.load_images()
        self.prepare_buttons()

    def load_images(self):
        while len(self.images_paths) != self.num_pairs:
            self.images_paths.clear()  # Limpiar la lista en caso de que el número de imágenes no sea el correcto
            images_selected = filedialog.askopenfilenames(
                title=f"Seleccione {self.num_pairs} imágenes para el juego",
                filetypes=[("Archivos de imagen", "*.jpeg *.jpg *.png *.gif *.bmp")]
            )
            if len(images_selected) != self.num_pairs:
                messagebox.showwarning("Advertencia", f"Por favor, seleccione exactamente {self.num_pairs} imágenes.")
            else:
                self.images_paths.extend(images_selected)

        self.images = [Image.open(path) for path in self.images_paths * 2]  # Abre las imágenes y duplica la lista
        random.shuffle(self.images)

        self.gifs_info = {}  # Diccionario para almacenar información de los GIFs
        for i, image in enumerate(self.images):
            if image.filename.endswith('.gif'):
                self.gifs_info[i] = {
                    "path": image.filename,
                    "is_playing": False,
                    "frame_index": 0
                }

    def set_default_images(self):
        default_image_paths = [
            "C:/Users/BatMa/Downloads/Programa del memorama/sandia.png",
            "C:/Users/BatMa/Downloads/Programa del memorama/pera.png",
            "C:/Users/BatMa/Downloads/Programa del memorama/manzana.png",
            "C:/Users/BatMa/Downloads/Programa del memorama/uvas.png"
        ]
        self.images_paths = default_image_paths * 2
        random.shuffle(self.images_paths)
        self.images = [Image.open(path) for path in self.images_paths]

    def play_gif(self, label, file_path, frame_number=0):
        if label.winfo_exists():  # Verifica si el widget todavía existe
            gif = Image.open(file_path)
            try:
                gif.seek(frame_number)
                frame_photo = ImageTk.PhotoImage(gif)
                label.config(image=frame_photo)
                label.image = frame_photo
                frame_number += 1
                self.root.after(100, lambda: self.play_gif(label, file_path, frame_number))
            except EOFError:
                pass  # Detener cuando se alcance el final del GIF

    def prepare_buttons(self):
        num_rows = num_cols = 4  # Configurar el tablero como 4x4

        for i in range(len(self.images)):
            button = tk.Button(self.root, image=self.default_image, width=160, height=160,
                               command=lambda card_index=i: self.on_card_click(card_index))
            button.image = self.default_image

            row = i // num_cols  # Determinar la fila del botón
            col = i % num_cols  # Determinar la columna del botón
            button.grid(row=row, column=col)

            self.buttons.append(button)

    def reset_game(self):
        for button in self.buttons:  # Eliminar botones existentes
            button.destroy()
        self.pairs_found = 0
        self.selected = []
        self.buttons = []
        self.images = []
        self.images_paths = []
        StartMenu(self.root)  # Crear el menú de inicio nuevamente

    def on_card_click(self, card_index):
        if card_index in self.selected or len(self.selected) == 2:
            return

        image_to_show = self.images[card_index]  # Ya es un objeto de imagen
        photo = ImageTk.PhotoImage(image_to_show.resize((160, 160), Image.Resampling.LANCZOS))
        button = self.buttons[card_index]
        button.config(image=photo, state="disabled")
        button.image = photo  # Guardar una referencia a la imagen para evitar que sea recolectada por el recolector de basura

        self.selected.append(card_index)

        if len(self.selected) == 2:
            if self.images[self.selected[0]] == self.images[self.selected[1]]:
                self.pairs_found += 1
                if self.pairs_found == self.num_pairs:
                    self.show_victory_screen()
                self.selected.clear()
            else:
                self.root.after(1000, self.hide_cards)

    def show_victory_screen(self):
        self.game_over = True
        victory_window = tk.Toplevel(self.root)
        victory_window.title("¡Victoria!")
        victory_window.geometry("800x600")

        background_label = tk.Label(victory_window)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.play_gif(background_label, "C:/Users/BatMa/PycharmProjects/pythonProject/Prg_Logica/victoria.gif")

        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Agregar un mensaje de victoria
        victory_label = tk.Label(victory_window, text="¡Felicidades! Has ganado.", font=("Arial", 24), bg="white")
        victory_label.pack(pady=50)

        # Reproducir música de fondo
        pygame.init()
        pygame.mixer.music.load("C:/Users/BatMa/PycharmProjects/pythonProject/Prg_Logica/victoria_happy_wheels.mp3")
        pygame.mixer.music.play()

        # Botón para cerrar la ventana y reiniciar el juego
        close_button = tk.Button(victory_window, text="Cerrar",
                                 command=lambda: [victory_window.destroy(), self.reset_game()])
        close_button.pack(pady=20)

    def hide_cards(self):
        for card_index in self.selected:
            button = self.buttons[card_index]
            button.config(image=self.default_image, state="active")
            button.image = self.default_image
        self.selected.clear()


class QuickMemoryGame(MemoryGame):
    def __init__(self, root, difficulty='normal'):
        super().__init__(root, 4)
        self.game_over = False  # Añadir un indicador de estado del juego
        self.set_default_images()
        self.difficulty = difficulty
        self.setup_timer()

    def setup_timer(self):
        self.timer_label = tk.Label(self.root, text="00:00", font=("Arial", 18))
        self.timer_label.grid(row=0, column=5, padx=20)  # Ajusta la posición según sea necesario
        self.start_timer()

    def start_timer(self):
        self.time_remaining = self.get_time_limit()
        self.update_timer()

    def get_time_limit(self):
        if self.difficulty == 'facil':
            return 600  # 10 minutos
        elif self.difficulty == 'Normal':
            return 300  # 5 minutos
        elif self.difficulty == 'DificiL':
            return 60  # 1 minuto
        else:  # GOD
            return 10  # 10 segundos

    def update_timer(self):
        if self.time_remaining > 0 and not self.game_over:  # Verificar si el juego ya terminó
            mins, secs = divmod(self.time_remaining, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            self.timer_label.config(text=time_format)
            self.time_remaining -= 1
            self.root.after(1000, self.update_timer)
        else:
            if not self.game_over:  # Verificar si el juego ya terminó
                self.show_defeat_screen()

    def show_defeat_screen(self):
        if not self.game_over:
            self.game_over = True
            defeat_window = tk.Toplevel(self.root)
            defeat_window.title(".__. XD")
            defeat_window.geometry("800x600")

            background_label = tk.Label(defeat_window)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.play_gif(background_label, "C:/Users/BatMa/PycharmProjects/pythonProject/Prg_Logica/derrota.gif")

        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Agregar un mensaje de victoria
        victory_label = tk.Label(defeat_window, text="Has Perdido! Suerte para la próxima (;", font=("Arial", 24),
                                 bg="white")
        victory_label.pack(pady=50)

        # Reproducir música de fondo
        pygame.init()
        pygame.mixer.music.load("C:/Users/BatMa/PycharmProjects/pythonProject/Prg_Logica/Game Over 8bit.mp3")
        pygame.mixer.music.play()

        # Botón para cerrar la ventana y reiniciar el juego
        close_button = tk.Button(defeat_window, text="Cerrar",
                                 command=lambda: [defeat_window.destroy(), self.reset_game()])
        close_button.pack(pady=20)
        pass

    def load_images(self):
        # Sobrescribir este método para cargar imágenes por defecto
        default_image_paths = [
            "C:/Users/BatMa/Downloads/Programa del memorama/sandia.png",
            "C:/Users/BatMa/Downloads/Programa del memorama/pera.png",
            "C:/Users/BatMa/Downloads/Programa del memorama/manzana.png",
            "C:/Users/BatMa/Downloads/Programa del memorama/uvas.png"
        ]
        self.images_paths = default_image_paths * 2
        random.shuffle(self.images_paths)
        self.images = [Image.open(path) for path in self.images_paths]


class StartMenu:
    def __init__(self, master):
        self.master = master
        self.game_root = None  # Agregar una referencia a la ventana del juego
        self.master.title("JUEGO DE MEMORIA de lo que quieras!")
        self.master.geometry("800x700")  # Tamaño de la ventana

        # Lista de canciones disponibles
        self.song_list = [
            "C:/Users/BatMa/PycharmProjects/pythonProject/Prg_Logica/Local Forecast.mp3",
            "C:/Users/BatMa/PycharmProjects/pythonProject/Prg_Logica/The Legend of Zelda_ Ocarina of Time - Shop Theme Cover.mp3",
            "C:/Users/BatMa/PycharmProjects/pythonProject/Prg_Logica/Gymnopedie No.1 Bossa ver.mp3"
        ]

        # Cargar y mostrar una imagen de fondo
        self.background_image = Image.open("C:/Users/BatMa/PycharmProjects/pythonProject/Prg_Logica/Chibi_monos.jpeg")
        self.background_image = self.background_image.resize((800, 600), resample_method)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.background_label = tk.Label(master, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Inicializar Pygame para la música
        pygame.init()
        self.is_music_paused = False
        self.load_and_play_music(random.choice(self.song_list))

        # Botón para silenciar/desilenciar la música
        self.mute_button = tk.Button(master, text="Silenciar", command=self.toggle_music)
        self.mute_button.grid(row=1, column=0, padx=20, pady=20, sticky="sw")

        # Botón para cambiar la canción
        self.change_music_button = tk.Button(master, text="Cambiar Canción", command=self.change_music)
        self.change_music_button.grid(row=2, column=0, padx=20, pady=40, sticky="sw")

        # Configuración del botón de inicio
        self.start_button = tk.Button(master, text="Elige tus cartas\ny COMIENZA EL JUEGO", command=self.start_game)
        self.start_button.grid(row=3, column=0, padx=20, pady=20, sticky="sw")
        self.start_button.place(relx=0.5, rely=0.2, anchor="center")  # Posición central, debajo de la etiqueta

        # Configuración del botón de inicio rápido
        self.start_quick_game_button = tk.Button(master, text="Iniciar una Partida", command=self.start_quick_game)
        self.start_quick_game_button.grid(row=5, column=0, padx=20, pady=10, sticky="sw")

        # Selector de dificultad
        self.difficulty_var = tk.StringVar(master)
        self.difficulty_var.set("Normal")  # Valor predeterminado
        self.difficulty_options = ["facil", "Normal", "DificiL", "GOD"]
        self.difficulty_menu = tk.OptionMenu(master, self.difficulty_var, *self.difficulty_options)
        self.difficulty_menu.grid(row=6, column=0, padx=20, pady=20, sticky="sw")

        # Configuración de la etiqueta con el nombre del programa
        self.title_label = tk.Label(master, text="JUEGO DE MEMORIA", font=("Arial", 24))
        self.title_label.grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")  # Posición central superior

        # Configuración del selector de número de pares
        self.num_pairs_var = tk.IntVar(master)
        self.num_pairs_var.set(1)  # Valor predeterminado
        self.options = [str(num) for num in range(1, 9)]
        self.option_menu = tk.OptionMenu(master, self.num_pairs_var, *self.options)
        self.option_menu.grid(row=4, column=0, padx=20, pady=20, sticky="sw")
        self.option_menu.place(relx=0.5, rely=0.3, anchor="center")

    def load_and_play_music(self, music_path):
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)  # Reproducir en bucle

    def toggle_music(self):
        if self.is_music_paused:
            pygame.mixer.music.unpause()
            self.mute_button.config(text="Silenciar")
        else:
            pygame.mixer.music.pause()
            self.mute_button.config(text="Desilenciar")
        self.is_music_paused = not self.is_music_paused

    def change_music(self):
        # Aquí puedes definir la lógica para cambiar la canción
        # Por ejemplo, cargar una canción diferente
        new_song_path = random.choice(self.song_list)
        self.load_and_play_music(new_song_path)

    def start_game(self):
        num_pairs = self.num_pairs_var.get()
        self.master.withdraw()
        self.game_root = tk.Toplevel()  # Guardar la referencia a la nueva ventana
        game = MemoryGame(self.game_root, num_pairs)
        self.game_root.protocol("WM_DELETE_WINDOW", self.on_close_game)

    def start_quick_game(self):
        selected_difficulty = self.difficulty_var.get()
        self.master.withdraw()
        self.game_root = tk.Toplevel(self.master)
        game = QuickMemoryGame(self.game_root, difficulty=selected_difficulty)
        self.game_root.protocol("WM_DELETE_WINDOW", self.on_close_game)

    def on_close_game(self):
        if self.game_root and self.game_root.winfo_exists():
            self.game_root.destroy()  # Cerrar la ventana del juego
            self.game_root = None  # Eliminar la referencia
        if self.master.winfo_exists():
            self.master.deiconify()  # Mostrar la ventana principal nuevamente


def main():
    root = tk.Tk()
    start_menu = StartMenu(root)
    root.mainloop()


if __name__ == "__main__":
    main()