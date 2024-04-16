import unittest

from generate_content import (
    extract_title, 
    generate_page,
    generate_pages_recursive,
)

class TestGenerateContent(unittest.TestCase):
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

    # def test_generate_page(self):
    #     print("Generating page...")
    #     generate_page(
    #         "content/index.md",
    #         "template.html",
    #         "public/index.html",
    #     )

    # def test_generate_pages(self):
    #     from_path = "content"
    #     template_path = "template.html"
    #     dest_path = "public"

    #     generate_pages_recursive(from_path, template_path, dest_path)
        

