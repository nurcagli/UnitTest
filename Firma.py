from Sektor import Sektor #Sektor dosyasından sektor classını dahıl eder.

class Firma:
    def __init__(self,adi="",cadde="",no=0,sehir="",ulke="",sektor=Sektor.Bilinmiyor):
        self.adi=adi
        self.adres=self.adres_olustur(cadde,no,sehir,ulke)
        self.sektor=sektor

    def adres_olustur(self,cadde,no,sehir,ulke):
        return f"{cadde} No:{no} , {sehir}/{ulke}"
    
    def adres_kontrol(self,filtre):
        return filtre in self.adres
    
    def __eq__(self,diger):
        if isinstance(diger,Firma):
            return self.adi == diger.adi
        return False
    
    '''
    isinstance() fonksiyonu, bir nesnenin belirli bir sınıfın bir örneği olup olmadığını kontrol eder.
    __eq__ metodundaki isinstance(diger, Firma) ifadesi, 
    diger adlı nesnenin Firma sınıfından bir örnek olup olmadığını kontrol eder
    
    '''

    def __str__(self):
        return f"Firma Adı:{self.adi}\nAdresi:{self.adres}\nSektor:{self.sektor}"
    
    
    
