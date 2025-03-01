from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)

        parts = old_node.text.split(delimiter)
        for i, part in enumerate(parts):
            if i % 2 == 0:  
                if part:  
                    new_nodes.append(TextNode(part, TextType.TEXT))
            else:  
                new_nodes.append(TextNode(part, text_type))
                
    return new_nodes

node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
print(new_nodes)    

        