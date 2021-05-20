import unittest

def oldAge(age):
    if age>=18:
        return True
    return False

class CrystalTest(unittest.TestCase):
    def test_oldAge(self):
        edad=20
        res=oldAge(edad)
        self.assertEqual(res, True)

    def test_young(self):
        edad=15
        res=oldAge(edad)
        self.assertEqual(res, False)

if __name__ == "__main__":
    unittest.main()