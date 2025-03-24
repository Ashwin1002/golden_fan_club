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

def split_nodes_images(old_nodes) -> TextNode:
    new_nodes = []
    image_pattern = re.compile(r'!\[(.*?)\]\((https?://[^)]+)\)')
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        parts = []
        last_end = 0
        
        for match in image_pattern.finditer(node.text):
            parts.append(TextNode(node.text[last_end:match.start()], TextType.TEXT))
            parts.append(TextNode(match.group(1), TextType.IMAGE, match.group(2)))
            last_end = match.end()
        
        parts.append(TextNode(node.text[last_end:], TextType.TEXT))
        new_nodes.extend(filter(lambda x: x.text, parts))
    
    return new_nodes

def split_nodes_links(old_nodes) -> TextNode:
    new_nodes = []
    link_pattern = re.compile(r'\[(.*?)\]\((https?://[^)]+)\)')
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        parts = []
        last_end = 0
        
        for match in link_pattern.finditer(node.text):
            parts.append(TextNode(node.text[last_end:match.start()], TextType.TEXT))
            parts.append(TextNode(match.group(1), TextType.LINK, match.group(2)))
            last_end = match.end()
        
        parts.append(TextNode(node.text[last_end:], TextType.TEXT))
        new_nodes.extend(filter(lambda x: x.text, parts))
    
    return new_nodes

def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_links(nodes)
    return nodes

