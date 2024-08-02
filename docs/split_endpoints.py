import re
import os
import logging


def extract_sections(markdown_text):
    """
    Extrahiert Sektionen und deren Inhalt aus einem Markdown-Text basierend auf Überschriften der Ebene 2.

    :param markdown_text: Der gesamte Markdown-Text als String.
    :return: Eine Liste von Tupeln, wobei jedes Tupel die Sektion und den entsprechenden Inhalt enthält.
    """
    section_pattern = re.compile(r'(## .+?)\n(.*?)(?=## |\Z)', re.DOTALL)
    sections = section_pattern.findall(markdown_text)
    return sections


def sanitize_filename(name):
    """
    Ersetzt ungültige Zeichen in Dateinamen durch Unterstriche.

    :param name: Der ursprüngliche Name.
    :return: Der bereinigte Name.
    """
    return re.sub(r'[\\/*?:"<>|]', '_', name)


def save_section_files(sections, base_path):
    """
    Speichert jede Sektion und deren Endpunkte in separate Dateien.

    :param sections: Eine Liste von Tupeln, wobei jedes Tupel die Sektion und den entsprechenden Inhalt enthält.
    :param base_path: Der Basis-Pfad, in dem die Dateien gespeichert werden.
    """
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    for section_title, section_content in sections:
        section_name = section_title.replace(
            '## ', '').strip().replace(' ', '_').lower()
        section_name = sanitize_filename(section_name)
        file_path = os.path.join(base_path, f"{section_name}.md")

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"{section_title}\n{section_content}")

        logging.info(f'Saved section to {file_path}')


def main(markdown_file_path, base_path):
    """
    Hauptfunktion des Skripts.

    :param markdown_file_path: Der Pfad zur Markdown-Datei.
    :param base_path: Der Basis-Pfad, in dem die Dateien gespeichert werden.
    """
    logging.basicConfig(filename='section_extraction.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    with open(markdown_file_path, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    sections = extract_sections(markdown_text)
    logging.info(f'Found {len(sections)} sections in the markdown file.')

    save_section_files(sections, base_path)
    logging.info('All sections have been saved successfully.')


if __name__ == "__main__":
    markdown_file_path = 'endpoint_schema.md'  # Pfad zur Markdown-Datei
    base_path = 'sections_output'  # Basis-Pfad zum Speichern der Sektion-Dateien
    main(markdown_file_path, base_path)
