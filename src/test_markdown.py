import unittest

from markdownhelper import *

class TestMarkdown(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        md = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    

    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING) 
        block = "1. This is a heading\n2. This is a heading\n3. This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "- This is a heading\n- This is a heading\n- This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "> This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        block = "```python\nThis is a heading\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

if __name__ == "__main__":
    unittest.main( )