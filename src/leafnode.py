from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag, value, None, props )
    
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value") 
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    
    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return False
        return(self.tag == other.tag and 
                self.value == other.value and 
                self.props == other.props)