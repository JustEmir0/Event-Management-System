import tkinter as tk
from customtkinter import *
from tkinter import messagebox
from CTkListbox import * 
from PIL import ImageTk,Image
import re

class Katilimci:
    def __init__(self, isim, soyisim, yaş, eposta):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş
        self.eposta = eposta

class Etkinlik:
    def __init__(self,Ad,Konum):
        self.Ad = Ad
        self.Konum = Konum


class Bilet:
    def __init__(self, tür, fiyat):
        self.tür = tür
        self.fiyat = fiyat

    def __str__(self):
        return f"{self.tür} Bilet - Fiyat: {self.fiyat} TL"


def giriş_yap():
    app.destroy()
    etkinlik_sistemine_giriş()

def etkinlik_sistemine_giriş():
    root = CTk()
    root.geometry('950x750')
    root.title('Etkinlik Yönetim Sistemi')

    f1 = CTkFrame(master=root,width=420, height=680,corner_radius=30)
    f1.place(x=20,y=40)

    l0 = CTkLabel(master=f1,text="Katılımcı Bilgileri",font=('Arial',20))
    l0.place(x=18,y=25)

    isim_label = CTkLabel(master=f1,text="İsim",font=('Arial',16))
    isim_label.place(x=40,y=60)

    isim_entry = CTkEntry(master=f1,width=150,height=25)
    isim_entry.place(x=35,y=85)

    soyisim_label = CTkLabel(master=f1,text="Soyisim",font=('Arial',16))
    soyisim_label.place(x=40,y=125)
    soyisim_entry = CTkEntry(master=f1,width=150,height=25)
    soyisim_entry.place(x=35,y=150)

    yaş_label = CTkLabel(master=f1,text="Yaşınız",font=('Arial',16))
    yaş_label.place(x=210,y=60)

    yaş_entry = CTkEntry(master=f1,width=150,height=25)
    yaş_entry.place(x=210,y=85)

    eposta_label = CTkLabel(master=f1,text="E-Posta Adresi",font=('Arial',16))
    eposta_label.place(x=210,y=125)

    eposta_entry = CTkEntry(master=f1,width=150,height=25)
    eposta_entry.place(x=210,y=150)

    l1 = CTkLabel(master=f1,text="Etkinlik Seçiniz",font=('Arial',20))
    l1.place(x=12,y=200)

    c1 = CTkComboBox(master=f1, values=güncel_etkinlikler ,width=350)
    c1.place(x=15,y=235)

    l2 = CTkLabel(master=f1,text="Bilet Seçiniz",font=('Arial',20))
    l2.place(x=12,y=280)

    c2 = CTkComboBox(master=f1, values=güncel_biletler ,width=150)
    c2.place(x=15,y=325)

    adet_label = CTkLabel(master=f1,text="Adet:",font=('Arial',16))
    adet_label.place(x=220,y=325)

    c_adet = CTkComboBox(master=f1, values=adet_bilet ,width=100)
    c_adet.place(x=270,y=325)

    l3 = CTkLabel(master=f1,text="Ödeme Bölümü",font=('Arial',20))
    l3.place(x=8,y=380)

    l3_kart_label = CTkLabel(master=f1,text="Kart Numarası",font=('Arial',16))
    l3_kart_label.place(x=20,y=420)

    e3_kart_entry = CTkEntry(master=f1,width=150,height=30)
    e3_kart_entry.place(x=20,y=450)

    l4_skt_label = CTkLabel(master=f1,text="Son Kullanma Tarihi",font=('Arial',16))
    l4_skt_label.place(x=220,y=420)

    e4_kart_skt = CTkEntry(master=f1,width=150,height=30)
    e4_kart_skt.place(x=220,y=450)

    l5_sifre_label = CTkLabel(master=f1,text="Şifre",font=('Arial',16))
    l5_sifre_label.place(x=175,y=490)

    e5_kart_sife = CTkEntry(master=f1,width=150,height=25)
    e5_kart_sife.place(x=125,y=520)

    listbox_label =CTkLabel(master=root,text="--- Etkinlik Bilgileriniz ---",font=('Arial',20))
    listbox_label.place(x=590,y=15)
    
    global listbox1  # listbox1'i global olarak tanımlayın
    listbox1 = CTkListbox(master=root,width=455,height=650)
    listbox1.place(x=460,y=50,)

    

    def ödeme_yap():

        isim = isim_entry.get()
        soyisim = soyisim_entry.get()
        yaş = yaş_entry.get()
        eposta = eposta_entry.get()
        etkinlik = c1.get()
        bilet = c2.get()
        adet = int(c_adet.get())  
        kart_numarası = e3_kart_entry.get()
        skt = e4_kart_skt.get()
        şifre = e5_kart_sife.get()

        # Herhangi bir alanın boş olup olmadığını kontrol et
        if not (isim and soyisim and yaş and etkinlik and bilet and kart_numarası and skt and şifre):
            messagebox.showerror("Eksik Bilgi", "Lütfen eksik alan olmadığından emin olun.")
            return

        # Yaş kontrolü yap
        if int(yaş) < 18:
            messagebox.showerror("Yaş Sınırı", "18 yaşından küçük kişiler Online bilet alışverişi yapamaz.")
            return

        # Kart numarasını kontrol et
        if not re.match(r"^\d{4} \d{4} \d{4} \d{4}$", kart_numarası):
            messagebox.showerror("Geçersiz Kart Numarası", "Lütfen geçerli bir kart numarası girin.")
            return

        # Kart numarası, son kullanma tarihi ve şifrenin tamamının uygun formatlarda olduğundan emin ol
        if not (re.match(r"^(0[1-9]|1[0-2])\/[0-9]{2}$", skt) and
                len(şifre) == 4 and şifre.isdigit()):
            messagebox.showerror("Geçersiz Giriş", "Lütfen son kullanma tarihini MM/YY formatında ve şifrenin 4 haneden oluştuğuna emin olun.")
            return

        
        ödeme_tutarı = adet * 100  

        # Ödeme işlemini gerçekleştir 
        başarılı_ödeme = True 

        # Başarılı ödeme durumunda
        if başarılı_ödeme:
            
            messagebox.showinfo("Ödeme Bilgisi", "Ödemeniz başarıyla gerçekleşti!")

            
            listbox1.insert(tk.END, f"İsim: {isim}")
            listbox1.insert(tk.END, f"Soyisim: {soyisim}")
            listbox1.insert(tk.END, f"Yaş: {yaş}")
            listbox1.insert(tk.END, f"E-Posta: {eposta}")
            listbox1.insert(tk.END, f"Etkinlik: {etkinlik}")
            listbox1.insert(tk.END, f"Bilet: {bilet} - Adet: {adet}")
            listbox1.insert(tk.END, f"Ödeme Tutarı: {ödeme_tutarı} TL")
            listbox1.insert(tk.END, "------------------------")
        else:
            
            messagebox.showerror("Ödeme Hatası", "Ödeme işlemi başarısız oldu. Lütfen tekrar deneyin.")
    
    btn_kart_öde = CTkButton(master=f1,text="Ödeme Yap",width=150,height=30,font=('Arial',16),command=ödeme_yap)
    btn_kart_öde.place(x=125,y=580) 

    root.mainloop()


