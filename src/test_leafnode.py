import unittest

from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", " Hello, world!")
        self.assertEqual(node.to_html(), "<h1> Hello, world!</h1>")

    def test_leaf_to_html_h2_not_eq(self):
        node = LeafNode("h2", " Hello, world!")
        self.assertNotEqual(node.to_html(), "<h2> Hello, world!<h2>")

    def test_leaf_none_value(self):
     #Test that None value raises ValueError"""
      with self.assertRaises(ValueError):
        node = LeafNode("p", None)
        node.to_html()

    def test_leaf_no_tag(self):
        #Test node with no tag returns just the value"""
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_empty_string(self):
        #Test node with empty string value"""
        node = LeafNode("p", "")
        self.assertEqual(node.to_html(), "<p></p>")

    def test_leaf_equality(self):
        #Test equality comparison between leaf nodes"""
        node1 = LeafNode("p", "Hello", props={"class": "greeting"})
        node2 = LeafNode("p", "Hello", props={"class": "greeting"})
        node3 = LeafNode("p", "Hello", props={"class": "different"})
        self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node3)

    def test_special_characters(self):
        #Test handling of special characters"""
        node = LeafNode("p", "Hello & goodbye!")
        self.assertEqual(node.to_html(), "<p>Hello & goodbye!</p>")

    def test_leaf_with_props(self):
        #Test HTML generation with properties"""
        node = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
        
if __name__ == "__main__":
    unittest.main()