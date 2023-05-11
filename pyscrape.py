import tkinter as tk
import customtkinter as ctk
from tkinter import *
import fpdf
from customtkinter import CTkButton
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import filedialog
import pypdf
from pypdf import PdfReader
from pypdf import PdfWriter
from fpdf import FPDF
import shutil
import sys
import PIL
from PIL import ImageTk

# pip install tk, customtkinter, fpdf, pypdf, tkPDFViewer

root = ctk.CTk()
root.geometry("500x500")
root.title("Adowasp PDF Scraper")
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
    p2.pack(expand=True, fill='both', pady=20, padx=20)

    # text extractor

    reader = PdfReader(file_path)
    text2 = ""

    for page in reader.pages:
        text2 += page.extract_text() + "\n\n"

        page2 = len(page)
        len2 = len(text2)

        frame3 = ctk.CTkFrame(frame2)
        frame3.pack(pady=10, padx=10, fill='both', expand=True)

        label2 = ctk.CTkLabel(frame3, text=f'Letter count: {str(len2)}', font=('Roboto', 10),
                              corner_radius=10,
                              text_color='white')

        label3 = ctk.CTkLabel(frame3, text=f'Page count: {str(page2)}', font=('Roboto', 10),
                              corner_radius=10,
                              text_color='white')

        label4 = ctk.CTkLabel(frame2, text=f'{file_path}', font=('Roboto', 10),
                              corner_radius=10,
                              text_color='white')

        label2.pack(side=LEFT, padx=5, pady=5)
        label3.pack(side=RIGHT, padx=5, pady=5)
        label4.pack(padx=5,pady=5)

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

label = ctk.CTkLabel(frame2, text="AdoBee PDF SCRAPER", font=('Lemon Milk', 30),
                     corner_radius=10,
                     text_color='white',

                     )

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
button.pack(padx=8)
button2.pack(pady=15, padx=10)

root.mainloop()