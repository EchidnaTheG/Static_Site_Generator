import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq_props(self):
        node = HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node, node2)
    
    def test_not_eq_props(self):
        node = HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode(props={"href": "https://www.google.com","target": "blank",})
        self.assertNotEqual(node, node2)

    def test_eqtext(self):
        node = HTMLNode("h1","Welcome to My Website!", props={"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("h1","WELcome to My Website!", props={"href": "https://www.google.com","target": "_blank",})
        self.assertNotEqual(node.value, node2.value)

    def test_different_url(self):
        node = HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode(props={"href": "https://www.boot.dev/lessons/","target": "_blank",})
        self.assertNotEqual(node, node2)

    def test_ulrnone(self):
        node = HTMLNode("h1","Welcome to My Website!")
        self.assertEqual(node.props, None)
    
if __name__ == "__main__":
    unittest.main()