import requests
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button, PhotoImage


link = "https://randomfox.ca/floof/"

def read_image():
    im_l = requests.get(link).json()
    print(im_l)
    im_l = requests.get(im_l["image"], stream=True).raw
    img = Image.open(im_l)
#   img = img.resize((800, 800), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)

    return img

def change_img():
    img = read_image()
    lbl1.config(image=img)
    lbl1.image = img

root = Tk()
root.title("Fox generator")

img = read_image()
lbl1 = Label(root, image=img)
lbl1.image = img
lbl1.pack()

btn = Button(text="Generate image", command=change_img)
btn.pack()

root.mainloop()
