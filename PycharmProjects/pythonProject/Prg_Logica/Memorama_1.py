import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class MemoryGame:
    def __init__(self, root, num_pairs):
        self.root = root
        self.num_pairs = num_pairs
        self.images = [f"image{i}.jpg" for i in range(num_pairs)] * 2
        random.shuffle(self.images)
        self.buttons = []
        self.selected = []
        self.pairs_found = 0

        for i, image in enumerate(self.images):
            img = Image.open(image)
            img = img.resize((100, 100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            button = tk.Button(root, image=photo, width=100, height=100,
                               command=lambda card_index=i: self.on_card_click(card_index))
           # button = tk.Button(root, image=photo, width=100, height=100, command=lambda i=i: self.on_card_click(i))
            button.image = photo
            button.grid(row=i // 4, column=i % 4)
            self.buttons.append(button)

    def on_card_click(self, card_index):
        if card_index in self.selected:
            return

        button = self.buttons[card_index]
        button.config(state="disabled")

        self.selected.append(card_index)

        if len(self.selected) == 2:
            if self.images[self.selected[0]] == self.images[self.selected[1]]:
                self.pairs_found += 1
                if self.pairs_found == self.num_pairs:
                    messagebox.showinfo("Memory Game", "¡Felicidades! Has ganado.")
                    self.root.quit()
            else:
                self.root.after(1000, self.hide_cards)

    def hide_cards(self):
        for card_index in self.selected:
            button = self.buttons[card_index]
            button.config(state="active")
        self.selected.clear()

def main():
    root = tk.Tk()
    num_pairs = 0
    while num_pairs < 1 or num_pairs > 12:
        num_pairs = int(input("Por favor, ingresa el número de pares de cartas para jugar (1-12): "))
        if num_pairs < 1 or num_pairs > 12:
            print("Entrada no válida. Ingresa un número entre 1 y 12.")

    root.title("Juego de Memoria con Imágenes")
    game = MemoryGame(root, num_pairs)
    root.mainloop()

if __name__ == "__main__":
    main()