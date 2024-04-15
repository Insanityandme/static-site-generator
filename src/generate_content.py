import os

from markdown_blocks import (
        markdown_to_blocks,
        markdown_to_html_node,
        block_type_heading,
        block_to_block_type
    )

def extract_title(md):
    lines = md.split("\n")
    
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    return ValueError("No h1 heading present in markdown page")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_md = ""
    template_html = ""

    with open(from_path, 'r') as f:
        from_md = f.read() 

    with open(template_path, 'r') as f:
        template_html = f.read()

    from_html = markdown_to_html_node(from_md).to_html()
    title = extract_title(from_md)

    dest_html = template_html.replace("{{ Title }}", title)
    dest_html = dest_html.replace("{{ Content }}", from_html)

    dirs = dest_path.split("/")
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    to_file = open(dest_path, "w")
    to_file.write(dest_html)
    to_file.close()
        

