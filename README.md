# Static Site Generator

A Python-based static site generator that converts markdown content into HTML using a custom node-based architecture.

## Project Structure

```
Static_Site_Generator/
├── src/
│   ├── htmlnode.py
│   ├── leafnode.py
│   ├── test_htmlnode.py
│   └── test_leafnode.py
```

## Components

### HTMLNode
Base class that represents an HTML element with the following properties:
- `tag`: The HTML tag name (e.g., "p", "h1", "a")
- `value`: The content/text of the element
- `children`: Child nodes (None for leaf nodes)
- `props`: HTML attributes as a dictionary (e.g., {"class": "greeting"})

### LeafNode
Extends HTMLNode to represent elements without children (text nodes). Features:
- Inherits from HTMLNode
- Converts node properties to valid HTML attributes
- Handles special characters in content
- Supports empty tags and tagless text nodes

## Testing

The project includes comprehensive unit tests covering:
- HTML tag generation
- Property handling
- Edge cases (empty strings, None values)
- Special character handling
- Node equality comparison

To run the tests:
```bash
python -m unittest src/test_htmlnode.py
python -m unittest src/test_leafnode.py
```

## Usage Example

```python
from leafnode import LeafNode

# Create a link with properties
link = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
print(link.to_html())  # Output: <a href="https://www.google.com">Click me!</a>

# Create a simple paragraph
para = LeafNode("p", "Hello, world!")
print(para.to_html())  # Output: <p>Hello, world!</p>
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.