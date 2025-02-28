import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_noteqtype(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_only_eqtext(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node.text, node2.text)
        
    def test_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://different.com")
        self.assertNotEqual(node, node2)

    def test_ulrnone(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)
    
    def test_TextNode_to_LeafNode_Invalid_Type(self):
          with self.assertRaises(ValueError):
            node = TextNode("This is a text node", "INVALID")
            node.text_node_to_html_node()

    def test_TextNode_to_LeafNode_Text(self):
            node = TextNode("This is a text node", TextType.TEXT)
            html_node = node.text_node_to_html_node()
            self.assertEqual(html_node.tag, None)
            self.assertEqual(html_node.value, "This is a text node")

    def test_TextNode_to_LeafNode_Bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")


    def test_TextNode_to_LeafNode_Italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")


    def test_TextNode_to_LeafNode_Code(self):
        node = TextNode("print('hello')", TextType.CODE)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('hello')")


    def test_TextNode_to_LeafNode_Link(self):
        node = TextNode("Click here", TextType.LINK, "https://example.com")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props, {"href": "https://example.com"})


    def test_TextNode_to_LeafNode_Image(self):
        node = TextNode("An image description", TextType.IMAGE, "https://example.com")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {'src': 'https://example.com', 'alt': 'An image description'})
if __name__ == "__main__":
    unittest.main()