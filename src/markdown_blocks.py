import re

from htmlnode import LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered list"
block_type_olist = "ordered list"

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    
    for block in blocks:
        html_node = block_to_html_node(block)
        nodes.append(html_node)

    return ParentNode("div", nodes)

def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []

    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)

    return filtered_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    for i in range(1, 7):
        if block.startswith(i * "#") and block.startswith(" ", i, i + 1):
            return block_type_heading

    if block.startswith("```") and block.endswith("```"):
        return block_type_code

    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist

    return block_type_paragraph

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []

    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))

    return children


def heading_to_html_node(block):
    level = 0

    for char in block:
        if char == "#":
            level += 1
        else:
            break

    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")

    text = block[level + 1 :]
    children = text_to_children(text)

    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")

    text = block[3:-3]

    children = text_to_children(text)
    code = ParentNode("code", children)

    return ParentNode("pre", [code])

def quote_to_html_node(block):
    block_list = block.split("\n") 

    for i in range(0, len(block_list)):
        block_list[i] = block_list[i].replace("> ", "")

    return LeafNode("blockquote", " ".join(block_list))

def ulist_to_html_node(block):
    block_list = block.split("\n") 
    text_nodes = []
    
    li_list = [] 
    for li in block_list:
        text = li[2:]
        children = text_to_children(text)
        li_list.append(ParentNode("li", children))
        
    return ParentNode("ul", li_list)

def olist_to_html_node(block):
    block_list = block.split("\n") 

    li_list = [] 
    for li in block_list:
        text = li[3:]
        children = text_to_children(text)
        li_list.append(ParentNode("li", children))
        
    return ParentNode("ol", li_list)

def paragraph_to_html_node(block):
    block_list = block.split("\n")
    paragraph = " ".join(block_list)
    inline_children = text_to_children(paragraph)
    return ParentNode("p", inline_children)

