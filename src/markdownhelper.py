from enum import Enum
from htmlnode import HTMLNode

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
    if ["#", "##", "###", "####", "#####", "######"].count(block[:block.index(" ")]) > 0 and block[block.index(" ") + 1] != "#":
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith("- "):
        return BlockType.UNORDERED_LIST
    elif block.startswith("1. "):    
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    
def markdown_to_html_node(markdown: str):
    html_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.HEADING:
                count = block.count("#")
                header_block = block.replace(f"{"#" * count} ", "").strip()
                html_nodes.append(HTMLNode(f"h{count}", header_block))
            case BlockType.CODE:
                code_block = block.replace("```", "").strip()
                html_nodes.append(HTMLNode("code", code_block))
            case BlockType.QUOTE:
                quote_block = block.replace(">", "").strip()
                html_nodes.append(HTMLNode("blockquote", quote_block))
            case BlockType.ORDERED_LIST:
                list_items = block.split("\n")
                list_items = [item.replace(f"{list_items.index(item) + 1}. ", "").strip() for item in list_items]
                html_nodes.append(HTMLNode("ol", list_items))
            case BlockType.UNORDERED_LIST:
                list_items = block.split("\n")
                list_items = [item.replace("- ", "").strip() for item in list_items]
                html_nodes.append(HTMLNode("ul", list_items))
            case _:
                html_nodes.append(HTMLNode("p", block))
                pass
        
        return html_nodes


def text_to_children(text: str):
    pass