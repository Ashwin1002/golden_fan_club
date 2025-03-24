from textnode import TextNode, TextType

from htmlhelper import split_nodes_links, text_to_textnodes

from markdownhelper import markdown_to_html_node

def main():
    print("hello world")

    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )
    print("\n".join([str(n) for n in split_nodes_links([node])]))

    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

    text_to_textnodes(text)

    md = """
        This is **bolded** paragraph
        text in a p
        tag here

        This is another paragraph with _italic_ text and `code` here

        """

    markdowns = markdown_to_html_node(md)

    print(markdowns)

if __name__ == "__main__":
    main()