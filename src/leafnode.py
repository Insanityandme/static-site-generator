from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value, props=None):
        super().__init__(tag, props)
        self.value = value

    def to_html(self):
        html_string = ""
        if self.value is None:
            raise ValueError("This leaf node needs a value")
        elif self.tag is None:
            return html_string
        

