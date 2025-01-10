import json

# File paths
json_file_path = 'html_tags.json'
readme_format_path = 'README-format.md'
readme_output_path = 'README.md'

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def read_template(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def generate_table(tags):
    table_header = "| Tag Name      | Brief Description         | Learn More Link                 |\n"
    table_header += "|---------------|---------------------------|---------------------------------|\n"

    table_rows = ""
    for tag in tags:
        table_rows += f"| `{tag['name']}` | {tag['brief']} | [Learn More]({tag['link']}) |\n"

    return table_header + table_rows

def write_readme(output_path, template, table):
    readme_content = template.replace("| `<tag_name>`  | Brief description here... | [Learn More](https://example.com) |", table)
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(readme_content)

def main():
    tags = read_json(json_file_path)
    template = read_template(readme_format_path)
    table = generate_table(tags)
    write_readme(readme_output_path, template, table)
    print(f"README.md has been successfully updated!")

if __name__ == "__main__":
    main()
