import unittest

from markdown_extraction import extract_markdown_links, extract_markdown_images, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


class TestMarkDown(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")    
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches= extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev","https://www.boot.dev"),("to youtube","https://www.youtube.com/@bootdotdev")],matches)

    def test_no_markdown_links(self):
        matches = extract_markdown_links("Plain text without links")
        self.assertEqual(len(matches), 0)

    def test_no_markdown_images(self):
        """Test text without any markdown images"""
        matches = extract_markdown_images("Plain text without images")
        self.assertEqual(len(matches), 0)

    def test_multiple_images_same_line(self):
        """Test multiple images on the same line"""
        text = "Images: ![first](img1.png) and ![second](img2.jpg)"
        matches = extract_markdown_images(text)
        self.assertListEqual([
            ("first", "img1.png"),
            ("second", "img2.jpg")
        ], matches)

    def test_invalid_markdown_links(self):
        """Test malformed markdown links"""
        text = "Bad links: [missing](] and [missing too"
        matches = extract_markdown_links(text)
        self.assertEqual(len(matches), 0)

    def test_links_with_special_characters(self):
        """Test links containing special characters"""
        text = "[complex link](https://api.example.com/v1?query=test&page=1)"
        matches = extract_markdown_links(text)
        self.assertListEqual([
            ("complex link", "https://api.example.com/v1?query=test&page=1")
        ], matches)

    def test_images_with_spaces(self):
        """Test images with spaces in alt text and URL"""
        text = "![Alt text with spaces](/path/to/image with spaces.jpg)"
        matches = extract_markdown_images(text)
        self.assertListEqual([
            ("Alt text with spaces", "/path/to/image with spaces.jpg")
        ], matches)

    def test_mixed_content(self):
        """Test mixture of links and images"""
        text = """
        # Header
        ![Image](img.png)
        [Link](https://example.com)
        ![Another Image](another.jpg)
        """
        image_matches = extract_markdown_images(text)
        link_matches = extract_markdown_links(text)
        self.assertEqual(len(image_matches), 2)
        self.assertEqual(len(link_matches), 1)

    def test_empty_string(self):
        """Test empty string input"""
        self.assertEqual(len(extract_markdown_links("")), 0)
        self.assertEqual(len(extract_markdown_images("")), 0)

    def test_extract_single_image(self):
        """Test extracting a single image from text"""
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_images(text)
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0], ("image", "https://i.imgur.com/zjjcJKZ.png"))

    def test_extract_multiple_images(self):
        """Test extracting multiple images"""
        text = "![first](img1.png) and ![second](img2.jpg)"
        matches = extract_markdown_images(text)
        self.assertEqual(len(matches), 2)
        self.assertEqual(matches[0], ("first", "img1.png"))
        self.assertEqual(matches[1], ("second", "img2.jpg"))

    def test_split_nodes_single_image(self):
        """Test splitting nodes with a single image"""
        node = TextNode("Before ![image](test.png) after", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Before ")
        self.assertEqual(result[1].text, "image")
        self.assertEqual(result[1].url, "test.png")
        self.assertEqual(result[2].text, " after")

    def test_split_nodes_consecutive_images(self):
        """Test handling consecutive images"""
        node = TextNode("![one](1.png)![two](2.png)", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "one")
        self.assertEqual(result[1].text, "two")

    def test_split_nodes_with_non_text_nodes(self):
        """Test that non-TEXT nodes are preserved"""
        nodes = [
            TextNode("![img](test.png)", TextType.TEXT),
            TextNode("Bold", TextType.BOLD),
            TextNode("![img2](test2.png)", TextType.TEXT)
        ]
        result = split_nodes_image(nodes)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[1].text_type, TextType.BOLD)

    def test_image_with_empty_alt_text(self):
        """Test handling images with empty alt text"""
        text = "![](empty.png)"
        matches = extract_markdown_images(text)
        self.assertEqual(matches[0], ("", "empty.png"))

    def test_image_with_spaces(self):
        """Test handling images with spaces in alt text and URL"""
        text = "![Alt text with spaces](/path/to/image with spaces.jpg)"
        matches = extract_markdown_images(text)
        self.assertEqual(matches[0], ("Alt text with spaces", "/path/to/image with spaces.jpg"))

    def test_invalid_image_syntax(self):
        """Test handling invalid image markdown syntax"""
        text = "![missing](] and ![missing too"
        matches = extract_markdown_images(text)
        self.assertEqual(len(matches), 0)

    def test_links_vs_images(self):
        """Test distinguishing between links and images"""
        text = "[link](url.com) and ![image](img.png)"
        image_matches = extract_markdown_images(text)
        link_matches = extract_markdown_links(text)
        self.assertEqual(len(image_matches), 1)
        self.assertEqual(len(link_matches), 1)
        self.assertEqual(image_matches[0][1], "img.png")
        self.assertEqual(link_matches[0][1], "url.com")

    def test_split_nodes_empty_text(self):
        """Test splitting nodes with empty text"""
        node = TextNode("", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(len(result), 0)
    def test_split_nodes_link_basic(self):
   
        node = TextNode("Here's a [link](https://example.com)", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "Here's a ")
        self.assertEqual(result[1].text, "link")
        self.assertEqual(result[1].url, "https://example.com")
        self.assertEqual(result[1].text_type, TextType.LINK)

def test_split_nodes_multiple_links(self):
    """Test handling multiple links in text"""
    node = TextNode(
        "Start [link1](url1.com) middle [link2](url2.com) end", 
        TextType.TEXT
    )
    result = split_nodes_link([node])
    self.assertEqual(len(result), 5)
    self.assertEqual(result[1].text, "link1")
    self.assertEqual(result[1].url, "url1.com")
    self.assertEqual(result[3].text, "link2")
    self.assertEqual(result[3].url, "url2.com")

def test_split_nodes_link_with_non_text_nodes(self):
    """Test that non-TEXT nodes are preserved"""
    nodes = [
        TextNode("[link](url.com)", TextType.TEXT),
        TextNode("Bold", TextType.BOLD),
        TextNode("[another](url2.com)", TextType.TEXT)
    ]
    result = split_nodes_link(nodes)
    self.assertEqual(len(result), 3)
    self.assertEqual(result[1].text_type, TextType.BOLD)

def test_split_nodes_link_empty_text(self):
    """Test handling empty text nodes"""
    node = TextNode("", TextType.TEXT)
    result = split_nodes_link([node])
    self.assertEqual(len(result), 0)

def test_split_nodes_link_no_links(self):
    """Test text without any links"""
    node = TextNode("Plain text without links", TextType.TEXT)
    result = split_nodes_link([node])
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0].text, "Plain text without links")

