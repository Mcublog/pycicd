import unittest

import app.example as exmpl


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # Проверим, что s.split не работает, если разделитель - не строка
        with self.assertRaises(TypeError):
            s.split(2)

    def test_main(self):
        self.assertFalse(exmpl.dupa_printing(12))
        self.assertTrue(exmpl.dupa_printing("dupa1"))

    def test_main_2(self):
        self.assertFalse(exmpl.dupa_printing(12))
        self.assertTrue(exmpl.dupa_printing("dupa1"))

    def test_main_3(self):
        self.assertFalse(exmpl.dupa_printing(12))
        self.assertTrue(exmpl.dupa_printing("dupa1"))


if __name__ == "__main__":
    unittest.main()
