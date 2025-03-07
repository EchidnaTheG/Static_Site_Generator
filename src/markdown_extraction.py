import re
from textnode import TextNode, TextType
def extract_markdown_images(text):
    regex_pattern_img= r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_pattern_img, text)
    return matches

def extract_markdown_links(text):
    regex_pattern_link= r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_pattern_link, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
       if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
       if not node.text:
           continue
       images= extract_markdown_images(node.text)   
       if not images:
           new_nodes.append(node)
           continue
       
       current_text= node.text
       for alt_text, url in images:
            image_markdown = f"![{alt_text}]({url})"
            parts = current_text.split(image_markdown, 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
                
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                
            if len(parts) > 1:
                current_text = parts[1]
            else:
                current_text = ""

       if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
       if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
       if not node.text:
           continue
       current_text =node.text
       links = extract_markdown_links(node.text)
       for alt_text, link in links:
           link_markdown = f"[{alt_text}]({link})"
           parts = current_text.split(link_markdown, 1)
       if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
                
       new_nodes.append(TextNode(alt_text, TextType.LINK, link))
                
       if len(parts) > 1:
                current_text = parts[1]
       else:
                current_text = ""

       if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes
