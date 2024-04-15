import unittest

from generate_page import extract_title, generate_page

class TestExtractPage(unittest.TestCase):
    def test_extract_title(self):
        text = "# I am correct"
        result = extract_title(text)

        self.assertEqual(result, "I am correct")

    def test_generate_page(self):
        pass
        

