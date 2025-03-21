from textnode import TextNode, TextType
from htmlnode import LeafNode

import re

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode("", text_node.text)
            pass
        case TextType.BOLD:
            return LeafNode( "b", text_node.text)
            pass
        case TextType.ITALIC:
            return LeafNode( "i", text_node.text)
            pass
        case TextType.CODE:
            return LeafNode( "code", text_node.text)
        case TextType.LINK:
            return LeafNode( "a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("", "img", text_node.text, {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("invalid TextType")
    return None

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        parts = node.text.split(delimiter)
        for i, part in enumerate(parts):
            node_type = text_type if i % 2 == 1 else TextType.TEXT
            new_nodes.append(TextNode(part, node_type))
    
    return new_nodes

def extract_markdown_images(text: str):
    matches = re.findall(r"\!\[(.*?)\]+\((https?://[^\s]+\.*?)\)", text)
    return matches

def extract_markdown_links(text: str):
    matches = re.findall(r"\[(.*?)\]+\((https?://[^\s]+\.*?)\)", text)
    return matches