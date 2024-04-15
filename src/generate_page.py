from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    nodes = markdown_to_html_node(markdown)
    print(nodes)

    return "hi" 

def generate_page(markdown):
    pass
