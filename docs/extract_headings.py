import re


def extract_headers(markdown_text):
    headers = []
    lines = markdown_text.split('\n')
    header_pattern = re.compile(r'^(#+)\s+(.*)')

    for line in lines:
        match = header_pattern.match(line)
        if match:
            headers.append((match.group(1).count('#'), match.group(2)))

    return headers


if __name__ == "__main__":
    # Lies den Inhalt der Markdown-Datei
    with open('endpoint_schema.md', 'r') as file:
        markdown_text = file.read()

    headers = extract_headers(markdown_text)

    for level, header in headers:
        print(f"{'#' * level} {header}")
