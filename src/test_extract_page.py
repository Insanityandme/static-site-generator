import unittest

from generate_page import extract_title, generate_page

class TestExtractPage(unittest.TestCase):
    def test_extract_title(self):
        text = """
### I'm a heading

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

# I'm a heading

* This is a list
* with items
        """
        result = extract_title(text)

        self.assertEqual(result, "I'm a heading")

    def test_generate_page(self):
        pass
        

