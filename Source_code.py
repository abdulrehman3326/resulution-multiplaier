import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, Tk, messagebox

class ImageResizerUpscalerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Resizer & Upscaler")

        # Variables
        self.img_path = tk.StringVar()
        self.new_size = tk.DoubleVar()
        self.new_size.set(1.0)  # Default to original size

        # GUI Components
        self.label_path = tk.Label(root, text="Image Path:")
        self.entry_path = tk.Entry(root, textvariable=self.img_path, state="readonly", width=40)
        self.button_browse = tk.Button(root, text="Browse", command=self.browse_image)

        self.label_options = tk.Label(root, text="Resize Options:")
        self.options = ["Original", "Half", "2X"]
        self.option_var = tk.StringVar()
        self.option_var.set(self.options[0])  # Default to Original
        self.option_menu = tk.OptionMenu(root, self.option_var, *self.options, command=self.set_new_size)

        self.button_resize = tk.Button(root, text="Resize", command=self.resize_image)  
        self.button_save_as = tk.Button(root, text="Save As", command=self.save_as_image)  # Save As button

        # Pack GUI Components
        self.label_path.grid(row=0, column=0, padx=10, pady=5, sticky="E")
        self.entry_path.grid(row=0, column=1, padx=5, pady=5, sticky="W")
        self.button_browse.grid(row=0, column=2, padx=10, pady=5)

        self.label_options.grid(row=1, column=0, padx=10, pady=5, sticky="E")
        self.option_menu.grid(row=1, column=1, padx=5, pady=5, sticky="W")

        self.button_resize.grid(row=2, column=0, pady=10, sticky="E")
        self.button_save_as.grid(row=2, column=1, pady=10, sticky="W")  # Save As button

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.img_path.set(file_path)

    def set_new_size(self, option):
        if option == "Half":
            self.new_size.set(0.5)
        elif option == "2X":
            self.new_size.set(2.0)
        else:
            self.new_size.set(1.0)

    def resize_image(self):
        image_path = self.img_path.get()
        if not image_path:
            messagebox.showinfo("Error", "Please select an image.")
            return

        try:
            new_size = self.new_size.get()

            # Fetching image and resizing
            image4resize = cv2.imread(image_path)
            shape_var = np.shape(image4resize)
            size1 = shape_var[0]
            size2 = shape_var[1]

            size_for_resize_photo = (int(size2 * new_size), int(size1 * new_size))
            resized_img = cv2.resize(image4resize, size_for_resize_photo)

            messagebox.showinfo("Info", "Image resized successfully.")

        except Exception as e:
            messagebox.showinfo("Error", f"An error occurred: {e}")

    def save_as_image(self):
        try:
            new_size = self.new_size.get()

            # Fetching image and resizing
            image4resize = cv2.imread(self.img_path.get())
            shape_var = np.shape(image4resize)
            size1 = shape_var[0]
            size2 = shape_var[1]

            size_for_resize_photo = (int(size2 * new_size), int(size1 * new_size))
            resized_img = cv2.resize(image4resize, size_for_resize_photo)

            # Ask the user for the destination path using a file dialog
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

            # If the user cancels the dialog, return
            if not file_path:
                messagebox.showinfo("Info", "Save As canceled.")
            else:
                # Save the resized image using OpenCV
                cv2.imwrite(file_path, resized_img)
                messagebox.showinfo("Info", f"Resized and saved image to: {file_path}")

        except Exception as e:
            messagebox.showinfo("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = Tk()
    app = ImageResizerUpscalerApp(root)
    root.mainloop()
