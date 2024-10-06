import unittest
from parse_data import *

class TestParsing(unittest.TestCase):
    
    def test_json_AT(self):
        self.assertEqual(ourjson['access_token'], "ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3")
    def test_json_EI(self):
        self.assertEqual(ourjson['expires_in'], 1209600)
    
    def test_yaml_AT(self):
        self.assertEqual(ouryaml['access_token'], "ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3")
    def test_yaml_EI(self):
        self.assertEqual(ouryaml['expires_in'], 1209600)

    def test_xml_TT(self):
        self.assertEqual(testop.text, "set")
    def test_xml_DO(self):
        self.assertEqual(defop.text, "merge")