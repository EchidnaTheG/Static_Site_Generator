    def test_split_nodes_multiple_links(self):
        """Test handling multiple links in text"""
        node = TextNode(
            "Start [link1](url1.com) middle [link2](url2.com) end", 
            TextType.TEXT
        )
        result = split_nodes_link([node])
        self.assertEqual(len(result), 5)
        self.assertEqual(result[1].text, "link1")
        self.assertEqual(result[1].url, "url1.com")
        self.assertEqual(result[3].text, "link2")
        self.assertEqual(result[3].url, "url2.com")

    def test_split_nodes_link_with_non_text_nodes(self):
        """Test that non-TEXT nodes are preserved"""
        nodes = [
            TextNode("[link](url.com)", TextType.TEXT),
            TextNode("Bold", TextType.BOLD),
            TextNode("[another](url2.com)", TextType.TEXT)
        ]
        result = split_nodes_link(nodes)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[1].text_type, TextType.BOLD)

    def test_split_nodes_link_empty_text(self):
        """Test handling empty text nodes"""
        node = TextNode("", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(len(result), 0)

    def test_split_nodes_link_no_links(self):
        """Test text without any links"""
        node = TextNode("Plain text without links", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "Plain text without links")

    def test_split_nodes_link_adjacent_links(self):
        """Test handling adjacent links"""
        node = TextNode(
            "[link1](url1.com)[link2](url2.com)", 
            TextType.TEXT
        )
        result = split_nodes_link([node])
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "link1")
        self.assertEqual(result[1].text, "link2")

    def test_split_nodes_link_with_spaces(self):
        """Test links containing spaces"""
        node = TextNode(
            "[link with spaces](https://example.com/path with spaces)", 
            TextType.TEXT
        )
        result = split_nodes_link([node])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "link with spaces")
        self.assertEqual(
            result[0].url, 
            "https://example.com/path with spaces"
        )

    def test_split_nodes_link_complex_urls(self):
        """Test links with complex URLs"""
        node = TextNode(
            "[link](https://api.example.com/v1?query=test&page=1#section)", 
            TextType.TEXT
        )
        result = split_nodes_link([node])
        self.assertEqual(len(result), 1)
        self.assertEqual(
            result[0].url, 
            "https://api.example.com/v1?query=test&page=1#section"
        )

    def test_split_nodes_link_preserve_surrounding_text(self):
        """Test preservation of text around links"""
        node = TextNode(
            "Before [link](url.com) after", 
            TextType.TEXT
        )
        result = split_nodes_link([node])
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Before ")
        self.assertEqual(result[2].text, " after")

    def test_text_to_textnodes_basic(self):
        """Test basic text conversion"""
        nodes = text_to_textnodes("Plain text")
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "Plain text")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

    def test_text_to_textnodes_bold(self):
        """Test bold text conversion"""
        nodes = text_to_textnodes("This is **bold** text")
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " text")

    def test_text_to_textnodes_italic(self):
        """Test italic text conversion"""
        nodes = text_to_textnodes("This is _italic_ text")
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[1].text, "italic")
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)

    def test_text_to_textnodes_code(self):
        """Test code block conversion"""
        nodes = text_to_textnodes("Here is `code` block")
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[1].text, "code")
        self.assertEqual(nodes[1].text_type, TextType.CODE)

    def test_text_to_textnodes_links(self):
        """Test link conversion"""
        nodes = text_to_textnodes("Here's a [link](https://example.com)")
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[1].text, "link")
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[1].url, "https://example.com")

    def test_text_to_textnodes_images(self):
        """Test image conversion"""
        nodes = text_to_textnodes("Here's an ![image](image.jpg)")
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[1].text, "image")
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(nodes[1].url, "image.jpg")

    def test_text_to_textnodes_mixed(self):
        """Test mixed content conversion"""
        text = "This is **bold** with an ![image](img.jpg) and _italic_"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 6)
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[3].text_type, TextType.IMAGE)
        self.assertEqual(nodes[5].text_type, TextType.ITALIC)

    def test_text_to_textnodes_nested_formats(self):
        """Test handling of nested formatting"""
        nodes = text_to_textnodes("**Bold _italic_**")
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text_type, TextType.BOLD)

    def test_text_to_textnodes_empty(self):
        """Test empty string handling"""
        nodes = text_to_textnodes("")
        self.assertEqual(len(nodes), 0)

    def test_text_to_textnodes_multiple_similar(self):
        """Test multiple instances of same formatting"""
        nodes = text_to_textnodes("**bold** normal **bold**")
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text_type, TextType.BOLD)
        self.assertEqual(nodes[1].text_type, TextType.TEXT)
        self.assertEqual(nodes[2].text_type, TextType.BOLD)


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

    def test_markdown_to_blocks_basic(self):
        """Test basic block separation"""
        markdown = "This is paragraph 1\n\nThis is paragraph 2"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 2)
        self.assertEqual(blocks[0], "This is paragraph 1")
        self.assertEqual(blocks[1], "This is paragraph 2")

    def test_markdown_to_blocks_multiple_newlines(self):
        """Test handling of multiple newlines"""
        markdown = "Paragraph 1\n\n\n\nParagraph 2"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 2)
        self.assertEqual(blocks[0], "Paragraph 1")
        self.assertEqual(blocks[1], "Paragraph 2")

    def test_markdown_to_blocks_with_lists(self):
        """Test handling of markdown lists"""
        markdown = "# Header\n\n* List item 1\n* List item 2\n\nParagraph"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(blocks[0], "# Header")
        self.assertEqual(blocks[1], "* List item 1\n* List item 2")
        self.assertEqual(blocks[2], "Paragraph")

    def test_markdown_to_blocks_with_code(self):
        """Test handling of code blocks"""
        markdown = "Text\n\n```\ncode block\nmore code\n```\n\nMore text"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(blocks[1], "```\ncode block\nmore code\n```")

    def test_markdown_to_blocks_empty_string(self):
        """Test handling of empty string"""
        blocks = markdown_to_blocks("")
        self.assertEqual(len(blocks), 0)

    def test_markdown_to_blocks_only_whitespace(self):
        """Test handling of whitespace-only input"""
        markdown = "   \n\n   \n\n   "
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 0)

    def test_markdown_to_blocks_single_paragraph(self):
        """Test handling of single paragraph"""
        markdown = "Just one paragraph"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0], "Just one paragraph")

    def test_markdown_to_blocks_preserve_indentation(self):
        """Test preservation of indentation within blocks"""
        markdown = "Normal text\n\n    Indented text\n    Still indented"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 2)
        self.assertEqual(blocks[1], "    Indented text\n    Still indented")
