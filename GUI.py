from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("GUI")



def tekan2():
          root2 = tk.Tk()
          root2.title("GUI2")
          root2.config(background="\Penyimpanan internal\Download\Adit.JPG")
          
          label_tekan = tk.Label(root2, text="Terima Kasih telah menekan tombol \nklik untuk melanjutkan!")
          tombol = tk.Button(root2, text="Klik")
          label_tekan.pack()
          tombol.pack()
     
     
def tekan():
          main_window = tk.Tk()
          main_window.title("GUI1")
          label_tekan = tk.Label(main_window, text="Terima kasih telah menekan tombol \ntekan untuk mepanjutkan!")
          tombol = tk.Button(main_window, text="Klik", command=tekan2)
          label_tekan.pack()
          tombol.pack()
  

label = tk.Label(root, text="Welcome")
tombol = tk.Button(root, text="Klik", width=5, height=1,  command=tekan)

label.pack()
tombol.pack()

root.mainloop()