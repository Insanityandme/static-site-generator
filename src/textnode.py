text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(node1, node2):
        if (node1.text == node2.text and 
            node1.text_type == node2.text_type and 
            node1.url == node2.url):
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    text_type = text_node.text_type
    if text_type == text_type_text:
        return LeafNode(None, text_node.text)
    elif text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    elif text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    elif text_type == text_type_code:
        return LeafNode("code", text_node.text)
    elif text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid text_type: {text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes_list = []
    
    for old_node in old_nodes:
        closed_delimiter = False

        if old_node.text_type != text_type_text:
            split_nodes_list.append(old_node)
        elif old_node.text_type == text_type_text:
            list_of_txt = old_node.text.split()

            before_delimiter_index = 0 
            before_delimiter_str = ""

            inside_delimiter = []
            inside_delimiter_str = ""

            after_delimiter_str = ""
            after_delimiter_index = 0

            for i in range(0, len(list_of_txt) - 1):
                if delimiter in list_of_txt[i]:
                    before_delimiter_index = i
                    list_of_delimiter = list_of_txt[i].split(delimiter)
                    try:
                        list_of_delimiter[2]
                        closed_delimiter = True
                    except IndexError:
                        inside_delimiter.append(list_of_txt[i].strip(delimiter))
                        del list_of_txt[i]

            for word in list_of_txt:
                if delimiter in word:
                    inside_delimiter.append(word.strip(delimiter))

            for i in range(0, len(list_of_txt) - 1):
                if delimiter in list_of_txt[i] and closed_delimiter == False:
                    after_delimiter_index = i + 1
                    closed_delimiter = True
                else:
                    after_delimiter_index = i + 1

            before_delimiter_str = " ".join(list_of_txt[:before_delimiter_index])
            before_node = TextNode(before_delimiter_str + " ", text_type_text)
            split_nodes_list.append(before_node)

            inside_delimiter_str = " ".join(inside_delimiter)
            inside_node = TextNode(inside_delimiter_str, text_type)
            split_nodes_list.append(inside_node)

            after_delimiter_str = " ".join(list_of_txt[after_delimiter_index:])
            after_node = TextNode(" " + after_delimiter_str, text_type_text)
            split_nodes_list.append(after_node)

            if not closed_delimiter: 
                raise ValueError("Closing delimiter not found")
              
    return split_nodes_list

