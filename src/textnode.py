from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, TEXT, TEXT_TYPE, URL):
        self.text= TEXT
        self.text_type=TEXT_TYPE
        self.url= URL
    def __eg__(self,other_node):
        if self.text == other_node.text and self.text_type == other_node.text_type and self.url == other_node.url:
            return True
        
    

    