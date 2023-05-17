import translator
import unittest

class translationTestCases(unittest.TestCase):

    def test_e2f_null_input(self):
        self.assertNotEqual(translator.englishToFrench(None) , None)
        
    def test_f2e_null_input(self):
        self.assertNotEqual(translator.frenchToEnglish(None) , None)
    
    def test_e2f_translation(self):
        self.assertEqual(translator.englishToFrench("Hello") , "Bonjour")

    def test_f2e_translation(self):
        self.assertEqual(translator.frenchToEnglish("Bonjour") , "Hello")


if __name__ == "__main__":
    unittest.main()