def test_split_nodes_link_adjacent_links(self):
    """Test handling adjacent links"""
    node = TextNode(
        "[link1](url1.com)[link2](url2.com)", 
        TextType.TEXT
    )
    result = split_nodes_link([node])
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0].text, "link1")
    self.assertEqual(result[1].text, "link2")

def test_split_nodes_link_with_spaces(self):
    """Test links containing spaces"""
    node = TextNode(
        "[link with spaces](https://example.com/path with spaces)", 
        TextType.TEXT
    )
    result = split_nodes_link([node])
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0].text, "link with spaces")
    self.assertEqual(
        result[0].url, 
        "https://example.com/path with spaces"
    )

def test_split_nodes_link_complex_urls(self):
    """Test links with complex URLs"""
    node = TextNode(
        "[link](https://api.example.com/v1?query=test&page=1#section)", 
        TextType.TEXT
    )
    result = split_nodes_link([node])
    self.assertEqual(len(result), 1)
    self.assertEqual(
        result[0].url, 
        "https://api.example.com/v1?query=test&page=1#section"
    )

def test_split_nodes_link_preserve_surrounding_text(self):
    """Test preservation of text around links"""
    node = TextNode(
        "Before [link](url.com) after", 
        TextType.TEXT
    )
    result = split_nodes_link([node])
    self.assertEqual(len(result), 3)
    self.assertEqual(result[0].text, "Before ")
    self.assertEqual(result[2].text, " after")
  







if __name__ == "__main__":
    unittest.main()