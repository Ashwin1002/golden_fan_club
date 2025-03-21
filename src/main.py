from textnode import TextNode, TextType

from htmlhelper import extract_markdown_images, extract_markdown_links

def main():
    print("hello world")

    text_node_1 = TextNode("This is some anchor text", TextType.BOLD, "https://www.boot.dev")

    print(text_node_1)

    text : str = "This is text with a " \
    "![rick roll](https://i.imgur.com/aKaOqIh.gif) and " \
    "![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) " \
    "(hello)"

    text2 = "This is text with a link " \
    "[to boot dev](https://www.boot.dev) and " \
    "[to youtube](https://www.youtube.com/@bootdotdev)"

    print(extract_markdown_images(text))
    print(extract_markdown_links(text2))

if __name__ == "__main__":
    main()