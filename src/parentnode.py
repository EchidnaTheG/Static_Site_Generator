from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None , children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode missing 'tag' parameter")
        if self.children is None or len(self.children) == 0:
            raise ValueError("ParentNode Missing 'children'")
        html= f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html += child.to_html()

        html += f"</{self.tag}>"
        return html
    

    def __eq__(self, other):
        if not isinstance(other, ParentNode):
            return False
        
        return(self.tag == other.tag and 
                self.children == other.children and 
                self.props == other.props)