import unittest

from htmlnode import HTMLNode, LeafNode

class TestHtmlNode(unittest.TestCase):
    
    def test_props_to_html(self):
        node = HTMLNode("a", "This is a paragraph", props={"href": "https://www.boot.dev"})
        self.assertEqual(node.props_to_html(), 'href="https://www.boot.dev"')
    
    def test_props_to_html_empty(self):
        node = HTMLNode("a", "This is a paragraph")
        self.assertEqual(node.props_to_html(), "")
    
    def test_empty_tag(self):
        node = HTMLNode()
        self.assertEqual(node.tag, "")
    
    def test_empty_value(self):
        node = HTMLNode()
        self.assertEqual(node.value, "")
    
    def test_empty_children(self):
        node = HTMLNode()
        self.assertEqual(node.children, [])
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
if __name__ == "__main__":
    unittest.main()