import unittest
from delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestDelimiter(unittest.TestCase):
    def test_empty_string(self):
        """Test handling of empty strings"""
        node = TextNode("", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(len(nodes), 0)

    def test_no_delimiters(self):
        """Test text without any delimiters"""
        node = TextNode("Plain text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "Plain text")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

    def test_multiple_delimiters(self):
        """Test handling multiple delimiter pairs"""
        node = TextNode("Hello *bold* normal *bold again*", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(len(nodes), 4)
        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " normal ")
        self.assertEqual(nodes[3].text, "bold again")
        self.assertEqual(nodes[3].text_type, TextType.BOLD)

    def test_multi_character_delimiter(self):
        """Test handling multi-character delimiters"""
        node = TextNode("Testing **bold** text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)

    def test_different_text_types(self):
        """Test handling different text types"""
        nodes = [
            TextNode("Normal `code` normal", TextType.TEXT),
            TextNode("Already bold", TextType.BOLD),
            TextNode("More `code` here", TextType.TEXT)
        ]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(len(result), 7)
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[3].text_type, TextType.BOLD)
        self.assertEqual(result[5].text_type, TextType.CODE)

    def test_mismatched_delimiters(self):
        """Test handling of mismatched delimiters"""
        node = TextNode("Mismatched *delimiter", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "*", TextType.BOLD)

    def test_adjacent_delimiters(self):
        """Test handling of adjacent delimiter pairs"""
        node = TextNode("**bold**_italic_", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].text, "bold")
        self.assertEqual(nodes[0].text_type, TextType.BOLD)


if __name__ == "__main__":
    unittest.main()