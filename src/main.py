from textnode import TextNode, TextType
from markdown_blocks import markdown_to_html_node
import os
import shutil

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        if os.path.isdir(from_path):
            dest_path = os.path.join(dest_dir_path, filename)
        else:
            dest_path = os.path.join(dest_dir_path, os.path.splitext(filename)[0] + ".html")
        if os.path.isfile(from_path):
            generate_page(from_path, template_path, dest_path)
        else:
            generate_page_recursive(from_path, template_path, dest_path)

def extract_title(markdown):
    header = markdown.split("\n\n")[0]
    if header[0:2] != "# ":
        raise Exception("Title must be the first line of the file and must start with #")
    
    return header

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")
    # read the markdown file
    with open(from_path, "r") as file:
        markdown = file.read()
        file.close()
    # read template file
    with open(template_path, "r") as file:
        template = file.read()
        file.close()
    # convert markdown to html
    html = markdown_to_html_node(markdown).to_html()
    # extract title
    title = extract_title(markdown)
    # replace title and content in template
    template = template.replace("{{ Title }}", title)
    new_html = template.replace("{{ Content }}", html)
    # write to destination
    with open(dest_path, "w") as file:
        file.write(new_html)

def main():
    # deleting the public directory and copying the static directory
    source = "static"
    destination = "public"
    copy_files_recursive(source,destination)

    # generating the index page
    generate_page_recursive("content", "template.html", "public")


main()
