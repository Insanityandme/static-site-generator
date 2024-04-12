import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

from markdown_blocks import (
    markdown_to_blocks,
    heading_to_html_node,
    code_to_html_node,
    quote_to_html_node,
    ulist_to_html_node,
    olist_to_html_node,
    paragraph_to_html_node,
    markdown_to_html_node,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_ulist,
    block_type_olist,
)

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
        """
        result = markdown_to_blocks(text)

        self.assertListEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items"
            ], 
            result
        )

    def test_markdown_to_blocks_newlines(self):
        text = """
This is **bolded** paragraph







This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
        """
        result = markdown_to_blocks(text)

        self.assertListEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items"
            ], 
            result
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_block_to_html_node(self):
        block = "# heading wow what a heading"
        result = heading_to_html_node(block)
        self.assertEqual(result.to_html(), "<h1>heading wow what a heading</h1>")

        block = "```I'm a code block yeah```"
        result = code_to_html_node(block)
        self.assertEqual(result.to_html(), "<pre><code>I'm a code block yeah</code></pre>")

        block = "> I'm a quote"
        result = quote_to_html_node(block)
        self.assertEqual(result.to_html(), "<blockquote>I'm a quote</blockquote>")

        block = "* hi\n* wow\n* amazing"
        result = ulist_to_html_node(block)
        self.assertEqual(result.to_html(), "<ul><li>hi</li><li>wow</li><li>amazing</li></ul>")

        block = "- hi\n- wow\n- amazing"
        result = ulist_to_html_node(block)
        self.assertEqual(result.to_html(), "<ul><li>hi</li><li>wow</li><li>amazing</li></ul>")

        block = "1. list\n2. items"
        result = olist_to_html_node(block)
        self.assertEqual(result.to_html(), "<ol><li>list</li><li>items</li></ol>")

        block = "this is text"
        result = paragraph_to_html_node(block)
        self.assertEqual(result.to_html(), "<p>this is text</p>")

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )


if __name__ == "__main__":
    unittest.main()
