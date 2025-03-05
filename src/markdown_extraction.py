import re

def extract_markdown_images(text):
    regex_pattern_img= r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_pattern_img, text)
    return matches

def extract_markdown_links(text):
    regex_pattern_link= r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_pattern_link, text)
    return matches

def split_nodes_image(old_nodes):
    pass
    