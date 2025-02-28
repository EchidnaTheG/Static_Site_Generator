from textnode import TextType, TextNode

def main():
    test= TextNode("This is text node", TextType.BOLD,"https://www.boot.dev")
    print(test)

if __name__ == "__main__":
    main()