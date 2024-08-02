import re
import json
import logging


def extract_json_blocks(markdown_text):
    """
    Extrahiert JSON-Codeblöcke aus einem Markdown-Text.

    :param markdown_text: Der gesamte Markdown-Text als String.
    :return: Eine Liste von JSON-Codeblöcken.
    """
    json_blocks = re.findall(r'```json(.*?)```', markdown_text, re.DOTALL)
    return [block.strip() for block in json_blocks]


def check_json_blocks(json_blocks):
    """
    Überprüft JSON-Codeblöcke auf Fehler.

    :param json_blocks: Eine Liste von JSON-Codeblöcken.
    :return: Eine Liste von Fehlern.
    """
    errors = []
    for i, block in enumerate(json_blocks):
        try:
            json.loads(block)
        except json.JSONDecodeError as e:
            errors.append((i+1, str(e)))
    return errors


def main(markdown_file_path):
    """
    Hauptfunktion des Skripts.

    :param markdown_file_path: Der Pfad zur Markdown-Datei.
    """
    logging.basicConfig(filename='json_check.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    with open(markdown_file_path, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    json_blocks = extract_json_blocks(markdown_text)
    logging.info(f'Found {len(json_blocks)} JSON blocks in the markdown file.')

    errors = check_json_blocks(json_blocks)
    if errors:
        logging.error(f'Found {len(errors)} errors in JSON blocks.')
        for block_num, error in errors:
            logging.error(f'Error in JSON block {block_num}: {error}')
            print(f'Error in JSON block {block_num}: {error}')
    else:
        logging.info('No errors found in JSON blocks.')
        print('No errors found in JSON blocks.')


if __name__ == "__main__":
    markdown_file_path = 'endpoint_schema.md'  # Pfad zur Markdown-Datei
    main(markdown_file_path)
