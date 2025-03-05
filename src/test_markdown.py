import unittest

from markdown_extraction import extract_markdown_links, extract_markdown_images


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

    def test_nested_brackets(self):
        """Test handling of nested brackets"""
        text = "[Link with [brackets]](https://example.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual([
            ("Link with [brackets]", "https://example.com")
        ], matches)









if __name__ == "__main__":
    unittest.main()