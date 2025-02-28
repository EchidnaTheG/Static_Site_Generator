from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None , children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Missing Tag")
        if self.children is None:
            raise ValueError("Missing Children")
        html= f"<{self.tag}>"
        for child in self.children:
            html += child.to_html()

        html += f"</{self.tag}>"
        return html
       