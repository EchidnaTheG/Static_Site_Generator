# Static Site Generator (Work in Progress) 🚧

A Python-based static site generator that converts markdown content into HTML using a custom node-based architecture. This project implements a tree-like structure for HTML generation with support for nested elements, text formatting, and attributes.

## 🏗️ Project Structure

```
Static_Site_Generator/
├── src/
│   ├── htmlnode.py      # Base HTML node class
│   ├── leafnode.py      # Terminal nodes (no children)
│   ├── parentnode.py    # Nodes that can have children
│   ├── textnode.py      # Text content with formatting
│   └── tests/
│       ├── test_htmlnode.py
│       ├── test_leafnode.py
│       ├── test_parentnode.py
│       └── test_textnode.py
```

## 🧱 Components

### HTMLNode
Base class providing core HTML element functionality:
- `tag`: HTML tag name (e.g., "p", "h1", "a")
- `value`: Node content/text
- `children`: Child nodes (None for leaf nodes)
- `props`: HTML attributes as dictionary

### LeafNode
Terminal nodes (no children):
```python
from leafnode import LeafNode

# Create a link
link = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
print(link.to_html())  # <a href="https://www.google.com">Click me!</a>
```

### ParentNode
Containers for other nodes:
```python
from parentnode import ParentNode
from leafnode import LeafNode

# Create a paragraph with bold text
bold = LeafNode("b", "Bold text")
para = ParentNode("p", [bold])
print(para.to_html())  # <p><b>Bold text</b></p>
```

### TextNode
Text content with formatting support:
```python
from textnode import TextNode, TextType

# Create formatted text
text = TextNode("Hello", TextType.BOLD)
node = text.text_node_to_html_node()
print(node.to_html())  # <b>Hello</b>
```

## 🧪 Testing

The project uses Python's unittest framework. Each component has its own test suite covering:
- Basic HTML generation
- Nested elements
- Attribute handling
- Edge cases
- Type validation

Run tests with:
```bash
# Run all tests
python -m unittest discover src/tests

# Run specific test file
python -m unittest src/tests/test_htmlnode.py
```

## 🚧 Current Status

This project is actively under development. Current features:
- [x] Basic HTML node structure
- [x] Leaf node implementation
- [x] Parent node with children
- [x] Text formatting
- [ ] Markdown parsing
- [ ] Full document generation
- [ ] CSS support
- [ ] Template system

# 🚀 Future Ideas & Enhancements for Static Site Generator

This document outlines ambitious, next-level ideas for the project—features that aim to make the generator both incredibly useful and mind-blowingly impressive.

---

## 1. Distributed & Serverless Deployment

### Idea: A Static Site Generator That Deploys Instantly, Globally, and Offline

- **Built-in IPFS Deployment:** Automatically deploy generated sites on a decentralized network.
- **Zero-Config Edge Computing:** Integrate with Cloudflare Workers or Vercel Edge Functions for lightning-fast global deployment.
- **Self-Hosting P2P Mode:** Serve sites directly from the user's browser without a traditional server.
- **Offline-First Websites:** Use service workers and local caching to ensure full functionality even when offline.

---

## 2. Interactive Static Sites Without Traditional JavaScript

### Idea: A Static Site Generator with AI Automation & Smart Components

- **AI-Generated Content:** Integrate with a language model (e.g., GPT) to convert bullet points into full, SEO-friendly content.
- **Smart Components:** Utilize Web Components or WASM to implement dynamic features without relying on heavy JavaScript frameworks.
- **Self-Updating Content:** Automatically pull updates from RSS feeds, APIs, or AI prompts to regenerate pages on the fly.

---

## 3. A New, Human-Friendly Markup Language

### Idea: A More Powerful, Readable Alternative to Markdown

- **Custom Syntax:** Develop a new markup language (e.g., "HyperMD") that improves on Markdown's readability and expressiveness.
- **Built-In Component Support:** Allow native support for advanced layouts, interactivity, and AI-generated content.
- **Example Syntax:**

  ```hypermd
  # Welcome to My Blog

  [HeroImage src="banner.jpg" alt="Beautiful banner"]

  [Button link="subscribe.html"] Subscribe Now [/Button]

  [AIContent prompt="Write a short paragraph about why programming is awesome."]

  ```
  
## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

[MIT](https://choosealicense.com/licenses/mit/)