biletler = [
    Bilet("Öğrenci", 100)
]
güncel_biletler = [f"{bilet.tür} - {bilet.fiyat} TL" for bilet in biletler]

etkinlikler = [
    Etkinlik("Mor ve Ötesi Müzik Konseri", "Tarihi Havagazı Fabrikası Kültür Merkezi"),
    Etkinlik("Gaming İstanbul", " Dr. Mimar Kadir Topbaş Gösteri ve Sanat Merkezi"),
    Etkinlik("Film Gösterimi", "Marmara Forum Sinema Salonu"),
    Etkinlik("Sanat Sergisi", "Lafiye Sanat Galerisi"),
    Etkinlik("Galatasaray - Bayern Münih, Futbol Maçı", "RAMS PARK"),
    Etkinlik("Oyun Yarışması", "Oyun Alanı"),
    Etkinlik("Müze Gezisi", "Topkapı Sarayı")]
güncel_etkinlikler = [f"{etkinlik.Ad} - {etkinlik.Konum} " for etkinlik in etkinlikler]

adet_bilet = [str(i) for i in range(1, 6)]  

#-----Karşılama Page-----#

app = CTk()
app.title('Karşılama Sayfası')
app.geometry("1300x900")


# Büyük yazı etiketi
buyuk_yazi = CTkLabel(master=app, text="BİRBİRİNDEN FARKLI VE EĞLENCELİ ETKİNLİKLERE HAZIRMISINIZ!!", font=('Arial', 30))
buyuk_yazi.place(relx=0.5, rely=0.4, anchor="center")

# Buton
bilet_al_buton = CTkButton(master=app, text="HEMEN BİLET AL", width=500, height=50, font=("Helvetica", 20),corner_radius=30, command=giriş_yap)
bilet_al_buton.place(relx=0.5, rely=0.6, anchor="center")


app.mainloop()