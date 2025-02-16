import tkinter as tk
from tkinter import filedialog, colorchooser
from PIL import Image, ImageTk, ImageDraw, ImageFont

class ResimDüzenleyici:
    def __init__(self):
        self.pencere = tk.Tk()
        self.pencere.title("Resim Düzenleyici")
        
        # Başlangıçta None değerinde olan resimler
        self.guncel_resim = None
        self.orjinal_resim = None
        self.gosterim_resmi = None
        self.metin_rengi = "white"  # Varsayılan metin rengi beyaz

        # Pencere boyutları
        self.pencere.geometry("800x600")
        self.pencere.config(bg="#2C3E50")  # Pencere arka planı

        # Sol panel için bir frame
        self.sol_panel = tk.Frame(self.pencere, width=200, bg="#34495E")
        self.sol_panel.grid(row=0, column=0, rowspan=5, sticky="ns")

        # Resim gösterim alanı
        self.resim_alani = tk.Label(self.pencere, bg="#2C3E50")
        self.resim_alani.grid(row=0, column=1, padx=10, pady=10)

        # Butonlar
        self.ac_button = tk.Button(self.sol_panel, text="Resim Aç", command=self.resim_ac, bg="#16A085", fg="white", font=("Arial", 12), relief="raised", width=15)
        self.ac_button.grid(row=0, column=0, pady=10)

        self.kaydet_button = tk.Button(self.sol_panel, text="Resmi Kaydet", command=self.resim_kaydet, bg="#27AE60", fg="white", font=("Arial", 12), relief="raised", width=15)
        self.kaydet_button.grid(row=1, column=0, pady=10)

        self.yazi_rengi_button = tk.Button(self.sol_panel, text="Yazı Rengi Seç", command=self.yazi_rengi_sec, bg="#F39C12", fg="black", font=("Arial", 12), relief="raised", width=15)
        self.yazi_rengi_button.grid(row=2, column=0, pady=10)

        self.yazi_ekle_button = tk.Button(self.sol_panel, text="Yazı Ekle", command=self.yazi_ekle_tikla, bg="#2980B9", fg="white", font=("Arial", 12), relief="raised", width=15)
        self.yazi_ekle_button.grid(row=3, column=0, pady=10)

        # Boyutlandırma butonları için daha iyi renk uyumu
        self.boyutlandirma_label = tk.Label(self.sol_panel, text="Boyutlandırma:", fg="blue", font=("Arial", 12))
        self.boyutlandirma_label.grid(row=6, column=0, pady=5)

        self.yeni_genislik_label = tk.Label(self.sol_panel, text="Yeni Genişlik:", fg="blue", font=("Arial", 10))
        self.yeni_genislik_label.grid(row=7, column=0, pady=5)

        self.yeni_genislik = tk.IntVar()
        self.yeni_genislik.set(400)  # Varsayılan değer
        self.yeni_genislik_spinbox = tk.Spinbox(self.sol_panel, from_=50, to_=1000, textvariable=self.yeni_genislik, width=10, font=("Arial", 10))
        self.yeni_genislik_spinbox.grid(row=8, column=0, pady=5)

        self.yeni_yukseklik_label = tk.Label(self.sol_panel, text="Yeni Yükseklik:", fg="blue", font=("Arial", 10))
        self.yeni_yukseklik_label.grid(row=9, column=0, pady=5)

        self.yeni_yukseklik = tk.IntVar()
        self.yeni_yukseklik.set(300)  # Varsayılan değer
        self.yeni_yukseklik_spinbox = tk.Spinbox(self.sol_panel, from_=50, to_=1000, textvariable=self.yeni_yukseklik, width=10, font=("Arial", 10))
        self.yeni_yukseklik_spinbox.grid(row=10, column=0, pady=5)

        # Boyutlandırma butonu arka planını değiştirdik
        self.boyutlandir_button = tk.Button(self.sol_panel, text="Boyutlandır", command=self.resim_boyutlandir, bg="#8E44AD", fg="white", font=("Arial", 12), relief="raised", width=15)
        self.boyutlandir_button.grid(row=11, column=0, pady=10)

    def resim_ac(self):
        dosya = filedialog.askopenfilename(filetypes=[("JPEG dosyaları", "*.jpg"), ("PNG dosyaları", "*.png"), ("Tüm dosyalar", "*.*")])
        if dosya:
            self.guncel_resim = Image.open(dosya)
            self.orjinal_resim = self.guncel_resim.copy()
            self.resim_goster()

    def resim_kaydet(self):
        if self.guncel_resim:
            kaydet_dosya = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG dosyaları", "*.jpg"), ("PNG dosyaları", "*.png")])
            if kaydet_dosya:
                self.guncel_resim.save(kaydet_dosya)

    def yazi_rengi_sec(self):
        renk = colorchooser.askcolor()[1]
        if renk:
            self.metin_rengi = renk

    def yazi_ekle_tikla(self):
        if self.guncel_resim and self.yazi_metni.get():
            draw = ImageDraw.Draw(self.guncel_resim)
            font = ImageFont.load_default()
            draw.text((50, 50), self.yazi_metni.get(), fill=self.metin_rengi, font=font)
            self.resim_goster()

    def resim_goster(self):
        if self.guncel_resim:
            self.gosterim_resmi = ImageTk.PhotoImage(self.guncel_resim)
            self.resim_alani.config(image=self.gosterim_resmi)

    def resim_boyutlandir(self):
        if self.guncel_resim:
            yeni_genislik = self.yeni_genislik.get()
            yeni_yukseklik = self.yeni_yukseklik.get()
            self.guncel_resim = self.orjinal_resim.resize((yeni_genislik, yeni_yukseklik))
            self.resim_goster()

if __name__ == "__main__":
    app = ResimDüzenleyici()
    app.pencere.mainloop()
