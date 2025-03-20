import unittest

from textnode import TextNode, Bender


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", Bender.AIR_BENDER)
        node2 = TextNode("This is a text node", Bender.AIR_BENDER)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", Bender.AIR_BENDER)
        node2 = TextNode("This is a text node", Bender.WATER_BENDER)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", Bender.AIR_BENDER)
        self.assertIsNone(node.url)
    
    def test_url_not_none(self):
        node = TextNode("This is a text node", Bender.AIR_BENDER, "https://www.boot.dev")
        self.assertIsNotNone(node.url)

if __name__ == "__main__":
    unittest.main()