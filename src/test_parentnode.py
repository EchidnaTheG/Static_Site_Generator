import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_Parent_to_html_p(self):
        node = ParentNode( "p", [ LeafNode("b", "Bold text"),  LeafNode(None, "Normal text"),  LeafNode("i", "italic text"),   LeafNode(None, "Normal text")])        
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grand_grand_children(self):
        grandgrandchild_node = LeafNode("b", "grandchild")
        grandchild_node = ParentNode("span", [grandgrandchild_node])
        child_node = ParentNode("div", [grandchild_node])
        parent_node = ParentNode("body", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<body><div><span><b>grandchild</b></span></div></body>",
        )
    def test_Parent_to_html_p_with_props(self):
        node = ParentNode( "a", [ LeafNode("b", "Bold text")],props={"href":"https://www.google.com"})        
        self.assertEqual(node.to_html(), r'<a href="https://www.google.com"><b>Bold text</b></a>')

    def test_error_case_None_Tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None,[ LeafNode("b", "Bold text")],props={"href":"https://www.google.com"})
            node.to_html()
    
    def test_error_case_none_children(self):
        with self.assertRaises(ValueError):
            node= ParentNode("html",None)
            node.to_html()

    def test_error_case_missing_children(self):
        with self.assertRaises(ValueError):
            node= ParentNode("html",[])
            node.to_html()
    





if __name__ == "__main__":
    unittest.main()