import unittest

from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = ParentNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")