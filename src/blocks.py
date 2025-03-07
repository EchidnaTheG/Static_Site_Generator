from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING= "heading"
    CODE= "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(md):

    if re.match(r"^#{1,6} .+", md):
        return BlockType.HEADING
    
    elif re.match(r"^```[\s\S]*```$", md):
        return BlockType.CODE

    else:
        return BlockType.PARAGRAPH
