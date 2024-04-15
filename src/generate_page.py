from markdown_blocks import (
        markdown_to_blocks,
        markdown_to_html_node,
        block_type_heading,
        block_to_block_type
    )

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        level = 0
        block_type = block_to_block_type(block)

        for char in block:
            if char == "#":
                level += 1
            else:
                break

        if block_type == block_type_heading and level == 1:
            return block[2:]

        level = 0

    return ValueError("No h1 heading present in markdown page")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    from_file = open(from_path, "r")
    from_md = from_file.read()

    template_file = open(template_path, "r")
    template_md = template_file.read()
    

