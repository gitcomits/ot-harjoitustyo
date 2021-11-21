import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti 

class TestKassapaate(unittest.TestCase):
    def setUp(self): 
        self.kassapaate = Kassapaate() 
        self.maksukortti = Maksukortti(400)

    def test_edullinen_lounas_maksukortilla_kun_kortilla_on_rahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_myytyjen_lounaiden_maara_kasvaa_kortilla_ostettaessa_edulliset(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_salod_ei_pienene_kun_kortilla_ei_ole_rahaa_edulliset(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 1.6")

    def test_kortilla_ei_ole_rahaa_false_palautuu_edulliset(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti),False)

    def test_myytyjen_lounaiden_maara_ei_muutu_kun_kortilla_ei_ole_rahaa_edulliset(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_kassa_ei_kasva_kortilla_ostaessa_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti) 
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)


    def test_maukas_lounas_maksukortilla_kun_kortilla_on_rahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_myytyjen_lounaiden_maara_kasvaa_kortilla_ostettaessa_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_salod_ei_pienene_kun_kortilla_ei_ole_rahaa_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")

    def test_kortilla_ei_ole_rahaa_false_palautuu_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti),False)

    def test_myytyjen_lounaiden_maara_ei_muutu_kun_kortilla_ei_ole_rahaa_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_kassa_ei_kasva_kortilla_ostaessa_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti) 
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_kortin_saldo_muuttuu_kortille_rahaa_ladatessa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,600)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_kortin_saldo_ei_muuttu_kortille_rahaa_ladatessa_0_euroa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-1)
        self.assertEqual(str(self.maksukortti), "saldo: 4.0")


    def test_kassan_saldo_muuttuu_kortille_rahaa_ladatessa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,600)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100600)

    



    def test_edulliset_on_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0) 

    def test_maukaat_on_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat,0)

    def test_kassassa_rahaa_1000_euroa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisesti_kateismaksu_palauttaa_260(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

    def test_maukkaasti_kateismaksu_palauttaa_100(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_kassa_kasvaa_240_eddullisesti_syodessa_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kassa_kasvaa_400_maukkaasti_syodessa_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_myydyt_lounaat_kasvavat_syodessa_maukkaasti_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_myydyt_lounaat_kasvavat_syodessa_edullisesti_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kassa_ei_muutu_maukkaasti_syodessa_kateisella_liaan_pieni_maksu(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassa_ei_muutu_edullisesti_syodessa_kateisella_liaan_pieni_maksu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_vaihtorahat_palautetaan_kun_liaan_pieni_maksu_syo_edullisesti(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_vaihtorahat_palautetaan_kun_liaan_pieni_maksu_syo_maukkaasti(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

    def test_myydyt_lounaat_ei_muutu_kun_liaan_pieni_maksu_syo_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_myydyt_lounaat_ei_muutu_kun_liaan_pieni_maksu_syo_edullisesti(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)    