from enum import Enum
from htmlnode import *
from textnode import TextNode
from htmlhelper import text_to_textnodes
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    QUOTE = "quote"
    CODE = "code"
    ORDERED_LIST = "ordered_list"
    UNORDERED_LIST = "unordered_list"

def markdown_to_blocks(markdown: str):
    markdowns = markdown.split("\n\n")
    markdowns = ["\n".join([m.strip() for m in markdown.strip().split("\n")]) for markdown in markdowns if  markdown.strip() != ""]
    return markdowns

def block_to_block_type(block: str) -> BlockType:
    if block.startswith("#"):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith(("- ", "* ")):
        return BlockType.UNORDERED_LIST
    elif re.match(r"\d+\. ", block):    
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    
def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    root = HTMLNode("div", children=[])
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.HEADING:
                count = block.count("#")
                header_block = block.replace(f"{"#" * count} ", "").strip()
                node = HTMLNode(f"h{count}", children=[text_to_children(header_block)])
            case BlockType.CODE:
                code_text = block.strip('`\n')
                code_node = HTMLNode("code", children=[TextNode(code_text)])
                node = HTMLNode("pre", children=[code_node])
            case BlockType.QUOTE:
                quote_block = block.replace(">", "").strip()
                node = HTMLNode("blockquote", quote_block)
            case BlockType.ORDERED_LIST:
                list_items = block.split("\n")
                list_items = [item.replace(f"{list_items.index(item) + 1}. ", "").strip() for item in list_items]
                node = HTMLNode("ol", children=[HTMLNode("li", l) for l in list_items])
            case BlockType.UNORDERED_LIST:
                list_items = block.split("\n")
                list_items = [item.replace("- ", "").strip() for item in list_items]
                node = HTMLNode("ul", children=[HTMLNode("li", l) for l in list_items])
            case _:
                node = HTMLNode("p", children=[text_to_children(block)])
                pass

        root.children.append(node)
    
    return root


def text_to_children(text: str) -> list[TextNode]:
    return text_to_textnodes(text)