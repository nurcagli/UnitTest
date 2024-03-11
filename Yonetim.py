from Firma import Firma

class Yonetim:
    def __init__(self):
        self.firmalar=[]

    def firma_ekle(self,firma):
        self.firmalar.append(firma)

    def firma_sorgula(self,filtre):
        if isinstance(filtre,Firma):
            return any(f == filtre for f in self.firmalar)
        else:
            return any(f.adres_kontrol(filtre) for f in self.firmalar)
        

#any() fonksiyonu, verilen koşulu herhangi 
#bir öğe sağlayana kadar firmalar listesindeki her bir öğeyi (f) adres_kontrol() metoduna gönderir.

    def __str__(self):
        cikti=""
        for firma in self.firmalar:
            cikti += str(firma) + "\n----------------" 
        return cikti
    