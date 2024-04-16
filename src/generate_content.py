import os
from pathlib import Path

from markdown_blocks import (
        markdown_to_blocks,
        markdown_to_html_node,
        block_type_heading,
        block_to_block_type
    )

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content_dirs = os.listdir(dir_path_content)

    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)

        if os.path.isfile(src_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(src_path, template_path, dest_path)
        else:
            generate_pages_recursive(src_path, template_path, dest_path)


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

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    to_file = open(dest_path, "w")
    to_file.write(dest_html)
    to_file.close()

def extract_title(md):
    lines = md.split("\n")
    
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    return ValueError("No h1 heading present in markdown page")
