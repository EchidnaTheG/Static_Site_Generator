class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag= tag
        self.value = value
        self.children = children
        self.props = props
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        
    def to_html(self):
        raise NotImplementedError("Error!")

    def props_to_html(self):
        if self.props == None:
            return ""
        string_representation=""
        for key, value in self.props.items():
            string_representation += " " + key + "=" + fr'"{value}"' + " "
        print(string_representation) 
        return string_representation
    
x= HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
x.props_to_html()
print(x)
