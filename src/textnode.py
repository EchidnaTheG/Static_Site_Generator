from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, TEXT, TEXT_TYPE, URL=None):
        self.text= TEXT
        self.text_type=TEXT_TYPE
        self.url= URL
    def __eq__(self,other_node):
        if self.text == other_node.text and self.text_type == other_node.text_type and self.url == other_node.url:
            return True
        else:
            return False
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def text_node_to_html_node(self):
        if self.text_type not in TextType:
            raise ValueError(f"Invalid Text Type, {self.text_type} isn't supported")
        if self.text_type == TextType.TEXT:
            return LeafNode(None,self.text)
        elif self.text_type == TextType.BOLD:
            return LeafNode("b",self.text)
        elif self.text_type == TextType.ITALIC:
            return LeafNode("i", self.text)
        elif self.text_type == TextType.CODE:
            return LeafNode("code", self.text)
        elif self.text_type == TextType.LINK:
            return LeafNode("a", self.text,props={"href":self.url})
        elif self.text_type == TextType.IMAGE:
            return LeafNode("img", None,props={"src":self.url, "alt":self.text})

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING= "heading"
    CODE= "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
