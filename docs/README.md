# Dvinci API Documentation

## Applications

### /applications/

**GET**
Get a list of permitted applications

Query Parameters:

-   byJobOpeningId: (number)
    Filter list by given job opening id.
-   byJobOpeningExternalId: (string)
    Filter list by given job opening externalId.
-   byApplicationStatusId: (string)
    Filter list by given application status internal-name.
-   byOrgUnitId: (number)
    Filter list by given organisation unit id.
-   byDateCreatedFrom: (date)
    Filter list by given creation date of application (from).
-   byDateCreatedTo: (date)
    Filter list by given creation date of application (to).
-   byLastStatusChangeDateFrom: (date)
    Filter list by given last status change date of application (from).
-   byLastStatusChangeDateTo: (date)
    Filter list by given last status change date of application (to).

**POST**
Create a new application.

Schema:

```json
{
    "externalId": "583988DC-1CD9-489B-A5D2-7D3E14712508",
    "person": {
        "id": 1,
        "externalId": "FA805173-9417-48C6-A063-28A5B6111DFF"
    },
    "jobOpening": {
        "externalId": "C99EDCDB-020F-4299-8340-4543DD22D7FB"
    },
    "applicationStatusId": "SYS_NEW",
    "languageId": "de",
    "comment": "This is a new comment!",
    "privacyPolicyAccepted": true,
    "extendedUseAccepted": true,
    "earliestStartingDate": "as soon as possible",
    "desiredSalary": "30.000$ per year",
    "hrServiceProviderEmail": "michael.mustermann@dvinci.de",
    "desiredLocations": ["HAMBURG", "NEW_YORK"],
    "type": "ONLINE",
    "rating": "B",
    "sourceId": "FAZ",
    "rejectionCodeId": null,
    "refJobPublication": {
        "id": 1
    },
    "refApplyDate": "2017-03-12",
    "dateCreated": "2017-03-12T09:14:04.997Z",
    "lastStatusChangeDate": "2017-03-14T08:14:06.129Z",
    "screeningQuestions": [
        {
            "id": "MS_OFFICE_KNOWLEDGE",
            "answers": [
                {
                    "id": "WORD"
                },
                {
                    "id": "EXCEL"
                }
            ]
        },
        {
            "id": "MATH_MARK",
            "answers": [
                {
                    "id": "MARK_4"
                }
            ]
        },
        {
            "id": "JAVA_KNOWLEDGE",
            "answer": "3"
        },
        {
            "id": "NATIONALITY",
            "answer": "German"
        }
    ]
}
```

### /applications/?externalId={externalId}

GET
Get a application with given externalId. asddasddasd

**URI Parameters**

-   externalId: required (string)

### /applications/{id}

GET
Get a specific application

PUT
Update a application

### /applications/{id}/delete

POST
Delete a specific application

### /applications/{id}/statusChange/{statusId}

POST
Change status for a specific application

### /applications/{id}/jobOpeningMove/{jobOpeningId}

POST
Change the associated job opening of a specific application

### /applications/{id}/attachments

GET
Get all attachments for given application id

POST
Add new attachment for a given application id

### /applications/{id}/attachments/{attachmentId}

GET
Get attachment for given application id and attachment id

/applications/{id}/attachments/{attachmentId}/pdfget
get
Get converted version (always a pdf) of the attachment for given application id and attachment id

/applications/{id}/attachments/{attachmentId}/deletepost
post
Delete a specific attachment

/applications/{id}/historyget put
get
Get all history entries for given application id

put
Add or update a list of history entries for a given application

/applications/{id}/history/{externalId}put
put
Add a new or update an existing history entry for given application
