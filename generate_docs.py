import os

def generate_stub(filepath, output_dir):
    """Generates a markdown stub file for a given file."""
    # Create the mirrored directory structure
    relative_path = os.path.relpath(filepath, ".")
    output_filepath = os.path.join(output_dir, relative_path + ".md")
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)

    # Define the content for the stub file
    content = f"""# {relative_path}

## Purpose
[Briefly describe the purpose of this file]

## Key APIs
[List key classes, functions, or variables with brief descriptions.
For C++ files, consider adding Doxygen markers for later extraction.
For Python files, consider using Sphinx autodoc.]

## Dependencies
[List any major files or modules this file depends on]

## Usage Examples
[Provide small, illustrative code snippets demonstrating how to use the key APIs]

## Implementation Notes
[Any important details, design choices, or potential gotchas]

## Source Link
[{relative_path}](link_to_source_repository/{relative_path})
"""

    # Write the content to the stub file
    with open(output_filepath, "w") as f:
        f.write(content)

def generate_documentation_stubs(project_dir, output_dir):
    """Generates documentation stubs for all files in the project directory."""
    print(f"Generating documentation stubs in {output_dir}...")
    for root, _, files in os.walk(project_dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            generate_stub(filepath, output_dir)
    print("Documentation stub generation complete.")

if __name__ == "__main__":
    project_directory = "."  # Replace with your project's root directory
    output_directory = "docs/modules"  # Replace with your desired output directory

    generate_documentation_stubs(project_directory, output_directory)
