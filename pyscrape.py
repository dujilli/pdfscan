
import customtkinter as ctk
from tkinter import *
import fpdf
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import filedialog

from pypdf import PdfReader

import shutil

from PIL import ImageTk


# pip install tk, customtkinter, fpdf, pypdf, tkPDFViewer

root = ctk.CTk()
root.geometry("500x500")
root.title("PyScraper")
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("green")
root.wm_iconbitmap()
icopath = ImageTk.PhotoImage(file="thumbs.png")
root.iconphoto(False, icopath)

p1 = None
p2 = None


def open_file_explorer():
    global p1
    global p2

    # text selector
    file_path = filedialog.askopenfilename()

    if file_path:
        if p2:
            p2.destroy()

    p1 = pdf.ShowPdf()
    p2 = p1.pdf_view(frame, pdf_location=open(file_path), width=150, height=150)
    p2.pack(expand=True, fill='both', pady=10, padx=10)

    # text extractor

    reader = PdfReader(file_path)
    text2 = ""
    total_words = 0
    page_count = 0

    for page in reader.pages:
        text2 += page.extract_text() + "\n\n"
        total_words += len(text2)
        page_count += 1

    frame3 = ctk.CTkFrame(frame2)
    frame3.pack(pady=5, padx=10, fill='both', expand=True)

    label2 = ctk.CTkLabel(frame3, text=f'Letter count: {total_words}', font=('Roboto', 10),
                          corner_radius=10,
                          text_color='white')

    label3 = ctk.CTkLabel(frame3, text=f'Page count: {page_count} ', font=('Roboto', 10),
                          corner_radius=10,
                          text_color='white')

    label4 = ctk.CTkLabel(frame3, text=f'File path: {file_path}', font=('Roboto', 10),
                          corner_radius=10,
                          text_color='white')

    label2.pack(side=LEFT, pady=5, padx=5)
    label3.pack(side=RIGHT, padx=5)
    label4.pack(side=TOP, pady=5)

    # text builder
    pdf1 = fpdf.FPDF(format='letter')
    pdf1.add_page()

    pdf1.add_font('Arial', '', 'c:/windows/fonts/arial.ttf', uni=True)
    pdf1.set_font('Arial', '', 10)

    pdf1.multi_cell(200, 6, txt=text2, align="L")
    pdf1.output("test.pdf")
    pass


def download():
    # text saver
    file_download = filedialog.asksaveasfilename(filetypes=[('PDF', ".pdf")], defaultextension='.pdf')
    if file_download:
        shutil.copy('test.pdf', file_download)
    pass


# Buttons

frame = ctk.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill='both', expand=True)

frame2 = ctk.CTkFrame(master=frame)
frame2.pack(pady=10, padx=10, fill='both', expand=True)

label = ctk.CTkLabel(frame2, text="PyDFScraper", font=('Lemon Milk', 30),
                     corner_radius=10,
                     text_color='white',)

button = ctk.CTkButton(frame2, text="SELECT PDF FILE",
                       font=('Roboto', 11),
                       text_color='black',
                       hover_color='grey',
                       corner_radius=5,
                       command=open_file_explorer)
button2 = ctk.CTkButton(frame2, text="DOWNLOAD SCRAPED PDF",
                        font=('Roboto', 11),
                        text_color='black',
                        hover_color='grey',
                        corner_radius=5,
                        command=download)

label.pack(pady=8, padx=10)
button.pack(side=TOP, padx=8)
button2.pack(side=TOP,pady=10, padx=10)

root.mainloop()
