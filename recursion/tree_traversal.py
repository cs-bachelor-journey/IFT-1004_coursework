# simple file system tree and calculate the total size of all files

class FileNode:
    def __init__(self, name, size=0, children=None):
        self.name = name
        self.size = size # 0 for folders
        self.children = children or []
        

def total_size(node: FileNode):
    # Base case: it's a file (no children)
    if not node.children:
        return node.size
    
    # Recursive case: sum this node's size + all children's sizes
    return node.size + sum(total_size(child) for child in node.children)

# Build a small file tree 
project = FileNode("project", children=[
    FileNode("src", children=[
        FileNode("main.py", size=12400),
        FileNode("utils.py", size=5800),
    ]),
    FileNode("data", children=[
        FileNode("sales_jan.parquet", size=302914),
        FileNode("sales_feb.parquet", size=289000),
    ]),
    FileNode("README.md", size=3200)
])

print(f"Total project size: {total_size(project):,} bytes")
print(f"Source files only: {total_size(project.children[0]):,} bytes")