import unittest #  unittest modülü, birim testlerinin yazılmasını ve çalıştırılmasını kolaylaştırır.
from faker import Faker # Bu satır, rastgele veri oluşturmak için popüler bir üçüncü taraf kütüphanesi olan Faker'ı içe aktarır.
from Yonetim import Yonetim
from Firma import Firma
from Sektor import Sektor

class Yonetimtest(unittest.TestCase): # Bu sınıf, unittest.TestCase sınıfından türetilir, bu da bu sınıfın birim 
#testlerini yazmak için unittest çerçevesini kullanacağını gösterir.

    def __init__(self,methodName='yonetimTest'):
        super().__init__(methodName) #Bu satır, üst sınıf olan unittest.TestCase'in yapıcı metodunu çağırır.
        self.yonetim =Yonetim()
        faker =Faker()
        for i in range(100):
            firmaAdi = faker.company()
            cadde= faker.street_name()
            if i == 50:
                self.firmaAdiKontrol =firmaAdi
                self.caddeAdiKontrol=cadde
            firma= Firma(firmaAdi,cadde,faker.building_number(),faker.city(), faker.country(),
                         faker.random_element(elements= [
                             Sektor.Bilinmiyor.name,
                             Sektor.Enerji.name,
                             Sektor.Saglik.name,
                             Sektor.Savunma.name,
                             Sektor.Kozmetik.name,
                             Sektor.Teknoloji.name

                         ]))
            self.yonetim.firma_ekle(firma)
            print(firma)

    def test_firma_sorgula(self):
        firma= Firma(self.firmaAdiKontrol)
        self.assertTrue(self.yonetim.firma_sorgula(firma))

    def test_firma_adres_sorgula(self):
        self.assertTrue(self.yonetim.firma_sorgula(self.caddeAdiKontrol))

    def test_olmayan_firma_sorgula(self):
        firma= Firma("Vestel")
        self.assertFalse(self.yonetim.firma_sorgula(firma))


if __name__ == "__main__":
    unittest.main()
# if __name__ == "__main__": bloğu, bir Python dosyasının başka bir dosya tarafından içe aktarıldığında çalıştırılmasını engellemek için kullanılır. 
# Bu blok, yalnızca dosyanın doğrudan çalıştırıldığında çalışır

        