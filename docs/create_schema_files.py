import os
import json
import re

# Definiere die Hauptkategorien und ihre jeweiligen Endpunkte
categories = {
    "Applications": {
        "/applications": ["GET", "POST"],
        "/applications/externalId=_externalId": ["GET"],
        "/applications_id": ["GET", "PUT"],
        "/applications_id_/delete": ["POST"],
        "/applications_id_/statusChange/_statusId": ["POST"],
        "/applications_id_/jobOpeningMove/_jobOpeningId": ["POST"],
        "/applications_id_/attachments": ["GET", "POST"],
        "/applications_id_/attachments/_attachmentId": ["GET"],
        "/applications_id_/attachments/_attachmentId_/pdf": ["GET"],
        "/applications_id_/attachments/_attachmentId_/delete": ["POST"],
        "/applications_id_/history": ["GET", "PUT"],
        "/applications_id_/history/_externalId": ["PUT"]
    },
    "Configuration": {
        "/configuration/_type_/externalLinks": ["GET", "PUT"]
    },
    "Hiring requests": {
        "/hiringRequests": ["GET", "POST"],
        "/hiringRequests/externalId=_externalId": ["GET"],
        "/hiringRequests_id": ["GET", "PUT"],
        "/hiringRequests_id_/history": ["GET"],
        "/hiringRequests_id_/approvers": ["GET"]
    },
    "Job openings": {
        "/jobOpenings": ["GET", "POST"],
        "/jobOpenings/externalId=_externalId": ["GET"],
        "/jobOpenings_id": ["GET", "PUT"],
        "/jobOpenings_id_/history": ["GET", "PUT"],
        "/jobOpenings_id_/history/_externalId": ["PUT"]
    },
    "Job publications": {
        "/jobPublications": ["GET", "POST"],
        "/jobPublications/externalId=_externalId": ["GET"],
        "/jobPublications_id": ["GET", "PUT"],
        "/jobPublications_id_/delete": ["POST"]
    },
    "Job publication placements": {
        "/jobPublicationPlacements/_partner_id_/placements": ["GET", "POST"],
        "/jobPublicationPlacements/_partner_id_/placements/externalId=_externalId": ["GET"],
        "/jobPublicationPlacements/_partner_id_/placements/jobPublicationId=_jobPublicationId": ["GET"],
        "/jobPublicationPlacements/_partner_id_/placements_id": ["GET", "PUT"],
        "/jobPublicationPlacements/_partner_id_/placements_id_/delete": ["POST"]
    },
    "Job publication channels": {
        "/jobPublicationChannels_id": ["GET", "PUT"]
    },
    "Locations": {
        "/locations": ["GET", "POST"],
        "/locations_id": ["GET", "PUT"],
        "/locations_id_/delete": ["POST"]
    },
    "Onboardings": {
        "/onboardings": ["GET"],
        "/onboardings_id": ["GET"],
        "/onboardings_id_/attachments": ["GET"],
        "/onboardings_id_/attachments/_attachmentId": ["GET"],
        "/onboardings_id_/attachments/_attachmentId_/pdf": ["GET"],
        "/onboardings_id_/delete": ["POST"]
    },
    "Organisation units": {
        "/orgUnits": ["GET"],
        "/orgUnits_id": ["GET"]
    },
    "Persons": {
        "/persons": ["GET", "POST"],
        "/persons/externalId=_externalId": ["GET"],
        "/persons_id": ["GET", "PUT"],
        "/persons_id_/delete": ["POST"],
        "/persons_id_/photo": ["GET", "POST"],
        "/persons_id_/photo/delete": ["POST"]
    },
    "Users": {
        "/dvinciUsers": ["GET", "POST"],
        "/dvinciUsers_id": ["GET", "PUT"],
        "/dvinciUsers_id_/delete": ["POST"]
    },
    "User groups": {
        "/userGroups": ["GET", "POST"],
        "/userGroups_id": ["GET", "PUT"],
        "/userGroups_id_/delete": ["POST"]
    }
}

# Basis-Pfad, in dem die Ordner und Dateien erstellt werden
base_path = 'output'


def sanitize_filename(name):
    """
    Ersetzt ungültige Zeichen in Dateinamen durch Unterstriche.

    :param name: Der ursprüngliche Name.
    :return: Der bereinigte Name.
    """
    return re.sub(r'[\\/*?:"<>|{}]', '_', name)


def create_files_and_folders(base_path, categories):
    """
    Erstellt die Ordner und JSON-Dateien basierend auf den Kategorien und Endpunkten.

    :param base_path: Der Basis-Pfad, in dem die Ordner und Dateien erstellt werden.
    :param categories: Ein Dictionary, das die Kategorien und Endpunkte enthält.
    """
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    for category, endpoints in categories.items():
        category_path = os.path.join(
            base_path, category.replace(' ', '_').lower())
        if not os.path.exists(category_path):
            os.makedirs(category_path)

        for endpoint, methods in endpoints.items():
            endpoint_path = os.path.join(
                category_path, sanitize_filename(endpoint.strip('/')))
            if not os.path.exists(endpoint_path):
                os.makedirs(endpoint_path)

            for method in methods:
                request_file_path = os.path.join(
                    endpoint_path, f"{method.lower()}_request.json")
                response_file_path = os.path.join(
                    endpoint_path, f"{method.lower()}_response.json")

                # Erstelle die Dateien und lasse sie leer
                with open(request_file_path, 'w', encoding='utf-8') as f:
                    json.dump({}, f, ensure_ascii=False, indent=4)
                with open(response_file_path, 'w', encoding='utf-8') as f:
                    json.dump({}, f, ensure_ascii=False, indent=4)

                print(
                    f'Created files: {request_file_path} and {response_file_path}')


def main():
    """
    Hauptfunktion des Skripts.
    """
    create_files_and_folders(base_path, categories)
    print('All files and folders have been created successfully.')


if __name__ == "__main__":
    main()
