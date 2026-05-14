# MoneySurvivor-AIGuard: Finansal Okuryazarlık ve Strateji Oyunu
# Hedef: Risk almadan, gerçek verilerle finansı öğreten global bir simülasyon.
# --- MoneySurvivor-AIGuard V0.1 ---

def baslangic_ekrani():
    print("*" * 40)
    print("  MONEY SURVIVOR & AI GUARD'A HOS GELDINIZ  ")
    print("       'Kaybetmeden Ogrenme Zamani'       ")
    print("*" * 40)
    
    varsayilan_bakiye = 50000
    print(f"\nSistem size baslangic sermayesi olarak {varsayilan_bakiye} TL tanimladi.")
    
    secim = input("Kendi bakiyenizi girmek ister misiniz? (Evet/Hayır): ").lower()
    
    if secim == "evet":
        bakiye = float(input("Lutfen simule etmek istediginiz tutari giriniz: "))
    else:
        bakiye = varsayilan_bakiye
        
    print(f"\nBasarili! Mevcut bakiyeniz: {bakiye} TL")
    print("AI Guard (Gemini) baglantisi kuruluyor...")
    print("Piyasa verileri cekiliyor... (Yarin guncellenecek)")

if __name__ == "__main__":
    baslangic_ekrani()
