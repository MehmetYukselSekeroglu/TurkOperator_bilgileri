#!/usr/bin/env python3 
# https://github.com/TheKoba-dev tarafından Hanedan-ı Root için yazılmış grafiksel
# bir osint aracıdır 


import tkinter as tk
from tkinter.font import Font
from tkinter.ttk import Button

# operatör tespitini yapan fonksiyon
def check_number(phone_numbber):
    abone_numarası = phone_numbber[3:10]
    if len(phone_numbber) < 10:
        return {"success":False, "message":"numara olması gerekenden kısa"}
    elif len(phone_numbber) > 10:
        return {"success":False, "message":"numara olması gerekenden uzun"}
    
    saglayıcı_kodu=phone_numbber[0:3]
    TurkTelekom = ["501", "505", "506","507","552","553","554","555","559"]
    TurkCell = ["530","531","532","533","534","535", "536", "537", "538", "539"]
    Vodafone = ["541", "542", "543", "544", "545", "546", "547", "548", "549"]
    if saglayıcı_kodu in TurkTelekom:
        SaglayıcıBilgisi = "TurkTelekom"
    elif saglayıcı_kodu == "551":
        SaglayıcıBilgisi = "BİMcell sanal operator | TurkTelekom"
    elif saglayıcı_kodu in TurkCell:
        SaglayıcıBilgisi = "Turkcell"
    elif saglayıcı_kodu == "516":
        SaglayıcıBilgisi = "Bursa mobile sanal operator | Turkcell"
    elif saglayıcı_kodu == "561":
        SaglayıcıBilgisi = "61cell sanal operator | Turkcell" 
    elif saglayıcı_kodu in Vodafone:
        SaglayıcıBilgisi = "Vodafone"
    else:
        SaglayıcıBilgisi="Tespit edilemedi, bölgesel numara olabilir."
    return {"success":True, "operatör":SaglayıcıBilgisi}

# ilgili numara için google dork hazırlayan fonksiyon
def google_dork(phone_number):
    GoogleDork=f"intext:\"+90{phone_number}\" OR intext:\"0{phone_number}\" OR inurl:\"{phone_number}\""
    return GoogleDork

# Tkinter butonu için son fonksiyon
def GetParsePhone():
    number_is = data_input.get()
    if check_number(number_is)["success"]:
        op_is = check_number(number_is)["operatör"]
        num_dork = google_dork(number_is)
        out_data = f"""-- işlem başarılı --

Operatör: {op_is}
Numara için dork:\n{num_dork}
"""
        
    else:
        err_mgs = check_number(number_is)["message"]
        out_data = f"""-X- işlem başarısız -X-

Sebep: {err_mgs}"""
    output_label["text"] = out_data

# Pencere başlık bilgileri
APP_NAME = "Operatör bilgi"
CORP_NAME = "Prime"

RootWindow = tk.Tk()
RootWindow.title(CORP_NAME+" | "+ APP_NAME)
RootWindow.geometry("600x400+200+50")

TitleFonts = Font(family="arial",size="14",)
StandartFonts = Font(family="arial",  size="12",)   
StandartColor = "#0a1e4a"
info_fonts = Font(family="arial", size="9")

üstBilgi = tk.Label( text="Numara: ", font=TitleFonts, fg=StandartColor)
üstBilgi.place(relx=0.01, rely=0.01)

data_input = tk.Entry()
data_input.place(relx=0.15, rely=0.02 ,relheight=0.05, relwidth=0.5)


parse_button = tk.Button(text="kontrol", command=GetParsePhone)
parse_button.place(relx=0.01, rely=0.08)


output_label = tk.Label( RootWindow,text="", justify="left", cursor="arrow")
output_label.place(relx=0.01, rely=0.2)

output_label.bind("<Button-1>", lambda e: RootWindow.clipboard_clear())
output_label.bind("<Button-1>", lambda e: RootWindow.clipboard_append(output_label["text"]))


ek_gösterge = tk.Label(text=f"Powered by {CORP_NAME}\nNumarayı yazarken +90 veya 0 olmadan yaznınız.", justify="left", font=info_fonts)
ek_gösterge.place(relx=0.01, rely=0.9)



RootWindow.mainloop()
