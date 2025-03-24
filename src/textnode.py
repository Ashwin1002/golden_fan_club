from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a href"
    IMAGE = "img src"


def text_to_text_type(text: str) -> TextType:
    if text.startswith("**") and text.endswith("**"):
        return TextType.BOLD
    elif text.startswith("_") and text.endswith("_"):
        return TextType.ITALIC
    elif text.startswith("`") and text.endswith("`"):
        return TextType.CODE
    elif text.startswith("[") and text.endswith("]"):
        return TextType.LINK
    elif text.startswith("![") and text.endswith(")"):
        return TextType.IMAGE
    else:
        return TextType.TEXT

class TextNode:
    def __init__(self, text: str, text_type: TextType, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return (
            self.text == other.text and 
            self.text_type == other.text_type and 
            self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"