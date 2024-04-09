import unittest

from extract_links import extract_markdown_images

class TestExtractLinks(unittest.TestCase):
    def test_extract_image(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        print(extract_markdown_images(text))
        self.assertEqual(extract_markdown_images(text), 
                         '[("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]')

    def text_extract_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        print(extract_markdown_links(text))
        # [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]



if __name__ == "__main__":
    unittest.main()
