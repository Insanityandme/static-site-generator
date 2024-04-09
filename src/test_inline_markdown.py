import unittest
from inline_markdown import (
    split_nodes_delimiter,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

class TestInlineMarkdown(unittest.TestCase):
    def test_split_false(self):
        node = TextNode("**This is text that is bold**", text_type_bold)

        self.assertListEqual(split_nodes_delimiter([node], "`", text_type_code),
        [
            TextNode("**This is text that is bold**", text_type_bold),
        ])

    def test_split_correct(self):
        node = TextNode("This is text with a `code block` word", text_type_text)

        self.assertListEqual(split_nodes_delimiter([node], "`", text_type_code),
        [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ])

    def test_split_no_closing_delimiter(self):
        with self.assertRaises(ValueError):
            node = TextNode("This is text with a `code block word", text_type_text)
            nodes = split_nodes_delimiter([node], "`", text_type_code)

    def test_italic_correct(self):
        node = TextNode("This is text with a *italic* word", text_type_text)

        self.assertListEqual(split_nodes_delimiter([node], "*", text_type_italic),
        [
            TextNode("This is text with a ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word", text_type_text),
        ])

    def test_bold_correct(self):
        node = TextNode("This is text with a **bold** word", text_type_text)

        self.assertListEqual(split_nodes_delimiter([node], "**", text_type_bold),
        [
            TextNode("This is text with a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" word", text_type_text),
        ])

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )
