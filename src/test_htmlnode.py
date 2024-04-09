import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        ) 

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_no_parent_children(self):
        node = LeafNode("b", "Bold text")
        node2 = LeafNode("i", "italic text!")

        parent = ParentNode("p", [node, node2])

        self.assertEqual(parent.to_html(), "<p><b>Bold text</b><i>italic text!</i></p>")

    def test_to_html_parent_children(self):
        node = LeafNode("b", "Bold text")

        node2 = LeafNode("i", "italic text!")
        node3 = ParentNode("p", [node2])

        parent = ParentNode("p", [node, node3])

        self.assertEqual(parent.to_html(), "<p><b>Bold text</b><p><i>italic text!</i></p></p>")

    def test_to_html_parent_with_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", None)
            node.to_html()

    def test_no_tag_error(self):
        children = [LeafNode("b", "Bold text"), LeafNode("i", "italic text")]
        with self.assertRaises(ValueError):
            node = ParentNode(None, children)
            node.to_html()


if __name__ == "__main__":
    unittest.main()
