import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)
        self.saldo = self.maksukortti

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):

        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")

    def test_saldo_vahenee_jos_rahaa_on_tarpeeksi(self):

        self.maksukortti.ota_rahaa(9)
        self.assertEqual(str(self.maksukortti), "saldo: 0.01")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):

        self.maksukortti.ota_rahaa(22)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

#        self.assertEqual(self.saldo < 22,  False)