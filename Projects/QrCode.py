import pandas as pd
# import pyqrcode
# # import pandas

# def createQRCode():
#     data = pd.read_csv('BTECH COMPUTER SCIENCE.docx')
#     image = pyqrcode.create(data)
#     image.svg('Btech.svg', scale = 5)
    
# createQRCode()

from tkinter import *
import tkinter as tk
import pandas as pd
import pyqrcode

# Create a QR code object
data = "Hello, World!"
qr = pyqrcode.create(data)

# Create a pandas dataframe from the QR code object
df = pd.DataFrame(qr.text(), columns=[data])

# Save the QR code as a PNG image
qr.png("qr_code.png", scale=6)

# root = tk.Tk()
# root.title('QR Code')
# root.geometry('250x250')
# root.resizable(0, 0)

# def createQr():
#     data = ent.get()
#     qr = pyqrcode.create(data)
#     # df = pd.DataFrame(qr.text(), columns=[data])
#     ent.insert(0, f'{qr}')
#     # qr.png("qr_code.png", scale=5)
    

# fr = Frame(root)
# fr.pack()

# ent = Entry(root, width=30)
# ent.pack()

# btn = Button(root, text = 'CreateQRCode', command=createQr)
# btn.pack()

# rec = Entry(fr)
# rec.pack()
# root.mainloop()




# import pyqrcode
# import pandas as pd

# # Use pandas to read data from a CSV file
# data = pd.read_csv("studentdata.csv")

# # Create a QR code object
# qr = pyqrcode.create(data)

# # Save the QR code as a PNG file
# try:
#     qr.png("qr_code.png", scale=6)
#     print("QR code saved successfully!")
# except:
#     print("Error saving QR code.")
import pyqrcode
import pandas as pd

# Create QR code
data = "https://www.google.com"
qr = pyqrcode.create(data)

# Save QR code as PNG file
qr.png("qr_code.png", scale=8)
