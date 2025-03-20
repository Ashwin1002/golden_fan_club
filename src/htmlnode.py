

class HTMLNode:
    def __init__(
            self, 
            tag: str = None,
            value: str = None, 
            children: list = None,
            props: dict = None
        ):
            self.tag = tag or ""
            self.value = value or ""
            self.children = children or []
            self.props = props or {}

    def to_html(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def props_to_html(self):
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
