from htmlnode import ParentNode, LeafNode
from markdown_blocks import *
from markdown_inline import *

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")
    # read the markdown file
    with open(from_path, "r") as file:
        markdown = file.read()
    # read template file
    with open(template_path, "r") as file:
        template = file.read()
    # convert markdown to html

    pass

def test(markdown):
    html = markdown_to_html_node(markdown).to_html()
    # extract title
    title = extract_title(markdown)
    # replace title and content in template
    template = """<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title> {{ Title }} </title>
    <link href="/index.css" rel="stylesheet">
</head>

<body>
    <article>
        {{ Content }}
    </article>
</body>

</html>"""
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    return template

print(test("""# Tolkien Fan Club

**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)

> All that is gold does not glitter

## Reasons I like Tolkien

* You can spend years studying the legendarium and still not understand its depths
* It can be enjoyed by children and adults alike
* Disney *didn't ruin it*
* It created an entirely new genre of fantasy

## My favorite characters (in order)

1. Gandalf
2. Bilbo
3. Sam
4. Glorfindel
5. Galadriel
6. Elrond
7. Thorin
8. Sauron
9. Aragorn

Here's what `elflang` looks like (the perfect coding language):

```
func main(){
    fmt.Println("Hello, World!")
}
```"""))