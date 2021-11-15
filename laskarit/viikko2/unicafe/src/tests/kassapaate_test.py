import unittest
from kassapaate import Kassapaate


class TestKassapaate(unittest.TestCase):
    def setUp(self): 
        self.kassapaate = Kassapaate()
#        self.edulliset = Kassapaate()
#        self.maukkat = Kassapaate()

 


    def test_aloituskassa_tasmaa(self):

    #    print(self.kassapaate.kassassa_rahaa)
        self.assertEqual(self.kassapaate.edulliset, 0)

#    self.assertEqual(str(self.maksukortti), "saldo: 0.1")

