# Endpoint Schemas

## Table of Contents

-   [Endpoint Schemas](#endpoint-schemas)
    -   [Table of Contents](#table-of-contents)
    -   [Applications](#applications)
        -   [GET /applications/](#get-applications)
            -   [Request](#request)
            -   [Response](#response)
        -   [POST /applications/](#post-applications)
            -   [Request](#request-1)
            -   [Response](#response-1)
        -   [GET /applications/?externalId={externalId}](#get-applicationsexternalidexternalid)
            -   [Request](#request-2)
            -   [Response](#response-2)
        -   [GET /applications/{id}](#get-applicationsid)
            -   [Request](#request-3)
            -   [Response](#response-3)
        -   [PUT /applications/{id}](#put-applicationsid)
            -   [Request](#request-4)
            -   [Response](#response-4)
        -   [POST /applications/{id}/delete](#post-applicationsiddelete)
            -   [Request](#request-5)
            -   [Response](#response-5)
        -   [POST /applications/{id}/statusChange/{statusId}](#post-applicationsidstatuschangestatusid)
            -   [Request](#request-6)
            -   [Response](#response-6)
        -   [POST /applications/{id}/jobOpeningMove/{jobOpeningId}](#post-applicationsidjobopeningmovejobopeningid)
            -   [Request](#request-7)
            -   [Response](#response-7)
        -   [GET /applications/{id}/attachments](#get-applicationsidattachments)
            -   [Request](#request-8)
            -   [Response](#response-8)
        -   [POST /applications/{id}/attachments](#post-applicationsidattachments)
            -   [Request](#request-9)
            -   [Response](#response-9)
        -   [GET /applications/{id}/attachments/{attachmentId}](#get-applicationsidattachmentsattachmentid)
            -   [Request](#request-10)
            -   [Response](#response-10)
        -   [GET /applications/{id}/attachments/{attachmentId}/pdf](#get-applicationsidattachmentsattachmentidpdf)
            -   [Request](#request-11)
            -   [Response](#response-11)
        -   [POST /applications/{id}/attachments/{attachmentId}/delete](#post-applicationsidattachmentsattachmentiddelete)
            -   [Request](#request-12)
            -   [Response](#response-12)
        -   [GET /applications/{id}/history](#get-applicationsidhistory)
            -   [Request](#request-13)
            -   [Response](#response-13)
        -   [PUT /applications/{id}/history](#put-applicationsidhistory)
            -   [Request](#request-14)
            -   [Response](#response-14)
        -   [PUT /applications/{id}/history/{externalId}](#put-applicationsidhistoryexternalid)
            -   [Request](#request-15)
            -   [Response](#response-15)
    -   [Configuration](#configuration)
        -   [GET /configuration/{type}/externalLinks](#get-configurationtypeexternallinks)
            -   [Request](#request-16)
            -   [Response](#response-16)
        -   [PUT /configuration/{type}/externalLinks](#put-configurationtypeexternallinks)
            -   [Request](#request-17)
            -   [Response](#response-17)
    -   [Hiring requests](#hiring-requests)
        -   [GET /hiringRequests/](#get-hiringrequests)
            -   [Request](#request-18)
            -   [Response](#response-18)
        -   [POST /hiringRequests/](#post-hiringrequests)
            -   [Request](#request-19)
            -   [Response](#response-19)
        -   [GET /hiringRequests/?externalId={externalId}](#get-hiringrequestsexternalidexternalid)
            -   [Request](#request-20)
            -   [Response](#response-20)
        -   [GET /hiringRequests/{id}](#get-hiringrequestsid)
            -   [Request](#request-21)
            -   [Response](#response-21)
        -   [PUT /hiringRequests/{id}](#put-hiringrequestsid)
            -   [Request](#request-22)
            -   [Response](#response-22)
        -   [GET /hiringRequests/{id}/history](#get-hiringrequestsidhistory)
            -   [Request](#request-23)
            -   [Response](#response-23)
        -   [GET /hiringRequests/{id}/approvers](#get-hiringrequestsidapprovers)
            -   [Request](#request-24)
            -   [Response](#response-24)
    -   [Job openings](#job-openings)
        -   [GET /jobOpenings/](#get-jobopenings)
            -   [Request](#request-25)
            -   [Response](#response-25)
        -   [POST /jobOpenings/](#post-jobopenings)
            -   [Request](#request-26)
            -   [Response](#response-26)
        -   [GET /jobOpenings/?externalId={externalId}](#get-jobopeningsexternalidexternalid)
            -   [Request](#request-27)
            -   [Response](#response-27)
        -   [GET /jobOpenings/{id}](#get-jobopeningsid)
            -   [Request](#request-28)
            -   [Response](#response-28)
        -   [PUT /jobOpenings/{id}](#put-jobopeningsid)
            -   [Request](#request-29)
            -   [Response](#response-29)
        -   [GET /jobOpenings/{id}/history](#get-jobopeningsidhistory)
            -   [Request](#request-30)
            -   [Response](#response-30)
        -   [PUT /jobOpenings/{id}/history](#put-jobopeningsidhistory)
            -   [Request](#request-31)
            -   [Response](#response-31)
        -   [PUT /jobOpenings/{id}/history/{externalId}](#put-jobopeningsidhistoryexternalid)
            -   [Request](#request-32)
            -   [Response](#response-32)
    -   [Job publications](#job-publications)
        -   [GET /jobPublications/](#get-jobpublications)
            -   [Request](#request-33)
            -   [Response](#response-33)
        -   [POST /jobPublications/](#post-jobpublications)
            -   [Request](#request-34)
            -   [Response](#response-34)
        -   [GET /jobPublications/?externalId={externalId}](#get-jobpublicationsexternalidexternalid)
            -   [Request](#request-35)
            -   [Response](#response-35)
        -   [GET /jobPublications/{id}](#get-jobpublicationsid)
            -   [Request](#request-36)
            -   [Response](#response-36)
        -   [PUT /jobPublications/{id}](#put-jobpublicationsid)
            -   [Request](#request-37)
            -   [Response](#response-37)
        -   [POST /jobPublications/{id}/delete](#post-jobpublicationsiddelete)
            -   [Request](#request-38)
            -   [Response](#response-38)
    -   [Job publication placements](#job-publication-placements)
        -   [GET /jobPublicationPlacements/{partner_id}/placements](#get-jobpublicationplacementspartner_idplacements)
            -   [Request](#request-39)
            -   [Response](#response-39)
        -   [POST /jobPublicationPlacements/{partner_id}/placements](#post-jobpublicationplacementspartner_idplacements)
            -   [Request](#request-40)
            -   [Response](#response-40)
        -   [GET /jobPublicationPlacements/{partner_id}/placements/?externalId={externalId}](#get-jobpublicationplacementspartner_idplacementsexternalidexternalid)
            -   [Request](#request-41)
            -   [Response](#response-41)
        -   [GET /jobPublicationPlacements/{partner_id}/placements/?jobPublicationId={jobPublicationId}](#get-jobpublicationplacementspartner_idplacementsjobpublicationidjobpublicationid)
            -   [Request](#request-42)
            -   [Response](#response-42)
        -   [GET /jobPublicationPlacements/{partner_id}/placements/{id}](#get-jobpublicationplacementspartner_idplacementsid)
            -   [Request](#request-43)
            -   [Response](#response-43)
        -   [PUT /jobPublicationPlacements/{partner_id}/placements/{id}](#put-jobpublicationplacementspartner_idplacementsid)
            -   [Request](#request-44)
            -   [Response](#response-44)
        -   [POST /jobPublicationPlacements/{partner_id}/placements/{id}/delete](#post-jobpublicationplacementspartner_idplacementsiddelete)
            -   [Request](#request-45)
            -   [Response](#response-45)
    -   [Job publication channels](#job-publication-channels)
        -   [GET /jobPublicationChannels/{id}](#get-jobpublicationchannelsid)
            -   [Request](#request-46)
            -   [Response](#response-46)
        -   [PUT /jobPublicationChannels/{id}](#put-jobpublicationchannelsid)
            -   [Request](#request-47)
            -   [Response](#response-47)
    -   [Locations](#locations)
        -   [GET /locations/](#get-locations)
            -   [Request](#request-48)
            -   [Response](#response-48)
        -   [POST /locations/](#post-locations)
            -   [Request](#request-49)
            -   [Response](#response-49)
        -   [GET /locations/{id}](#get-locationsid)
            -   [Request](#request-50)
            -   [Response](#response-50)
        -   [PUT /locations/{id}](#put-locationsid)
            -   [Request](#request-51)
            -   [Response](#response-51)
        -   [POST /locations/{id}/delete](#post-locationsiddelete)
            -   [Request](#request-52)
            -   [Response](#response-52)
    -   [Onboardings](#onboardings)
        -   [GET /onboardings/](#get-onboardings)
            -   [Request](#request-53)
            -   [Response](#response-53)
        -   [GET /onboardings/{id}](#get-onboardingsid)
            -   [Request](#request-54)
            -   [Response](#response-54)
        -   [GET /onboardings/{id}/attachments](#get-onboardingsidattachments)
            -   [Request](#request-55)
            -   [Response](#response-55)
        -   [GET /onboardings/{id}/attachments/{attachmentId}](#get-onboardingsidattachmentsattachmentid)
            -   [Request](#request-56)
            -   [Response](#response-56)
        -   [GET /onboardings/{id}/attachments/{attachmentId}/pdf](#get-onboardingsidattachmentsattachmentidpdf)
            -   [Request](#request-57)
            -   [Response](#response-57)
        -   [POST /onboardings/{id}/delete](#post-onboardingsiddelete)
            -   [Request](#request-58)
            -   [Response](#response-58)
    -   [Organisation units](#organisation-units)
        -   [GET /orgUnits/](#get-orgunits)
            -   [Request](#request-59)
            -   [Response](#response-59)
        -   [GET /orgUnits/{id}](#get-orgunitsid)
            -   [Request](#request-60)
            -   [Response](#response-60)
    -   [Persons](#persons)
        -   [GET /persons/](#get-persons)
            -   [Request](#request-61)
            -   [Response](#response-61)
        -   [POST /persons/](#post-persons)
            -   [Request](#request-62)
            -   [Response](#response-62)
        -   [GET /persons/?externalId={externalId}](#get-personsexternalidexternalid)
            -   [Request](#request-63)
            -   [Response](#response-63)
        -   [GET /persons/{id}](#get-personsid)
            -   [Request](#request-64)
            -   [Response](#response-64)
        -   [PUT /persons/{id}](#put-personsid)
            -   [Request](#request-65)
            -   [Response](#response-65)
        -   [POST /persons/{id}/delete](#post-personsiddelete)
            -   [Request](#request-66)
            -   [Response](#response-66)
        -   [GET /persons/{id}/photo](#get-personsidphoto)
            -   [Request](#request-67)
            -   [Response](#response-67)
        -   [POST /persons/{id}/photo](#post-personsidphoto)
            -   [Request](#request-68)
            -   [Response](#response-68)
        -   [POST /persons/{id}/photo/delete](#post-personsidphotodelete)
            -   [Request](#request-69)
            -   [Response](#response-69)
    -   [Users](#users)
        -   [GET /dvinciUsers/](#get-dvinciusers)
            -   [Request](#request-70)
            -   [Response](#response-70)
        -   [POST /dvinciUsers/](#post-dvinciusers)
            -   [Request](#request-71)
            -   [Response](#response-71)
        -   [GET /dvinciUsers/{id}](#get-dvinciusersid)
            -   [Request](#request-72)
            -   [Response](#response-72)
        -   [PUT /dvinciUsers/{id}](#put-dvinciusersid)
            -   [Request](#request-73)
            -   [Response](#response-73)
        -   [POST /dvinciUsers/{id}/delete](#post-dvinciusersiddelete)
            -   [Request](#request-74)
            -   [Response](#response-74)
    -   [User groups](#user-groups)
        -   [GET /userGroups/](#get-usergroups)
            -   [Request](#request-75)
            -   [Response](#response-75)
        -   [POST /userGroups/](#post-usergroups)
            -   [Request](#request-76)
            -   [Response](#response-76)
        -   [GET /userGroups/{id}](#get-usergroupsid)
            -   [Request](#request-77)
            -   [Response](#response-77)
        -   [PUT /userGroups/{id}](#put-usergroupsid)
            -   [Request](#request-78)
            -   [Response](#response-78)
        -   [POST /userGroups/{id}/delete](#post-usergroupsiddelete)
            -   [Request](#request-79)
            -   [Response](#response-79)

## Applications

### GET /applications/

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {
                "description": "Property is not settable - only returned by the system",
                "type": "integer"
            },
            "externalId": {
                "description": "Can be used to identify this resource in other systems. Must be unique or null.",
                "type": ["string", "null"]
            },
            "person": {
                "description": "Person of application",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "externalId": {
                        "type": ["string", "null"]
                    }
                },
                "type": "object"
            },
            "jobOpening": {
                "description": "Job opening of application.",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "externalId": {
                        "type": ["string", "null"]
                    }
                },
                "type": "object"
            },
            "applicationStatusId": {
                "description": "Status of application.",
                "type": "string"
            },
            "lastStatusChangeDate": {
                "description": "Date of last status change.",
                "type": "string",
                "format": "date-time"
            },
            "dateCreated": {
                "description": "Technical creation date of application.",
                "type": "string",
                "format": "date-time"
            }
        },
        "required": [
            "id",
            "externalId",
            "person",
            "jobOpening",
            "applicationStatusId",
            "lastStatusChangeDate",
            "dateCreated"
        ]
    }
}
```

### POST /applications/

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": "string"
        },
        "person": {
            "description": "Person that the application will be associated with. Property can not be updated.",
            "properties": {
                "id": {
                    "description": "ID of person. If ID is set externalId will be ignored.",
                    "type": ["integer", "null"]
                },
                "externalId": {
                    "description": "ExternalId of person.",
                    "type": ["string", "null"]
                }
            },
            "type": "object"
        },
        "jobOpening": {
            "description": "Job opening that the application will be associated with. Property can not be updated.",
            "properties": {
                "id": {
                    "description": "ID of job opening. If ID is set externalId will be ignored.",
                    "type": ["integer", "null"]
                },
                "externalId": {
                    "description": "ExternalId of job opening.",
                    "type": ["string", "null"]
                }
            },
            "type": "object"
        },
        "applicationStatusId": {
            "description": "Initial status of application. Will be set to initial workflow status if empty.",
            "type": "string"
        },
        "languageId": {
            "description": "Language of application",
            "type": "string"
        },
        "comment": {
            "description": "Comment of application",
            "type": ["string", "null"]
        },
        "privacyPolicyAccepted": {
            "type": "boolean"
        },
        "extendedUseAccepted": {
            "type": ["boolean", "null"]
        },
        "earliestStartingDate": {
            "type": ["string", "null"]
        },
        "desiredSalary": {
            "type": ["string", "null"]
        },
        "hrServiceProviderEmail": {
            "type": ["string", "null"]
        },
        "desiredLocationIds": {
            "description": "List of desired locations of application. Those values are correspondent to the /locations API",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "type": {
            "description": "Type of Application",
            "enum": [
                "ONLINE",
                "EMAIL",
                "LETTER",
                "HR_SERVICE_PROVIDER",
                "DIRECT_CONTACT"
            ]
        },
        "rating": {
            "description": "Rating can be set if user has required permission 'Rating set'.",
            "enum": [null, "NONE", "A", "B", "C"]
        },
        "sourceId": {
            "description": "Identifier of applications source.",
            "type": ["string", "null"]
        },
        "rejectionCodeId": {
            "description": "Identifier of applications rejection.",
            "type": ["string", "null"]
        },
        "refJobPublication": {
            "description": "Reference for correspondence: Application To Job Publication.",
            "properties": {
                "id": {
                    "description": "ID of job opening. If ID is set externalId will be ignored.",
                    "type": ["integer", "null"]
                },
                "externalId": {
                    "description": "ExternalId of job opening.",
                    "type": ["string", "null"]
                }
            },
            "type": ["object", "null"]
        },
        "refApplyDate": {
            "description": "Reference for correspondence: Application On.",
            "type": ["string", "null"]
        },
        "dateCreated": {
            "description": "Technical creation date of application.",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "lastStatusChangeDate": {
            "description": "Date of last status change.",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "screeningQuestions": {
            "description": "List of answered screening questions. Screening question types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
            "items": {
                "properties": {
                    "answers": {
                        "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "string"
                                }
                            }
                        },
                        "type": "array"
                    },
                    "answer": {
                        "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                        "type": "string"
                    },
                    "id": {
                        "description": "Identifier of screening question",
                        "type": "string"
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": ["person", "jobOpening", "languageId", "type"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "person": {
            "description": "Person of application",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "externalId": {
                    "type": ["string", "null"]
                }
            },
            "type": "object"
        },
        "jobOpening": {
            "description": "Job opening of application.",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "externalId": {
                    "type": ["string", "null"]
                }
            },
            "type": "object"
        },
        "applicationStatusId": {
            "description": "Status of application.",
            "type": "string"
        },
        "languageId": {
            "description": "Language of application",
            "type": "string"
        },
        "comment": {
            "description": "Comment of application",
            "type": ["string", "null"]
        },
        "privacyPolicyAccepted": {
            "type": "boolean"
        },
        "extendedUseAccepted": {
            "type": ["boolean", "null"]
        },
        "earliestStartingDate": {
            "type": ["string", "null"]
        },
        "desiredSalary": {
            "type": ["string", "null"]
        },
        "hrServiceProviderEmail": {
            "type": ["string", "null"]
        },
        "desiredLocationIds": {
            "description": "List of desired locations of application. Those values are correspondent to the /locations API",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "type": {
            "description": "Type of Application",
            "enum": [
                "ONLINE",
                "EMAIL",
                "LETTER",
                "HR_SERVICE_PROVIDER",
                "DIRECT_CONTACT"
            ]
        },
        "rating": {
            "description": "Rating is only displayed if user has required permission 'Rating view'.",
            "enum": ["NONE", "A", "B", "C"]
        },
        "sourceId": {
            "description": "Identifier of applications source.",
            "type": ["string", "null"]
        },
        "rejectionCodeId": {
            "description": "Identifier of applications rejection.",
            "type": ["string", "null"]
        },
        "refJobPublication": {
            "description": "Reference for correspondence: Application To Job Publication.",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "externalId": {
                    "type": ["string", "null"]
                }
            },
            "type": ["object", "null"]
        },
        "refApplyDate": {
            "description": "Reference for correspondence: Application On.",
            "type": ["string", "null"]
        },
        "permanentPostNumber": {
            "description": "Number of permanent post of job opening.",
            "type": ["string", "null"]
        },
        "lastStatusChangeDate": {
            "description": "Date of last status change.",
            "type": "string",
            "format": "date-time"
        },
        "dateCreated": {
            "description": "Technical creation date of application.",
            "type": "string",
            "format": "date-time"
        },
        "candidateMailbox": {
            "description": "Mailbox of application.",
            "type": ["string", "null"],
            "format": "email"
        },
        "screeningQuestions": {
            "description": "List of answered screening questions. Screening question types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
            "items": {
                "properties": {
                    "answers": {
                        "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "answer": {
                                    "type": "string"
                                }
                            }
                        },
                        "type": "array"
                    },
                    "answer": {
                        "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                        "type": "string"
                    },
                    "displayName": {
                        "description": "Display name of screening question",
                        "type": "string"
                    },
                    "id": {
                        "description": "Identifier of screening question",
                        "type": "string"
                    },
                    "type": {
                        "description": "Type of the screening question",
                        "enum": [
                            "TEXT",
                            "TEXT_4_120",
                            "TEXTAREA",
                            "TEXTAREA_MAX_1200",
                            "FIVE_STAR_RATING",
                            "YES_NO",
                            "YES_NO_NOT_SPECIFIED",
                            "SINGLE_CHOICE",
                            "MULTI_CHOICE"
                        ]
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": [
        "id",
        "version",
        "person",
        "jobOpening",
        "applicationStatusId",
        "languageId",
        "type",
        "dateCreated"
    ]
}
```

### GET /applications/?externalId={externalId}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "person": {
            "description": "Person of application",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "externalId": {
                    "type": ["string", "null"]
                }
            },
            "type": "object"
        },
        "jobOpening": {
            "description": "Job opening of application.",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "externalId": {
                    "type": ["string", "null"]
                }
            },
            "type": "object"
        },
        "applicationStatusId": {
            "description": "Status of application.",
            "type": "string"
        },
        "languageId": {
            "description": "Language of application",
            "type": "string"
        },
        "comment": {
            "description": "Comment of application",
            "type": ["string", "null"]
        },
        "privacyPolicyAccepted": {
            "type": "boolean"
        },
        "extendedUseAccepted": {
            "type": ["boolean", "null"]
        },
        "earliestStartingDate": {
            "type": ["string", "null"]
        },
        "desiredSalary": {
            "type": ["string", "null"]
        },
        "hrServiceProviderEmail": {
            "type": ["string", "null"]
        },
        "desiredLocationIds": {
            "description": "List of desired locations of application. Those values are correspondent to the /locations API",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "type": {
            "description": "Type of Application",
            "enum": [
                "ONLINE",
                "EMAIL",
                "LETTER",
                "HR_SERVICE_PROVIDER",
                "DIRECT_CONTACT"
            ]
        },
        "rating": {
            "description": "Rating is only displayed if user has required permission 'Rating view'.",
            "enum": ["NONE", "A", "B", "C"]
        },
        "sourceId": {
            "description": "Identifier of applications source.",
            "type": ["string", "null"]
        },
        "rejectionCodeId": {
            "description": "Identifier of applications rejection.",
            "type": ["string", "null"]
        },
        "refJobPublication": {
            "description": "Reference for correspondence: Application To Job Publication.",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "externalId": {
                    "type": ["string", "null"]
                }
            },
            "type": ["object", "null"]
        },
        "refApplyDate": {
            "description": "Reference for correspondence: Application On.",
            "type": ["string", "null"]
        },
        "permanentPostNumber": {
            "description": "Number of permanent post of job opening.",
            "type": ["string", "null"]
        },
        "lastStatusChangeDate": {
            "description": "Date of last status change.",
            "type": "string",
            "format": "date-time"
        },
        "dateCreated": {
            "description": "Technical creation date of application.",
            "type": "string",
            "format": "date-time"
        },
        "candidateMailbox": {
            "description": "Mailbox of application.",
            "type": ["string", "null"],
            "format": "email"
        },
        "screeningQuestions": {
            "description": "List of answered screening questions. Screening question types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
            "items": {
                "properties": {
                    "answers": {
                        "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "answer": {
                                    "type": "string"
                                }
                            }
                        },
                        "type": "array"
                    },
                    "answer": {
                        "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                        "type": "string"
                    },
                    "displayName": {
                        "description": "Display name of screening question",
                        "type": "string"
                    },
                    "id": {
                        "description": "Identifier of screening question",
                        "type": "string"
                    },
                    "type": {
                        "description": "Type of the screening question",
                        "enum": [
                            "TEXT",
                            "TEXT_4_120",
                            "TEXTAREA",
                            "TEXTAREA_MAX_1200",
                            "FIVE_STAR_RATING",
                            "YES_NO",
                            "YES_NO_NOT_SPECIFIED",
                            "SINGLE_CHOICE",
                            "MULTI_CHOICE"
                        ]
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": [
        "id",
        "version",
        "person",
        "jobOpening",
        "applicationStatusId",
        "languageId",
        "type",
        "dateCreated"
    ]
}
```

### GET /applications/{id}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "person": {
            "description": "Person of application",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "externalId": {
                    "type": ["string", "null"]
                }
            },
            "type": "object"
        },
        "jobOpening": {
            "description": "Job opening of application.",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "externalId": {
                    "type": ["string", "null"]
                }
            },
            "type": "object"
        },
        "applicationStatusId": {
            "description": "Status of application.",
            "type": "string"
        },
        "languageId": {
            "description": "Language of application",
            "type": "string"
        },
        "comment": {
            "description": "Comment of application",
            "type": ["string", "null"]
        },
        "privacyPolicyAccepted": {
            "type": "boolean"
        },
        "extendedUseAccepted": {
            "type": ["boolean", "null"]
        },
        "earliestStartingDate": {
            "type": ["string", "null"]
        },
        "desiredSalary": {
            "type": ["string", "null"]
        },
        "hrServiceProviderEmail": {
            "type": ["string", "null"]
        },
        "desiredLocationIds": {
            "description": "List of desired locations of application. Those values are correspondent to the /locations API",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "type": {
            "description": "Type of Application",
            "enum": [
                "ONLINE",
                "EMAIL",
                "LETTER",
                "HR_SERVICE_PROVIDER",
                "DIRECT_CONTACT"
            ]
        },
        "rating": {
            "description": "Rating is only displayed if user has required permission 'Rating view'.",
            "enum": ["NONE", "A", "B", "C"]
        },
        "sourceId": {
            "description": "Identifier of applications source.",
            "type": ["string", "null"]
        },
        "rejectionCodeId": {
            "description": "Identifier of applications rejection.",
            "type": ["string", "null"]
        },
        "refJobPublication": {
            "description": "Reference for correspondence: Application To Job Publication.",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "externalId": {
                    "type": ["string", "null"]
                }
            },
            "type": ["object", "null"]
        },
        "refApplyDate": {
            "description": "Reference for correspondence: Application On.",
            "type": ["string", "null"]
        },
        "permanentPostNumber": {
            "description": "Number of permanent post of job opening.",
            "type": ["string", "null"]
        },
        "lastStatusChangeDate": {
            "description": "Date of last status change.",
            "type": "string",
            "format": "date-time"
        },
        "dateCreated": {
            "description": "Technical creation date of application.",
            "type": "string",
            "format": "date-time"
        },
        "candidateMailbox": {
            "description": "Mailbox of application.",
            "type": ["string", "null"],
            "format": "email"
        },
        "screeningQuestions": {
            "description": "List of answered screening questions. Screening question types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
            "items": {
                "properties": {
                    "answers": {
                        "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "answer": {
                                    "type": "string"
                                }
                            }
                        },
                        "type": "array"
                    },
                    "answer": {
                        "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                        "type": "string"
                    },
                    "displayName": {
                        "description": "Display name of screening question",
                        "type": "string"
                    },
                    "id": {
                        "description": "Identifier of screening question",
                        "type": "string"
                    },
                    "type": {
                        "description": "Type of the screening question",
                        "enum": [
                            "TEXT",
                            "TEXT_4_120",
                            "TEXTAREA",
                            "TEXTAREA_MAX_1200",
                            "FIVE_STAR_RATING",
                            "YES_NO",
                            "YES_NO_NOT_SPECIFIED",
                            "SINGLE_CHOICE",
                            "MULTI_CHOICE"
                        ]
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": [
        "id",
        "version",
        "person",
        "jobOpening",
        "applicationStatusId",
        "languageId",
        "type",
        "dateCreated"
    ]
}
```

### PUT /applications/{id}

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": "string"
        },
        "languageId": {
            "description": "Language of application",
            "type": "string"
        },
        "comment": {
            "description": "Comment of application",
            "type": ["string", "null"]
        },
        "privacyPolicyAccepted": {
            "type": "boolean"
        },
        "extendedUseAccepted": {
            "type": ["boolean", "null"]
        },
        "earliestStartingDate": {
            "type": ["string", "null"]
        },
        "desiredSalary": {
            "type": ["string", "null"]
        },
        "hrServiceProviderEmail": {
            "type": ["string", "null"]
        },
        "desiredLocationIds": {
            "description": "List of desired locations of application. Those values are correspondent to the /locations API",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "type": {
            "description": "Type of Application",
            "enum": [
                "ONLINE",
                "EMAIL",
                "LETTER",
                "HR_SERVICE_PROVIDER",
                "DIRECT_CONTACT"
            ]
        },
        "rating": {
            "description": "Rating can be set if user has required permission 'Rating set'.",
            "enum": [null, "NONE", "A", "B", "C"]
        },
        "sourceId": {
            "description": "Identifier of applications source.",
            "type": ["string", "null"]
        },
        "rejectionCodeId": {
            "description": "Identifier of applications rejection.",
            "type": ["string", "null"]
        },
        "refJobPublication": {
            "description": "Reference for correspondence: Application To Job Publication.",
            "properties": {
                "id": {
                    "description": "ID of job opening. If ID is set externalId will be ignored.",
                    "type": ["integer", "null"]
                },
                "externalId": {
                    "description": "ExternalId of job opening.",
                    "type": ["string", "null"]
                }
            },
            "type": ["object", "null"]
        },
        "refApplyDate": {
            "description": "Reference for correspondence: Application On.",
            "type": ["string", "null"]
        },
        "screeningQuestions": {
            "description": "List of answered screening questions. Screening question types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
            "items": {
                "properties": {
                    "answers": {
                        "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "string"
                                }
                            }
                        },
                        "type": "array"
                    },
                    "answer": {
                        "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                        "type": "string"
                    },
                    "id": {
                        "description": "Identifier of screening question",
                        "type": "string"
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": ["version", "languageId", "type", "rating"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "person": {
            "description": "Person of application",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "externalId": {
                    "type": ["string", "null"]
                }
            },
            "type": "object"
        },
        "jobOpening": {
            "description": "Job opening of application.",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "externalId": {
                    "type": ["string", "null"]
                }
            },
            "type": "object"
        },
        "applicationStatusId": {
            "description": "Status of application.",
            "type": "string"
        },
        "languageId": {
            "description": "Language of application",
            "type": "string"
        },
        "comment": {
            "description": "Comment of application",
            "type": ["string", "null"]
        },
        "privacyPolicyAccepted": {
            "type": "boolean"
        },
        "extendedUseAccepted": {
            "type": ["boolean", "null"]
        },
        "earliestStartingDate": {
            "type": ["string", "null"]
        },
        "desiredSalary": {
            "type": ["string", "null"]
        },
        "hrServiceProviderEmail": {
            "type": ["string", "null"]
        },
        "desiredLocationIds": {
            "description": "List of desired locations of application. Those values are correspondent to the /locations API",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "type": {
            "description": "Type of Application",
            "enum": [
                "ONLINE",
                "EMAIL",
                "LETTER",
                "HR_SERVICE_PROVIDER",
                "DIRECT_CONTACT"
            ]
        },
        "rating": {
            "description": "Rating is only displayed if user has required permission 'Rating view'.",
            "enum": ["NONE", "A", "B", "C"]
        },
        "sourceId": {
            "description": "Identifier of applications source.",
            "type": ["string", "null"]
        },
        "rejectionCodeId": {
            "description": "Identifier of applications rejection.",
            "type": ["string", "null"]
        },
        "refJobPublication": {
            "description": "Reference for correspondence: Application To Job Publication.",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "externalId": {
                    "type": ["string", "null"]
                }
            },
            "type": ["object", "null"]
        },
        "refApplyDate": {
            "description": "Reference for correspondence: Application On.",
            "type": ["string", "null"]
        },
        "permanentPostNumber": {
            "description": "Number of permanent post of job opening.",
            "type": ["string", "null"]
        },
        "lastStatusChangeDate": {
            "description": "Date of last status change.",
            "type": "string",
            "format": "date-time"
        },
        "dateCreated": {
            "description": "Technical creation date of application.",
            "type": "string",
            "format": "date-time"
        },
        "candidateMailbox": {
            "description": "Mailbox of application.",
            "type": ["string", "null"],
            "format": "email"
        },
        "screeningQuestions": {
            "description": "List of answered screening questions. Screening question types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
            "items": {
                "properties": {
                    "answers": {
                        "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "answer": {
                                    "type": "string"
                                }
                            }
                        },
                        "type": "array"
                    },
                    "answer": {
                        "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                        "type": "string"
                    },
                    "displayName": {
                        "description": "Display name of screening question",
                        "type": "string"
                    },
                    "id": {
                        "description": "Identifier of screening question",
                        "type": "string"
                    },
                    "type": {
                        "description": "Type of the screening question",
                        "enum": [
                            "TEXT",
                            "TEXT_4_120",
                            "TEXTAREA",
                            "TEXTAREA_MAX_1200",
                            "FIVE_STAR_RATING",
                            "YES_NO",
                            "YES_NO_NOT_SPECIFIED",
                            "SINGLE_CHOICE",
                            "MULTI_CHOICE"
                        ]
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": [
        "id",
        "version",
        "person",
        "jobOpening",
        "applicationStatusId",
        "languageId",
        "type",
        "dateCreated"
    ]
}
```

### POST /applications/{id}/delete

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        }
    },
    "required": ["success"]
}
```

### POST /applications/{id}/statusChange/{statusId}

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "correspondenceTemplateId": {
            "description": "id of the correspondence template for candidate emails.",
            "type": "string"
        },
        "comment": {
            "description": "comment concerning the status change.",
            "type": "string"
        }
    }
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        }
    },
    "required": ["success"]
}
```

### POST /applications/{id}/jobOpeningMove/{jobOpeningId}

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "comment": {
            "description": "comment concerning the job opening change.",
            "type": "string"
        }
    }
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        }
    },
    "required": ["success"]
}
```

### GET /applications/{id}/attachments

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {
                "description": "Property is not settable - only returned by the system.",
                "type": "string"
            },
            "dateCreated": {
                "description": "Technical creation date of the attachment.",
                "type": "string",
                "format": "date-time"
            },
            "filename": {
                "description": "File name of the attachment.",
                "type": "string"
            },
            "fileSize": {
                "description": "File size of the attachment.",
                "type": "integer"
            },
            "contentType": {
                "description": "Content type of the attachment.",
                "type": "string"
            },
            "description": {
                "description": "Description of the attachment.",
                "type": "string"
            },
            "conversionState": {
                "description": "Conversion state of the attachment - null means conversion not executed.",
                "enum": ["DONE", "DOING", "FAILED", null]
            }
        },
        "required": ["id", "dateCreated", "filename", "fileSize", "contentType"]
    }
}
```

### POST /applications/{id}/attachments

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "filename": {
            "description": "File name of the attachment.",
            "type": "string"
        },
        "description": {
            "description": "Description of the attachment.",
            "type": "string"
        },
        "contentAsBase64": {
            "description": "Content of the attachment file encoded as base64.",
            "type": "string"
        }
    },
    "required": ["filename", "contentAsBase64"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        }
    },
    "required": ["id"]
}
```

### GET /applications/{id}/attachments/{attachmentId}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system.",
            "type": "string"
        },
        "dateCreated": {
            "description": "Technical creation date of the attachment.",
            "type": "string",
            "format": "date-time"
        },
        "filename": {
            "description": "File name of the attachment.",
            "type": "string"
        },
        "fileSize": {
            "description": "File size of the attachment.",
            "type": "integer"
        },
        "contentType": {
            "description": "Content type of the attachment.",
            "type": "string"
        },
        "description": {
            "description": "Description of the attachment.",
            "type": "string"
        },
        "conversionState": {
            "description": "Conversion state of the attachment - null means conversion not executed.",
            "enum": ["DONE", "DOING", "FAILED", null]
        },
        "contentAsBase64": {
            "description": "Content of the attachment file encoded as base64.",
            "type": "string"
        }
    },
    "required": [
        "id",
        "dateCreated",
        "filename",
        "fileSize",
        "contentType",
        "contentAsBase64"
    ]
}
```

### GET /applications/{id}/attachments/{attachmentId}/pdf

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system.",
            "type": "string"
        },
        "dateCreated": {
            "description": "Technical creation date of the attachment.",
            "type": "string",
            "format": "date-time"
        },
        "filename": {
            "description": "File name of the attachment.",
            "type": "string"
        },
        "fileSize": {
            "description": "File size of the attachment.",
            "type": "integer"
        },
        "contentType": {
            "description": "Content type of the attachment.",
            "type": "string"
        },
        "description": {
            "description": "Description of the attachment.",
            "type": "string"
        },
        "contentAsBase64": {
            "description": "Content of the attachment file encoded as base64.",
            "type": "string"
        }
    },
    "required": [
        "id",
        "dateCreated",
        "filename",
        "fileSize",
        "contentType",
        "contentAsBase64"
    ]
}
```

### POST /applications/{id}/attachments/{attachmentId}/delete

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        }
    },
    "required": ["success"]
}
```

### GET /applications/{id}/history

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "comment": {
                "description": "The comment of the history entry",
                "type": ["string", "null"]
            },
            "dateCreated": {
                "description": "The creation-date of the history entry",
                "type": "string",
                "format": "date-time"
            },
            "description": {
                "description": "The human readable description of the history entry",
                "type": "string"
            },
            "dvinciUserId": {
                "description": "The dvinci user who has triggered the history entry",
                "type": "integer"
            },
            "externalId": {
                "description": "The unique identifier of the external system.",
                "type": ["string", "null"]
            },
            "externalUser": {
                "description": "A display name for a user, who does not exists in the dvinci system.",
                "type": ["string", "null"]
            },
            "type": {
                "description": "The type of the history entry.",
                "type": "string"
            },
            "fromApplicationStatusId": {
                "description": "Source application status on application status change operations. Property only exists for types: APPLICATION_ENTRY, APPLICATION_STATUS_CHANGE, APPLICATION_AUTO_STATUS_CHANGE",
                "type": ["string", "null"]
            },
            "toApplicationStatusId": {
                "description": "Destination application status on application status change operations. Property only exists for types: APPLICATION_ENTRY, APPLICATION_STATUS_CHANGE, APPLICATION_AUTO_STATUS_CHANGE",
                "type": ["string"]
            }
        },
        "required": ["dateCreated", "type", "description", "dvinciUserId"]
    }
}
```

### PUT /applications/{id}/history

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "properties": {
        "dateCreated": {
            "description": "The creation-date of the history entry",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "description": {
            "description": "The description for the history entry",
            "type": "string"
        },
        "dvinciUserId": {
            "description": "The dvinci user who has triggered the history entry",
            "type": ["null", "integer"]
        },
        "externalUser": {
            "description": "A display name for a user, who does not exists in the dvinci system.",
            "type": ["string", "null"]
        },
        "externalId": {
            "description": "The unique identifier of the external system.",
            "type": "string"
        }
    },
    "required": ["description", "externalId"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "comment": {
                "description": "The comment of the history entry",
                "type": ["string", "null"]
            },
            "dateCreated": {
                "description": "The creation-date of the history entry",
                "type": "string",
                "format": "date-time"
            },
            "description": {
                "description": "The human readable description of the history entry",
                "type": "string"
            },
            "dvinciUserId": {
                "description": "The dvinci user who has triggered the history entry",
                "type": "integer"
            },
            "externalId": {
                "description": "The unique identifier of the external system.",
                "type": ["string", "null"]
            },
            "externalUser": {
                "description": "A display name for a user, who does not exists in the dvinci system.",
                "type": ["string", "null"]
            },
            "type": {
                "description": "The type of the history entry.",
                "type": "string"
            },
            "fromApplicationStatusId": {
                "description": "Source application status on application status change operations. Property only exists for types: APPLICATION_ENTRY, APPLICATION_STATUS_CHANGE, APPLICATION_AUTO_STATUS_CHANGE",
                "type": ["string", "null"]
            },
            "toApplicationStatusId": {
                "description": "Destination application status on application status change operations. Property only exists for types: APPLICATION_ENTRY, APPLICATION_STATUS_CHANGE, APPLICATION_AUTO_STATUS_CHANGE",
                "type": ["string"]
            }
        },
        "required": ["dateCreated", "type", "description", "dvinciUserId"]
    }
}
```

### PUT /applications/{id}/history/{externalId}

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "dateCreated": {
            "description": "The creation-date of the history entry",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "description": {
            "description": "The description for the history entry",
            "type": "string"
        },
        "dvinciUserId": {
            "description": "The dvinci user who has triggered the history entry",
            "type": ["null", "integer"]
        },
        "externalUser": {
            "description": "A display name for a user, who does not exists in the dvinci system.",
            "type": ["string", "null"]
        }
    },
    "required": ["description"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "comment": {
            "description": "The comment of the history entry",
            "type": ["string", "null"]
        },
        "dateCreated": {
            "description": "The creation-date of the history entry",
            "type": "string",
            "format": "date-time"
        },
        "description": {
            "description": "The human readable description of the history entry",
            "type": "string"
        },
        "dvinciUserId": {
            "description": "The dvinci user who has triggered the history entry",
            "type": "integer"
        },
        "externalId": {
            "description": "The unique identifier of the external system.",
            "type": ["string", "null"]
        },
        "externalUser": {
            "description": "A display name for a user, who does not exists in the dvinci system.",
            "type": ["string", "null"]
        },
        "type": {
            "description": "The type of the history entry.",
            "type": "string"
        },
        "fromApplicationStatusId": {
            "description": "Source application status on application status change operations. Property only exists for types: APPLICATION_ENTRY, APPLICATION_STATUS_CHANGE, APPLICATION_AUTO_STATUS_CHANGE",
            "type": ["string", "null"]
        },
        "toApplicationStatusId": {
            "description": "Destination application status on application status change operations. Property only exists for types: APPLICATION_ENTRY, APPLICATION_STATUS_CHANGE, APPLICATION_AUTO_STATUS_CHANGE",
            "type": ["string"]
        }
    },
    "required": ["dateCreated", "type", "description", "dvinciUserId"]
}
```

## Configuration

### GET /configuration/{type}/externalLinks

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
        "properties": {
            "nameMessages": {
                "type": "object",
                "properties": {
                    "de": {
                        "type": "string"
                    },
                    "en": {
                        "type": "string"
                    }
                },
                "description": "The external link name translated in available languages"
            },
            "url": {
                "description": "External link URL. Can contain the placeholder (jwt) that will be replaced if the URL is accessed.",
                "type": "string"
            },
            "faIcon": {
                "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'.",
                "type": "string"
            },
            "requiredPermission": {
                "description": "The internal name of the required permission to access the external link",
                "type": "string"
            }
        },
        "required": ["nameMessages", "url", "faIcon", "requiredPermission"]
    }
}
```

### PUT /configuration/{type}/externalLinks

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
        "properties": {
            "nameMessages": {
                "type": "object",
                "properties": {
                    "de": {
                        "type": "string"
                    },
                    "en": {
                        "type": "string"
                    }
                },
                "description": "The external link name translated in available languages"
            },
            "url": {
                "description": "External link URL. Can contain the placeholder (jwt) that will be replaced if the URL is accessed.",
                "type": "string"
            },
            "faIcon": {
                "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'.",
                "type": "string"
            },
            "requiredPermission": {
                "description": "The internal name of the required permission to access the external link",
                "type": "string"
            }
        },
        "required": ["nameMessages", "url", "faIcon", "requiredPermission"]
    }
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
        "properties": {
            "nameMessages": {
                "type": "object",
                "properties": {
                    "de": {
                        "type": "string"
                    },
                    "en": {
                        "type": "string"
                    }
                },
                "description": "The external link name translated in available languages"
            },
            "url": {
                "description": "External link URL. Can contain the placeholder (jwt) that will be replaced if the URL is accessed.",
                "type": "string"
            },
            "faIcon": {
                "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'.",
                "type": "string"
            },
            "requiredPermission": {
                "description": "The internal name of the required permission to access the external link",
                "type": "string"
            }
        },
        "required": ["nameMessages", "url", "faIcon", "requiredPermission"]
    }
}
```

## Hiring requests

### GET /hiringRequests/

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {
                "description": "Property is not settable - only returned by the system",
                "type": "integer"
            },
            "externalId": {
                "description": "Can be used to identify this resource in other systems. Must be unique or null.",
                "type": ["string", "null"]
            },
            "version": {
                "description": "Mandatory for all PUT requests",
                "type": "integer"
            },
            "jobTitle": {
                "description": "Job title of the hiring request",
                "type": "string"
            },
            "dateCreated": {
                "description": "The creation-date of the hiring request",
                "type": "string",
                "format": "date-time"
            },
            "orgUnitId": {
                "description": "OrgUnitId cannot be changed for an existing hiring request",
                "type": "integer"
            },
            "hiringRequestCreatorId": {
                "description": "The dvinci user who has created the hiring request. Value cannot be set by rest api.",
                "type": "integer"
            },
            "status": {
                "description": "Status of the hiring request. Value cannot be set by rest api.",
                "enum": ["OPEN", "IN_APPROVAL", "FINISHED"]
            },
            "superiorId": {
                "description": "The dvinci user who is superior of the hiring request",
                "type": "integer"
            },
            "hrContactId": {
                "description": "The dvinci user who is HR contact of the hiring request",
                "type": "integer"
            },
            "approvalStatus": {
                "description": "Approval status cannot be set or changed by rest api",
                "enum": ["NONE", "APPROVED", "REJECTED"]
            },
            "approvalProcessStarterId": {
                "description": "The dvinci user who started the hiring request approval process. Value cannot be set or changed by rest api.",
                "type": ["integer", "null"]
            },
            "companyId": {
                "description": "Internal name of company",
                "type": ["string", "null"]
            },
            "contractPeriodId": {
                "description": "Internal name of contract period",
                "type": ["string", "null"]
            },
            "functionGroupId": {
                "description": "Id of function group",
                "type": ["string", "null"]
            },
            "occupationalGroupId": {
                "description": "Id of occupational group",
                "type": ["string", "null"]
            },
            "payGradeId": {
                "description": "Id of pay grade",
                "type": ["string", "null"]
            },
            "openingsCount": {
                "description": "Number of openings",
                "type": ["integer", "null"]
            },
            "hiringReason": {
                "description": "Hiring reason",
                "enum": [
                    "ADDITIONAL_REQUIREMENT",
                    "EXPANSION",
                    "REPLACEMENT_TERMINATION",
                    "REPLACEMENT_TRANSFER",
                    "TEMPORARY_SUBSTITUTE",
                    "RENEWAL_OR_EXTENSION_OF_CONTRACT",
                    "TRAINING",
                    "OTHER"
                ]
            },
            "departmentAndCostUnit": {
                "description": "Department/ cost unit can only be set in combination with hiring reason REPLACEMENT_TRANSFER",
                "type": ["string", "null"]
            },
            "nameAndStaffNumber": {
                "description": "Name/ staff number can only be set in combination with hiring reasons REPLACEMENT_TERMINATION, REPLACEMENT_TRANSFER and TEMPORARY_SUBSTITUTE",
                "type": ["string", "null"]
            },
            "reason": {
                "description": "Reason can only be set in combination with hiring reasons TRAINING, EXPANSION, OTHER, RENEWAL_OR_EXTENSION_OF_CONTRACT, TEMPORARY_SUBSTITUTE and ADDITIONAL_REQUIREMENT",
                "type": ["string", "null"]
            },
            "substituteDateFrom": {
                "description": "Substition start date can only be set in combination with hiring reason TEMPORARY_SUBSTITUTE. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
                "type": ["string", "null"]
            },
            "substituteDateTo": {
                "description": "Substition end date can only be set in combination with hiring reason TEMPORARY_SUBSTITUTE. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
                "type": ["string", "null"]
            },
            "terminationDate": {
                "description": "Termination date can only be set in combination with hiring reason REPLACEMENT_TERMINATION. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
                "type": ["string", "null"]
            },
            "transferDate": {
                "description": "Transfer date can only be set in combination with hiring reason REPLACEMENT_TRANSFER. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
                "type": ["string", "null"]
            },
            "area": {
                "description": "Area",
                "type": ["string", "null"]
            },
            "costUnit": {
                "description": "Cost unit",
                "type": ["string", "null"]
            },
            "department": {
                "description": "Department",
                "type": ["string", "null"]
            },
            "profile": {
                "description": "Requirements",
                "type": ["string", "null"]
            },
            "remark": {
                "description": "Remark",
                "type": ["string", "null"]
            },
            "salary": {
                "description": "Wage/ salary range",
                "type": ["string", "null"]
            },
            "tasks": {
                "description": "Tasks",
                "type": ["string", "null"]
            },
            "vacancyNumber": {
                "description": "Vacancy number",
                "type": ["string", "null"]
            },
            "budgeted": {
                "description": "Budgeted",
                "type": ["boolean", "null"]
            },
            "earliestEntryDate": {
                "description": "Planned starting date. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
                "type": ["string", "null"]
            },
            "locationIds": {
                "description": "Internal name of location",
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
            "workingTimeIds": {
                "description": "Internal name of working time",
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
            "formFields": {
                "description": "List of answered form fields. Form field types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
                "items": {
                    "properties": {
                        "answers": {
                            "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                            "items": {
                                "properties": {
                                    "id": {
                                        "type": "string"
                                    },
                                    "answer": {
                                        "type": "string"
                                    }
                                }
                            },
                            "type": "array"
                        },
                        "answer": {
                            "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                            "type": "string"
                        },
                        "displayName": {
                            "description": "Display name of form field",
                            "type": "string"
                        },
                        "id": {
                            "description": "Identifier of form field",
                            "type": "string"
                        },
                        "type": {
                            "description": "Type of the form field",
                            "enum": [
                                "TEXT",
                                "TEXT_4_120",
                                "TEXTAREA",
                                "TEXTAREA_MAX_1200",
                                "FIVE_STAR_RATING",
                                "YES_NO",
                                "YES_NO_NOT_SPECIFIED",
                                "SINGLE_CHOICE",
                                "MULTI_CHOICE"
                            ]
                        }
                    },
                    "type": "object"
                },
                "type": "array"
            }
        },
        "required": [
            "id",
            "version",
            "jobTitle",
            "orgUnitId",
            "superiorId",
            "hrContactId"
        ]
    }
}
```

### POST /hiringRequests/

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "jobTitle": {
            "description": "Job title of the hiring request",
            "type": "string"
        },
        "orgUnitId": {
            "description": "OrgUnitId cannot be changed for an existing hiring request",
            "type": "integer"
        },
        "superiorId": {
            "description": "The dvinci user who is superior of the hiring request",
            "type": "integer"
        },
        "hrContactId": {
            "description": "The dvinci user who is HR contact of the hiring request",
            "type": "integer"
        },
        "approverIds": {
            "description": "The dvinci users who are approvers of the hiring request",
            "type": "array",
            "items": {
                "type": "integer"
            }
        },
        "companyId": {
            "description": "Internal name of company",
            "type": ["string", "null"]
        },
        "contractPeriodId": {
            "description": "Internal name of contract period",
            "type": ["string", "null"]
        },
        "functionGroupId": {
            "description": "Id of function group",
            "type": ["string", "null"]
        },
        "occupationalGroupId": {
            "description": "Id of occupational group",
            "type": ["string", "null"]
        },
        "payGradeId": {
            "description": "Id of pay grade",
            "type": ["string", "null"]
        },
        "openingsCount": {
            "description": "Number of openings",
            "type": ["integer", "null"]
        },
        "hiringReason": {
            "description": "Hiring reason",
            "enum": [
                "ADDITIONAL_REQUIREMENT",
                "EXPANSION",
                "REPLACEMENT_TERMINATION",
                "REPLACEMENT_TRANSFER",
                "TEMPORARY_SUBSTITUTE",
                "RENEWAL_OR_EXTENSION_OF_CONTRACT",
                "TRAINING",
                "OTHER"
            ]
        },
        "departmentAndCostUnit": {
            "description": "Department/ cost unit can only be set in combination with hiring reason REPLACEMENT_TRANSFER",
            "type": ["string", "null"]
        },
        "nameAndStaffNumber": {
            "description": "Name/ staff number can only be set in combination with hiring reasons REPLACEMENT_TERMINATION, REPLACEMENT_TRANSFER and TEMPORARY_SUBSTITUTE",
            "type": ["string", "null"]
        },
        "reason": {
            "description": "Reason can only be set in combination with hiring reasons TRAINING, EXPANSION, OTHER, RENEWAL_OR_EXTENSION_OF_CONTRACT, TEMPORARY_SUBSTITUTE and ADDITIONAL_REQUIREMENT",
            "type": ["string", "null"]
        },
        "substituteDateFrom": {
            "description": "Substition start date can only be set in combination with hiring reason TEMPORARY_SUBSTITUTE. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "substituteDateTo": {
            "description": "Substition end date can only be set in combination with hiring reason TEMPORARY_SUBSTITUTE. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "terminationDate": {
            "description": "Termination date can only be set in combination with hiring reason REPLACEMENT_TERMINATION. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "transferDate": {
            "description": "Transfer date can only be set in combination with hiring reason REPLACEMENT_TRANSFER. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "area": {
            "description": "Area",
            "type": ["string", "null"]
        },
        "costUnit": {
            "description": "Cost unit",
            "type": ["string", "null"]
        },
        "department": {
            "description": "Department",
            "type": ["string", "null"]
        },
        "profile": {
            "description": "Requirements",
            "type": ["string", "null"]
        },
        "remark": {
            "description": "Remark",
            "type": ["string", "null"]
        },
        "salary": {
            "description": "Wage/ salary range",
            "type": ["string", "null"]
        },
        "tasks": {
            "description": "Tasks",
            "type": ["string", "null"]
        },
        "vacancyNumber": {
            "description": "Vacancy number",
            "type": ["string", "null"]
        },
        "budgeted": {
            "description": "Budgeted",
            "type": ["boolean", "null"]
        },
        "earliestEntryDate": {
            "description": "Planned starting date. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "locationIds": {
            "description": "Internal name of location",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "workingTimeIds": {
            "description": "Internal name of working time",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "formFields": {
            "description": "List of answered form fields. Form field types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
            "items": {
                "properties": {
                    "answers": {
                        "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "answer": {
                                    "type": "string"
                                }
                            }
                        },
                        "type": "array"
                    },
                    "answer": {
                        "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                        "type": "string"
                    },
                    "displayName": {
                        "description": "Display name of form field",
                        "type": "string"
                    },
                    "id": {
                        "description": "Identifier of form field",
                        "type": "string"
                    },
                    "type": {
                        "description": "Type of the form field",
                        "enum": [
                            "TEXT",
                            "TEXT_4_120",
                            "TEXTAREA",
                            "TEXTAREA_MAX_1200",
                            "FIVE_STAR_RATING",
                            "YES_NO",
                            "YES_NO_NOT_SPECIFIED",
                            "SINGLE_CHOICE",
                            "MULTI_CHOICE"
                        ]
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": ["jobTitle", "orgUnitId", "superiorId", "hrContactId"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "jobTitle": {
            "description": "Job title of the hiring request",
            "type": "string"
        },
        "dateCreated": {
            "description": "The creation-date of the hiring request",
            "type": "string",
            "format": "date-time"
        },
        "orgUnitId": {
            "description": "OrgUnitId cannot be changed for an existing hiring request",
            "type": "integer"
        },
        "hiringRequestCreatorId": {
            "description": "The dvinci user who has created the hiring request. Value cannot be set by rest api.",
            "type": "integer"
        },
        "status": {
            "description": "Status cannot be changed to FINISHED by rest api",
            "enum": ["OPEN", "IN_APPROVAL", "FINISHED"]
        },
        "superiorId": {
            "description": "The dvinci user who is superior of the hiring request",
            "type": "integer"
        },
        "hrContactId": {
            "description": "The dvinci user who is HR contact of the hiring request",
            "type": "integer"
        },
        "approvalStatus": {
            "description": "Approval status cannot be set or changed by rest api",
            "enum": ["NONE", "APPROVED", "REJECTED"]
        },
        "approvalProcessStarterId": {
            "description": "The dvinci user who started the hiring request approval process. Value cannot be set or changed by rest api.",
            "type": ["integer", "null"]
        },
        "companyId": {
            "description": "Internal name of company",
            "type": ["string", "null"]
        },
        "contractPeriodId": {
            "description": "Internal name of contract period",
            "type": ["string", "null"]
        },
        "functionGroupId": {
            "description": "Id of function group",
            "type": ["string", "null"]
        },
        "occupationalGroupId": {
            "description": "Id of occupational group",
            "type": ["string", "null"]
        },
        "payGradeId": {
            "description": "Id of pay grade",
            "type": ["string", "null"]
        },
        "openingsCount": {
            "description": "Number of openings",
            "type": ["integer", "null"]
        },
        "hiringReason": {
            "description": "Hiring reason",
            "enum": [
                "ADDITIONAL_REQUIREMENT",
                "EXPANSION",
                "REPLACEMENT_TERMINATION",
                "REPLACEMENT_TRANSFER",
                "TEMPORARY_SUBSTITUTE",
                "RENEWAL_OR_EXTENSION_OF_CONTRACT",
                "TRAINING",
                "OTHER"
            ]
        },
        "departmentAndCostUnit": {
            "description": "Department/ cost unit can only be set in combination with hiring reason REPLACEMENT_TRANSFER",
            "type": ["string", "null"]
        },
        "nameAndStaffNumber": {
            "description": "Name/ staff number can only be set in combination with hiring reasons REPLACEMENT_TERMINATION, REPLACEMENT_TRANSFER and TEMPORARY_SUBSTITUTE",
            "type": ["string", "null"]
        },
        "reason": {
            "description": "Reason can only be set in combination with hiring reasons TRAINING, EXPANSION, OTHER, RENEWAL_OR_EXTENSION_OF_CONTRACT, TEMPORARY_SUBSTITUTE and ADDITIONAL_REQUIREMENT",
            "type": ["string", "null"]
        },
        "substituteDateFrom": {
            "description": "Substition start date can only be set in combination with hiring reason TEMPORARY_SUBSTITUTE. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "substituteDateTo": {
            "description": "Substition end date can only be set in combination with hiring reason TEMPORARY_SUBSTITUTE. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "terminationDate": {
            "description": "Termination date can only be set in combination with hiring reason REPLACEMENT_TERMINATION. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "transferDate": {
            "description": "Transfer date can only be set in combination with hiring reason REPLACEMENT_TRANSFER. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "area": {
            "description": "Area",
            "type": ["string", "null"]
        },
        "costUnit": {
            "description": "Cost unit",
            "type": ["string", "null"]
        },
        "department": {
            "description": "Department",
            "type": ["string", "null"]
        },
        "profile": {
            "description": "Requirements",
            "type": ["string", "null"]
        },
        "remark": {
            "description": "Remark",
            "type": ["string", "null"]
        },
        "salary": {
            "description": "Wage/ salary range",
            "type": ["string", "null"]
        },
        "tasks": {
            "description": "Tasks",
            "type": ["string", "null"]
        },
        "vacancyNumber": {
            "description": "Vacancy number",
            "type": ["string", "null"]
        },
        "budgeted": {
            "description": "Budgeted",
            "type": ["boolean", "null"]
        },
        "earliestEntryDate": {
            "description": "Planned starting date. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "locationIds": {
            "description": "Internal name of location",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "workingTimeIds": {
            "description": "Internal name of working time",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "formFields": {
            "description": "List of answered form fields. Form field types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
            "items": {
                "properties": {
                    "answers": {
                        "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "answer": {
                                    "type": "string"
                                }
                            }
                        },
                        "type": "array"
                    },
                    "answer": {
                        "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                        "type": "string"
                    },
                    "displayName": {
                        "description": "Display name of form field",
                        "type": "string"
                    },
                    "id": {
                        "description": "Identifier of form field",
                        "type": "string"
                    },
                    "type": {
                        "description": "Type of the form field",
                        "enum": [
                            "TEXT",
                            "TEXT_4_120",
                            "TEXTAREA",
                            "TEXTAREA_MAX_1200",
                            "FIVE_STAR_RATING",
                            "YES_NO",
                            "YES_NO_NOT_SPECIFIED",
                            "SINGLE_CHOICE",
                            "MULTI_CHOICE"
                        ]
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": [
        "id",
        "version",
        "jobTitle",
        "orgUnitId",
        "superiorId",
        "hrContactId"
    ]
}
```

### GET /hiringRequests/?externalId={externalId}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "jobTitle": {
            "description": "Job title of the hiring request",
            "type": "string"
        },
        "dateCreated": {
            "description": "The creation-date of the hiring request",
            "type": "string",
            "format": "date-time"
        },
        "orgUnitId": {
            "description": "OrgUnitId cannot be changed for an existing hiring request",
            "type": "integer"
        },
        "hiringRequestCreatorId": {
            "description": "The dvinci user who has created the hiring request. Value cannot be set by rest api.",
            "type": "integer"
        },
        "status": {
            "description": "Status cannot be changed to FINISHED by rest api",
            "enum": ["OPEN", "IN_APPROVAL", "FINISHED"]
        },
        "superiorId": {
            "description": "The dvinci user who is superior of the hiring request",
            "type": "integer"
        },
        "hrContactId": {
            "description": "The dvinci user who is HR contact of the hiring request",
            "type": "integer"
        },
        "approvalStatus": {
            "description": "Approval status cannot be set or changed by rest api",
            "enum": ["NONE", "APPROVED", "REJECTED"]
        },
        "approvalProcessStarterId": {
            "description": "The dvinci user who started the hiring request approval process. Value cannot be set or changed by rest api.",
            "type": ["integer", "null"]
        },
        "companyId": {
            "description": "Internal name of company",
            "type": ["string", "null"]
        },
        "contractPeriodId": {
            "description": "Internal name of contract period",
            "type": ["string", "null"]
        },
        "functionGroupId": {
            "description": "Id of function group",
            "type": ["string", "null"]
        },
        "occupationalGroupId": {
            "description": "Id of occupational group",
            "type": ["string", "null"]
        },
        "payGradeId": {
            "description": "Id of pay grade",
            "type": ["string", "null"]
        },
        "openingsCount": {
            "description": "Number of openings",
            "type": ["integer", "null"]
        },
        "hiringReason": {
            "description": "Hiring reason",
            "enum": [
                "ADDITIONAL_REQUIREMENT",
                "EXPANSION",
                "REPLACEMENT_TERMINATION",
                "REPLACEMENT_TRANSFER",
                "TEMPORARY_SUBSTITUTE",
                "RENEWAL_OR_EXTENSION_OF_CONTRACT",
                "TRAINING",
                "OTHER"
            ]
        },
        "departmentAndCostUnit": {
            "description": "Department/ cost unit can only be set in combination with hiring reason REPLACEMENT_TRANSFER",
            "type": ["string", "null"]
        },
        "nameAndStaffNumber": {
            "description": "Name/ staff number can only be set in combination with hiring reasons REPLACEMENT_TERMINATION, REPLACEMENT_TRANSFER and TEMPORARY_SUBSTITUTE",
            "type": ["string", "null"]
        },
        "reason": {
            "description": "Reason can only be set in combination with hiring reasons TRAINING, EXPANSION, OTHER, RENEWAL_OR_EXTENSION_OF_CONTRACT, TEMPORARY_SUBSTITUTE and ADDITIONAL_REQUIREMENT",
            "type": ["string", "null"]
        },
        "substituteDateFrom": {
            "description": "Substition start date can only be set in combination with hiring reason TEMPORARY_SUBSTITUTE. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "substituteDateTo": {
            "description": "Substition end date can only be set in combination with hiring reason TEMPORARY_SUBSTITUTE. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "terminationDate": {
            "description": "Termination date can only be set in combination with hiring reason REPLACEMENT_TERMINATION. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "transferDate": {
            "description": "Transfer date can only be set in combination with hiring reason REPLACEMENT_TRANSFER. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "area": {
            "description": "Area",
            "type": ["string", "null"]
        },
        "costUnit": {
            "description": "Cost unit",
            "type": ["string", "null"]
        },
        "department": {
            "description": "Department",
            "type": ["string", "null"]
        },
        "profile": {
            "description": "Requirements",
            "type": ["string", "null"]
        },
        "remark": {
            "description": "Remark",
            "type": ["string", "null"]
        },
        "salary": {
            "description": "Wage/ salary range",
            "type": ["string", "null"]
        },
        "tasks": {
            "description": "Tasks",
            "type": ["string", "null"]
        },
        "vacancyNumber": {
            "description": "Vacancy number",
            "type": ["string", "null"]
        },
        "budgeted": {
            "description": "Budgeted",
            "type": ["boolean", "null"]
        },
        "earliestEntryDate": {
            "description": "Planned starting date. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "locationIds": {
            "description": "Internal name of location",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "workingTimeIds": {
            "description": "Internal name of working time",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "formFields": {
            "description": "List of answered form fields. Form field types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
            "items": {
                "properties": {
                    "answers": {
                        "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "answer": {
                                    "type": "string"
                                }
                            }
                        },
                        "type": "array"
                    },
                    "answer": {
                        "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                        "type": "string"
                    },
                    "displayName": {
                        "description": "Display name of form field",
                        "type": "string"
                    },
                    "id": {
                        "description": "Identifier of form field",
                        "type": "string"
                    },
                    "type": {
                        "description": "Type of the form field",
                        "enum": [
                            "TEXT",
                            "TEXT_4_120",
                            "TEXTAREA",
                            "TEXTAREA_MAX_1200",
                            "FIVE_STAR_RATING",
                            "YES_NO",
                            "YES_NO_NOT_SPECIFIED",
                            "SINGLE_CHOICE",
                            "MULTI_CHOICE"
                        ]
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": [
        "id",
        "version",
        "jobTitle",
        "orgUnitId",
        "superiorId",
        "hrContactId"
    ]
}
```

### GET /hiringRequests/{id}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "jobTitle": {
            "description": "Job title of the hiring request",
            "type": "string"
        },
        "dateCreated": {
            "description": "The creation-date of the hiring request",
            "type": "string",
            "format": "date-time"
        },
        "orgUnitId": {
            "description": "OrgUnitId cannot be changed for an existing hiring request",
            "type": "integer"
        },
        "hiringRequestCreatorId": {
            "description": "The dvinci user who has created the hiring request. Value cannot be set by rest api.",
            "type": "integer"
        },
        "status": {
            "description": "Status cannot be changed to FINISHED by rest api",
            "enum": ["OPEN", "IN_APPROVAL", "FINISHED"]
        },
        "superiorId": {
            "description": "The dvinci user who is superior of the hiring request",
            "type": "integer"
        },
        "hrContactId": {
            "description": "The dvinci user who is HR contact of the hiring request",
            "type": "integer"
        },
        "approvalStatus": {
            "description": "Approval status cannot be set or changed by rest api",
            "enum": ["NONE", "APPROVED", "REJECTED"]
        },
        "approvalProcessStarterId": {
            "description": "The dvinci user who started the hiring request approval process. Value cannot be set or changed by rest api.",
            "type": ["integer", "null"]
        },
        "companyId": {
            "description": "Internal name of company",
            "type": ["string", "null"]
        },
        "contractPeriodId": {
            "description": "Internal name of contract period",
            "type": ["string", "null"]
        },
        "functionGroupId": {
            "description": "Id of function group",
            "type": ["string", "null"]
        },
        "occupationalGroupId": {
            "description": "Id of occupational group",
            "type": ["string", "null"]
        },
        "payGradeId": {
            "description": "Id of pay grade",
            "type": ["string", "null"]
        },
        "openingsCount": {
            "description": "Number of openings",
            "type": ["integer", "null"]
        },
        "hiringReason": {
            "description": "Hiring reason",
            "enum": [
                "ADDITIONAL_REQUIREMENT",
                "EXPANSION",
                "REPLACEMENT_TERMINATION",
                "REPLACEMENT_TRANSFER",
                "TEMPORARY_SUBSTITUTE",
                "RENEWAL_OR_EXTENSION_OF_CONTRACT",
                "TRAINING",
                "OTHER"
            ]
        },
        "departmentAndCostUnit": {
            "description": "Department/ cost unit can only be set in combination with hiring reason REPLACEMENT_TRANSFER",
            "type": ["string", "null"]
        },
        "nameAndStaffNumber": {
            "description": "Name/ staff number can only be set in combination with hiring reasons REPLACEMENT_TERMINATION, REPLACEMENT_TRANSFER and TEMPORARY_SUBSTITUTE",
            "type": ["string", "null"]
        },
        "reason": {
            "description": "Reason can only be set in combination with hiring reasons TRAINING, EXPANSION, OTHER, RENEWAL_OR_EXTENSION_OF_CONTRACT, TEMPORARY_SUBSTITUTE and ADDITIONAL_REQUIREMENT",
            "type": ["string", "null"]
        },
        "substituteDateFrom": {
            "description": "Substition start date can only be set in combination with hiring reason TEMPORARY_SUBSTITUTE. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "substituteDateTo": {
            "description": "Substition end date can only be set in combination with hiring reason TEMPORARY_SUBSTITUTE. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "terminationDate": {
            "description": "Termination date can only be set in combination with hiring reason REPLACEMENT_TERMINATION. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "transferDate": {
            "description": "Transfer date can only be set in combination with hiring reason REPLACEMENT_TRANSFER. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "area": {
            "description": "Area",
            "type": ["string", "null"]
        },
        "costUnit": {
            "description": "Cost unit",
            "type": ["string", "null"]
        },
        "department": {
            "description": "Department",
            "type": ["string", "null"]
        },
        "profile": {
            "description": "Requirements",
            "type": ["string", "null"]
        },
        "remark": {
            "description": "Remark",
            "type": ["string", "null"]
        },
        "salary": {
            "description": "Wage/ salary range",
            "type": ["string", "null"]
        },
        "tasks": {
            "description": "Tasks",
            "type": ["string", "null"]
        },
        "vacancyNumber": {
            "description": "Vacancy number",
            "type": ["string", "null"]
        },
        "budgeted": {
            "description": "Budgeted",
            "type": ["boolean", "null"]
        },
        "earliestEntryDate": {
            "description": "Planned starting date. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "locationIds": {
            "description": "Internal name of location",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "workingTimeIds": {
            "description": "Internal name of working time",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "formFields": {
            "description": "List of answered form fields. Form field types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
            "items": {
                "properties": {
                    "answers": {
                        "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "answer": {
                                    "type": "string"
                                }
                            }
                        },
                        "type": "array"
                    },
                    "answer": {
                        "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                        "type": "string"
                    },
                    "displayName": {
                        "description": "Display name of form field",
                        "type": "string"
                    },
                    "id": {
                        "description": "Identifier of form field",
                        "type": "string"
                    },
                    "type": {
                        "description": "Type of the form field",
                        "enum": [
                            "TEXT",
                            "TEXT_4_120",
                            "TEXTAREA",
                            "TEXTAREA_MAX_1200",
                            "FIVE_STAR_RATING",
                            "YES_NO",
                            "YES_NO_NOT_SPECIFIED",
                            "SINGLE_CHOICE",
                            "MULTI_CHOICE"
                        ]
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": [
        "id",
        "version",
        "jobTitle",
        "orgUnitId",
        "superiorId",
        "hrContactId"
    ]
}
```

### PUT /hiringRequests/{id}

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "jobTitle": {
            "description": "Job title of the hiring request",
            "type": "string"
        },
        "superiorId": {
            "description": "The dvinci user who is superior of the hiring request",
            "type": "integer"
        },
        "hrContactId": {
            "description": "The dvinci user who is HR contact of the hiring request",
            "type": "integer"
        },
        "companyId": {
            "description": "Internal name of company",
            "type": ["string", "null"]
        },
        "contractPeriodId": {
            "description": "Internal name of contract period",
            "type": ["string", "null"]
        },
        "functionGroupId": {
            "description": "Id of function group",
            "type": ["string", "null"]
        },
        "occupationalGroupId": {
            "description": "Id of occupational group",
            "type": ["string", "null"]
        },
        "payGradeId": {
            "description": "Id of pay grade",
            "type": ["string", "null"]
        },
        "openingsCount": {
            "description": "Number of openings",
            "type": ["integer", "null"]
        },
        "hiringReason": {
            "description": "Hiring reason",
            "enum": [
                "ADDITIONAL_REQUIREMENT",
                "EXPANSION",
                "REPLACEMENT_TERMINATION",
                "REPLACEMENT_TRANSFER",
                "TEMPORARY_SUBSTITUTE",
                "RENEWAL_OR_EXTENSION_OF_CONTRACT",
                "TRAINING",
                "OTHER"
            ]
        },
        "departmentAndCostUnit": {
            "description": "Department/ cost unit can only be set in combination with hiring reason REPLACEMENT_TRANSFER",
            "type": ["string", "null"]
        },
        "nameAndStaffNumber": {
            "description": "Name/ staff number can only be set in combination with hiring reasons REPLACEMENT_TERMINATION, REPLACEMENT_TRANSFER and TEMPORARY_SUBSTITUTE",
            "type": ["string", "null"]
        },
        "reason": {
            "description": "Reason can only be set in combination with hiring reasons TRAINING, EXPANSION, OTHER, RENEWAL_OR_EXTENSION_OF_CONTRACT, TEMPORARY_SUBSTITUTE and ADDITIONAL_REQUIREMENT",
            "type": ["string", "null"]
        },
        "substituteDateFrom": {
            "description": "Substition start date can only be set in combination with hiring reason TEMPORARY_SUBSTITUTE. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "substituteDateTo": {
            "description": "Substition end date can only be set in combination with hiring reason TEMPORARY_SUBSTITUTE. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "terminationDate": {
            "description": "Termination date can only be set in combination with hiring reason REPLACEMENT_TERMINATION. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "transferDate": {
            "description": "Transfer date can only be set in combination with hiring reason REPLACEMENT_TRANSFER. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "area": {
            "description": "Area",
            "type": ["string", "null"]
        },
        "costUnit": {
            "description": "Cost unit",
            "type": ["string", "null"]
        },
        "department": {
            "description": "Department",
            "type": ["string", "null"]
        },
        "profile": {
            "description": "Requirements",
            "type": ["string", "null"]
        },
        "remark": {
            "description": "Remark",
            "type": ["string", "null"]
        },
        "salary": {
            "description": "Wage/ salary range",
            "type": ["string", "null"]
        },
        "tasks": {
            "description": "Tasks",
            "type": ["string", "null"]
        },
        "vacancyNumber": {
            "description": "Vacancy number",
            "type": ["string", "null"]
        },
        "budgeted": {
            "description": "Budgeted",
            "type": ["boolean", "null"]
        },
        "earliestEntryDate": {
            "description": "Planned starting date. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "locationIds": {
            "description": "Internal name of location",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "workingTimeIds": {
            "description": "Internal name of working time",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "formFields": {
            "description": "List of answered form fields. Form field types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
            "items": {
                "properties": {
                    "answers": {
                        "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "answer": {
                                    "type": "string"
                                }
                            }
                        },
                        "type": "array"
                    },
                    "answer": {
                        "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                        "type": "string"
                    },
                    "displayName": {
                        "description": "Display name of form field",
                        "type": "string"
                    },
                    "id": {
                        "description": "Identifier of form field",
                        "type": "string"
                    },
                    "type": {
                        "description": "Type of the form field",
                        "enum": [
                            "TEXT",
                            "TEXT_4_120",
                            "TEXTAREA",
                            "TEXTAREA_MAX_1200",
                            "FIVE_STAR_RATING",
                            "YES_NO",
                            "YES_NO_NOT_SPECIFIED",
                            "SINGLE_CHOICE",
                            "MULTI_CHOICE"
                        ]
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": [
        "version",
        "jobTitle",
        "orgUnitId",
        "superiorId",
        "hrContactId"
    ]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "jobTitle": {
            "description": "Job title of the hiring request",
            "type": "string"
        },
        "dateCreated": {
            "description": "The creation-date of the hiring request",
            "type": "string",
            "format": "date-time"
        },
        "orgUnitId": {
            "description": "OrgUnitId cannot be changed for an existing hiring request",
            "type": "integer"
        },
        "hiringRequestCreatorId": {
            "description": "The dvinci user who has created the hiring request. Value cannot be set by rest api.",
            "type": "integer"
        },
        "status": {
            "description": "Status cannot be changed to FINISHED by rest api",
            "enum": ["OPEN", "IN_APPROVAL", "FINISHED"]
        },
        "superiorId": {
            "description": "The dvinci user who is superior of the hiring request",
            "type": "integer"
        },
        "hrContactId": {
            "description": "The dvinci user who is HR contact of the hiring request",
            "type": "integer"
        },
        "approvalStatus": {
            "description": "Approval status cannot be set or changed by rest api",
            "enum": ["NONE", "APPROVED", "REJECTED"]
        },
        "approvalProcessStarterId": {
            "description": "The dvinci user who started the hiring request approval process. Value cannot be set or changed by rest api.",
            "type": ["integer", "null"]
        },
        "companyId": {
            "description": "Internal name of company",
            "type": ["string", "null"]
        },
        "contractPeriodId": {
            "description": "Internal name of contract period",
            "type": ["string", "null"]
        },
        "functionGroupId": {
            "description": "Id of function group",
            "type": ["string", "null"]
        },
        "occupationalGroupId": {
            "description": "Id of occupational group",
            "type": ["string", "null"]
        },
        "payGradeId": {
            "description": "Id of pay grade",
            "type": ["string", "null"]
        },
        "openingsCount": {
            "description": "Number of openings",
            "type": ["integer", "null"]
        },
        "hiringReason": {
            "description": "Hiring reason",
            "enum": [
                "ADDITIONAL_REQUIREMENT",
                "EXPANSION",
                "REPLACEMENT_TERMINATION",
                "REPLACEMENT_TRANSFER",
                "TEMPORARY_SUBSTITUTE",
                "RENEWAL_OR_EXTENSION_OF_CONTRACT",
                "TRAINING",
                "OTHER"
            ]
        },
        "departmentAndCostUnit": {
            "description": "Department/ cost unit can only be set in combination with hiring reason REPLACEMENT_TRANSFER",
            "type": ["string", "null"]
        },
        "nameAndStaffNumber": {
            "description": "Name/ staff number can only be set in combination with hiring reasons REPLACEMENT_TERMINATION, REPLACEMENT_TRANSFER and TEMPORARY_SUBSTITUTE",
            "type": ["string", "null"]
        },
        "reason": {
            "description": "Reason can only be set in combination with hiring reasons TRAINING, EXPANSION, OTHER, RENEWAL_OR_EXTENSION_OF_CONTRACT, TEMPORARY_SUBSTITUTE and ADDITIONAL_REQUIREMENT",
            "type": ["string", "null"]
        },
        "substituteDateFrom": {
            "description": "Substition start date can only be set in combination with hiring reason TEMPORARY_SUBSTITUTE. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "substituteDateTo": {
            "description": "Substition end date can only be set in combination with hiring reason TEMPORARY_SUBSTITUTE. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "terminationDate": {
            "description": "Termination date can only be set in combination with hiring reason REPLACEMENT_TERMINATION. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "transferDate": {
            "description": "Transfer date can only be set in combination with hiring reason REPLACEMENT_TRANSFER. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "area": {
            "description": "Area",
            "type": ["string", "null"]
        },
        "costUnit": {
            "description": "Cost unit",
            "type": ["string", "null"]
        },
        "department": {
            "description": "Department",
            "type": ["string", "null"]
        },
        "profile": {
            "description": "Requirements",
            "type": ["string", "null"]
        },
        "remark": {
            "description": "Remark",
            "type": ["string", "null"]
        },
        "salary": {
            "description": "Wage/ salary range",
            "type": ["string", "null"]
        },
        "tasks": {
            "description": "Tasks",
            "type": ["string", "null"]
        },
        "vacancyNumber": {
            "description": "Vacancy number",
            "type": ["string", "null"]
        },
        "budgeted": {
            "description": "Budgeted",
            "type": ["boolean", "null"]
        },
        "earliestEntryDate": {
            "description": "Planned starting date. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "locationIds": {
            "description": "Internal name of location",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "workingTimeIds": {
            "description": "Internal name of working time",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "formFields": {
            "description": "List of answered form fields. Form field types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
            "items": {
                "properties": {
                    "answers": {
                        "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "answer": {
                                    "type": "string"
                                }
                            }
                        },
                        "type": "array"
                    },
                    "answer": {
                        "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                        "type": "string"
                    },
                    "displayName": {
                        "description": "Display name of form field",
                        "type": "string"
                    },
                    "id": {
                        "description": "Identifier of form field",
                        "type": "string"
                    },
                    "type": {
                        "description": "Type of the form field",
                        "enum": [
                            "TEXT",
                            "TEXT_4_120",
                            "TEXTAREA",
                            "TEXTAREA_MAX_1200",
                            "FIVE_STAR_RATING",
                            "YES_NO",
                            "YES_NO_NOT_SPECIFIED",
                            "SINGLE_CHOICE",
                            "MULTI_CHOICE"
                        ]
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": [
        "id",
        "version",
        "jobTitle",
        "orgUnitId",
        "superiorId",
        "hrContactId"
    ]
}
```

### GET /hiringRequests/{id}/history

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "comment": {
                "description": "The comment of the history entry",
                "type": ["string", "null"]
            },
            "dateCreated": {
                "description": "The creation-date of the history entry",
                "type": "string",
                "format": "date-time"
            },
            "description": {
                "description": "The human readable description of the history entry",
                "type": "string"
            },
            "dvinciUserId": {
                "description": "The dvinci user who has triggered the history entry",
                "type": "integer"
            },
            "type": {
                "description": "The type of the history entry.",
                "enum": [
                    "HIRING_REQUEST_CREATE",
                    "HIRING_REQUEST_UPDATE",
                    "HIRING_REQUEST_FINISH",
                    "HIRING_REQUEST_APPROVAL_START",
                    "HIRING_REQUEST_APPROVAL_ABORT",
                    "HIRING_REQUEST_APPROVAL_APPROVE",
                    "HIRING_REQUEST_APPROVAL_REJECT",
                    "HIRING_REQUEST_APPROVAL_DECISIONS_CANCELED",
                    "HIRING_REQUEST_APPROVER_ADD",
                    "HIRING_REQUEST_APPROVER_REPLACE",
                    "HIRING_REQUEST_APPROVER_DELETE",
                    "HIRING_REQUEST_DOCUMENT_CREATE",
                    "HIRING_REQUEST_DOCUMENT_DELETE",
                    "HIRING_REQUEST_COMMENT"
                ]
            }
        },
        "required": ["dateCreated", "type", "description", "dvinciUserId"]
    }
}
```

### GET /hiringRequests/{id}/approvers

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {
                "description": "Dvinci user id",
                "type": "integer"
            },
            "sequence": {
                "description": "Sequence within the approvers list",
                "type": "integer"
            },
            "processState": {
                "description": "Process state set by approver",
                "enum": ["DEFAULT", "NEXT", "APPROVED", "REJECTED"]
            }
        },
        "required": ["id", "sequence", "processState"]
    }
}
```

## Job openings

### GET /jobOpenings/

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {
                "description": "Property is not settable - only returned by the system",
                "type": "integer"
            },
            "version": {
                "description": "Mandatory for all PUT requests",
                "type": "integer"
            },
            "name": {
                "description": "Name or main title of the job opening",
                "type": "string"
            },
            "orgUnitId": {
                "description": "OrgUnitId cannot be changed for an existing job opening",
                "type": "integer"
            },
            "earliestEntryDate": {
                "type": ["string", "null"]
            },
            "responsibleUserId": {
                "type": "integer"
            },
            "department": {
                "type": ["string", "null"]
            },
            "contractPeriod": {
                "description": "Only internalNames defined in master data set by internal user are allowed. New systems contains: LIMITED, UNLIMITED",
                "type": ["string", "null"]
            },
            "reference": {
                "type": ["string", "null"]
            },
            "reward": {
                "type": ["string", "null"]
            },
            "costUnit": {
                "type": ["string", "null"]
            },
            "type": {
                "description": "Defines the type of the job opening (default value = 'DEFAULT'). Job openings with type 'MANAGED_BY_API' are for managing in external systems.",
                "enum": ["MANAGED_BY_API", "DEFAULT", "UNSOLICITED"]
            },
            "status": {
                "description": "Status cannot be changed to CLOSED by rest api",
                "enum": ["ACTIVE", "INACTIVE", "CLOSED"]
            },
            "companyId": {
                "type": ["string", "null"]
            },
            "userGroupIds": {
                "type": "array",
                "items": {
                    "type": "integer"
                }
            },
            "categoryIds": {
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
            "locationIds": {
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
            "targetGroups": {
                "description": "Only internalNames defined in master data set by internal user are allowed. New systems contains: PROFESSIONALS, GRADUATES, STUDENTS, PUPILS, OTHERS",
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
            "workingTimes": {
                "description": "Only internalNames defined in master data set by internal user are allowed. New systems contains: FULL_TIME, PART_TIME, MARGINAL_EMPLOYMENT",
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
            "externalLinks": {
                "type": "array",
                "description": "These links are rendered as buttons to the actionbar in the show view of this specific job opening, e.g. deep back-links to your system.",
                "properties": {
                    "label": {
                        "type": "string"
                    },
                    "url": {
                        "description": "Url of the external system. Has to start with 'http(s)://'",
                        "type": "string"
                    },
                    "faIcon": {
                        "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'. When none given, 'fa-external-link' will be used as icon",
                        "type": "string"
                    }
                },
                "required": ["label", "url"]
            },
            "externalId": {
                "description": "Can be used to identify this resource in other systems. Must be unique or null.",
                "type": ["string", "null"]
            },
            "jobOpeningUrl": {
                "description": "Deep link to the jobOpening in the d.vinci system,",
                "type": "string"
            },
            "applicationListUrl": {
                "description": "Deep link to the list of application for the given job opening in the d.vinci system",
                "type": "string"
            },
            "jobPublications": {
                "description": "A 'DEFAULT' or 'UNSOLICITED' job opening can have more than one job publications. 'MANAGED_BY_API' contains only one job publication.",
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "position": {
                            "description": "Title of the job publication",
                            "type": "string"
                        },
                        "applicationFormUrls": {
                            "description": "List of links to application form for different application portals. First link of list is the default one, others sorted by org unit level.",
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "languageId": {
                            "description": "IsoA2 code of the requested language. Eg. 'de', 'en'. Property is only available for job openings with type 'DEFAULT' or 'UNSOLICITED'.",
                            "type": "string"
                        }
                    }
                }
            },
            "formFields": {
                "description": "List of answered form fields. Form field types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
                "items": {
                    "properties": {
                        "answers": {
                            "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                            "items": {
                                "properties": {
                                    "id": {
                                        "type": "string"
                                    },
                                    "answer": {
                                        "type": "string"
                                    }
                                }
                            },
                            "type": "array"
                        },
                        "answer": {
                            "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                            "type": "string"
                        },
                        "displayName": {
                            "description": "Display name of form field",
                            "type": "string"
                        },
                        "id": {
                            "description": "Identifier of form field",
                            "type": "string"
                        },
                        "type": {
                            "description": "Type of the form field",
                            "enum": [
                                "TEXT",
                                "TEXT_4_120",
                                "TEXTAREA",
                                "TEXTAREA_MAX_1200",
                                "FIVE_STAR_RATING",
                                "YES_NO",
                                "YES_NO_NOT_SPECIFIED",
                                "SINGLE_CHOICE",
                                "MULTI_CHOICE"
                            ]
                        }
                    },
                    "type": "object"
                },
                "type": "array"
            }
        },
        "required": ["name", "responsibleUserId", "status", "orgUnitId"]
    }
}
```

### POST /jobOpenings/

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "name": {
            "description": "Name or main title of the job opening",
            "type": "string"
        },
        "orgUnitId": {
            "description": "OrgUnitId cannot be changed for an existing job opening",
            "type": "integer"
        },
        "earliestEntryDate": {
            "description": "earliestEntryDate has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' earliestEntryDate can't be null.",
            "type": "string"
        },
        "responsibleUserId": {
            "type": "integer"
        },
        "department": {
            "description": "Department has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' department can't be null.",
            "type": "string"
        },
        "contractPeriod": {
            "description": "Only internalNames defined in master data set by internal user are allowed. New systems contains: LIMITED, UNLIMITED. It has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' contractPeriod can't be null.",
            "type": "string"
        },
        "reference": {
            "description": "Reference has one of following field types: 'GENERATED', 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' reference can't be null. In case of 'GENERATED' the value will be generated by the system.",
            "type": "string"
        },
        "reward": {
            "description": "Reward has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' reward can't be null.",
            "type": "string"
        },
        "costUnit": {
            "description": "CostUnit has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' costUnit can't be null.",
            "type": "string"
        },
        "type": {
            "description": "Defines the type of the job opening. Job openings with type 'MANAGED_BY_API' are for managing in external systems.",
            "enum": ["MANAGED_BY_API", "DEFAULT", "UNSOLICITED"]
        },
        "status": {
            "description": "Status cannot be changed to CLOSED by rest api",
            "enum": ["ACTIVE", "INACTIVE", "CLOSED"]
        },
        "companyId": {
            "type": ["string", "null"]
        },
        "userGroupIds": {
            "type": "array",
            "items": {
                "type": "integer"
            }
        },
        "categoryIds": {
            "description": "CategoryIds has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' categoryIds can't be null.",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "locationIds": {
            "description": "LocationIds has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' locationIds can't be null.",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "targetGroups": {
            "description": "Only internalNames defined in master data set by internal user are allowed. New systems contains: PROFESSIONALS, GRADUATES, STUDENTS, PUPILS, OTHERS. It has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' targetGroups can't be null.",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "workingTimes": {
            "description": "Only internalNames defined in master data set by internal user are allowed. New systems contains: FULL_TIME, PART_TIME, MARGINAL_EMPLOYMENT. It has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' workingTimes can't be null.",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "externalLinks": {
            "type": "array",
            "description": "These links are rendered as buttons to the actionbar in the show view of this specific job opening, e.g. deep back-links to your system.",
            "properties": {
                "label": {
                    "type": "string"
                },
                "url": {
                    "description": "Url of the external system. Has to start with 'http(s)://'",
                    "type": "string"
                },
                "faIcon": {
                    "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'. When none given, 'fa-external-link' will be used as icon",
                    "type": "string"
                }
            },
            "required": ["label", "url"]
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "formFields": {
            "description": "List of answered form fields. Form field types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
            "items": {
                "properties": {
                    "answers": {
                        "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "string"
                                }
                            }
                        },
                        "type": "array"
                    },
                    "answer": {
                        "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                        "type": "string"
                    },
                    "id": {
                        "description": "Identifier of form field",
                        "type": "string"
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": ["name", "responsibleUserId", "status", "orgUnitId", "type"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "name": {
            "description": "Name or main title of the job opening",
            "type": "string"
        },
        "orgUnitId": {
            "description": "OrgUnitId cannot be changed for an existing job opening",
            "type": "integer"
        },
        "earliestEntryDate": {
            "type": ["string", "null"]
        },
        "responsibleUserId": {
            "type": "integer"
        },
        "department": {
            "type": ["string", "null"]
        },
        "contractPeriod": {
            "description": "Only internalNames defined in master data set by internal user are allowed. New systems contains: LIMITED, UNLIMITED",
            "type": ["string", "null"]
        },
        "reference": {
            "type": ["string", "null"]
        },
        "reward": {
            "type": ["string", "null"]
        },
        "costUnit": {
            "type": ["string", "null"]
        },
        "type": {
            "description": "Defines the type of the job opening (default value = 'DEFAULT'). Job openings with type 'MANAGED_BY_API' are for managing in external systems.",
            "enum": ["MANAGED_BY_API", "DEFAULT", "UNSOLICITED"]
        },
        "status": {
            "description": "Status cannot be changed to CLOSED by rest api",
            "enum": ["ACTIVE", "INACTIVE", "CLOSED"]
        },
        "companyId": {
            "type": ["string", "null"]
        },
        "userGroupIds": {
            "type": "array",
            "items": {
                "type": "integer"
            }
        },
        "categoryIds": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "locationIds": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "targetGroups": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "workingTimes": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "externalLinks": {
            "type": "array",
            "items": {
                "properties": {
                    "label": {
                        "type": "string"
                    },
                    "url": {
                        "type": "string"
                    },
                    "faIcon": {
                        "type": "string"
                    }
                }
            }
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "jobOpeningUrl": {
            "description": "Deep link to the jobOpening in the d.vinci system,",
            "type": "string"
        },
        "applicationListUrl": {
            "description": "Deep link to the list of application for the given job opening in the d.vinci system",
            "type": "string"
        },
        "jobPublications": {
            "description": "A 'DEFAULT' or 'UNSOLICITED' job opening can have more than one job publications. 'MANAGED_BY_API' contains only one job publication.",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "position": {
                        "description": "Title of the job publication",
                        "type": "string"
                    },
                    "applicationFormUrls": {
                        "description": "List of links to application form for different application portals. First link of list is the default one, others sorted by org unit level.",
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "languageId": {
                        "description": "IsoA2 code of the requested language. Eg. 'de', 'en'. Property is only available for job openings with type 'DEFAULT' or 'UNSOLICITED'.",
                        "type": "string"
                    }
                }
            }
        },
        "formFields": {
            "description": "List of answered form fields. Form field types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
            "items": {
                "properties": {
                    "answers": {
                        "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "string"
                                }
                            }
                        },
                        "type": "array"
                    },
                    "answer": {
                        "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                        "type": "string"
                    },
                    "id": {
                        "description": "Identifier of form field",
                        "type": "string"
                    }
                }
            }
        }
    }
}
```

### GET /jobOpenings/?externalId={externalId}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "name": {
            "description": "Name or main title of the job opening",
            "type": "string"
        },
        "orgUnitId": {
            "description": "OrgUnitId cannot be changed for an existing job opening",
            "type": "integer"
        },
        "earliestEntryDate": {
            "type": ["string", "null"]
        },
        "responsibleUserId": {
            "type": "integer"
        },
        "department": {
            "type": ["string", "null"]
        },
        "contractPeriod": {
            "description": "Only internalNames defined in master data set by internal user are allowed. New systems contains: LIMITED, UNLIMITED",
            "type": ["string", "null"]
        },
        "reference": {
            "type": ["string", "null"]
        },
        "reward": {
            "type": ["string", "null"]
        },
        "costUnit": {
            "type": ["string", "null"]
        },
        "type": {
            "description": "Defines the type of the job opening (default value = 'DEFAULT'). Job openings with type 'MANAGED_BY_API' are for managing in external systems.",
            "enum": ["MANAGED_BY_API", "DEFAULT", "UNSOLICITED"]
        },
        "status": {
            "description": "Status cannot be changed to CLOSED by rest api",
            "enum": ["ACTIVE", "INACTIVE", "CLOSED"]
        },
        "companyId": {
            "type": ["string", "null"]
        },
        "userGroupIds": {
            "type": "array",
            "items": {
                "type": "integer"
            }
        },
        "categoryIds": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "locationIds": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "targetGroups": {
            "description": "Only internalNames defined in master data set by internal user are allowed. New systems contains: PROFESSIONALS, GRADUATES, STUDENTS, PUPILS, OTHERS",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "workingTimes": {
            "description": "Only internalNames defined in master data set by internal user are allowed. New systems contains: FULL_TIME, PART_TIME, MARGINAL_EMPLOYMENT",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "externalLinks": {
            "type": "array",
            "description": "These links are rendered as buttons to the actionbar in the show view of this specific job opening, e.g. deep back-links to your system.",
            "properties": {
                "label": {
                    "type": "string"
                },
                "url": {
                    "description": "Url of the external system. Has to start with 'http(s)://'",
                    "type": "string"
                },
                "faIcon": {
                    "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'. When none given, 'fa-external-link' will be used as icon",
                    "type": "string"
                }
            },
            "required": ["label", "url"]
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "jobOpeningUrl": {
            "description": "Deep link to the jobOpening in the d.vinci system,",
            "type": "string"
        },
        "applicationListUrl": {
            "description": "Deep link to the list of application for the given job opening in the d.vinci system",
            "type": "string"
        },
        "jobPublications": {
            "description": "A 'DEFAULT' or 'UNSOLICITED' job opening can have more than one job publications. 'MANAGED_BY_API' contains only one job publication.",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "position": {
                        "description": "Title of the job publication",
                        "type": "string"
                    },
                    "applicationFormUrls": {
                        "description": "List of links to application form for different application portals. First link of list is the default one, others sorted by org unit level.",
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "languageId": {
                        "description": "IsoA2 code of the requested language. Eg. 'de', 'en'. Property is only available for job opening with type 'DEFAULT' or 'UNSOLICITED'.",
                        "type": "string"
                    }
                }
            }
        },
        "formFields": {
            "description": "List of answered form fields. Form field types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
            "items": {
                "properties": {
                    "answers": {
                        "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "answer": {
                                    "type": "string"
                                }
                            }
                        },
                        "type": "array"
                    },
                    "answer": {
                        "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                        "type": "string"
                    },
                    "displayName": {
                        "description": "Display name of form field",
                        "type": "string"
                    },
                    "id": {
                        "description": "Identifier of form field",
                        "type": "string"
                    },
                    "type": {
                        "description": "Type of the form field",
                        "enum": [
                            "TEXT",
                            "TEXT_4_120",
                            "TEXTAREA",
                            "TEXTAREA_MAX_1200",
                            "FIVE_STAR_RATING",
                            "YES_NO",
                            "YES_NO_NOT_SPECIFIED",
                            "SINGLE_CHOICE",
                            "MULTI_CHOICE"
                        ]
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": ["name", "responsibleUserId", "status", "orgUnitId"]
}
```

### GET /jobOpenings/{id}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "name": {
            "description": "Name or main title of the job opening",
            "type": "string"
        },
        "orgUnitId": {
            "description": "OrgUnitId cannot be changed for an existing job opening",
            "type": "integer"
        },
        "earliestEntryDate": {
            "type": ["string", "null"]
        },
        "responsibleUserId": {
            "type": "integer"
        },
        "department": {
            "type": ["string", "null"]
        },
        "contractPeriod": {
            "description": "Only internalNames defined in master data set by internal user are allowed. New systems contains: LIMITED, UNLIMITED",
            "type": ["string", "null"]
        },
        "reference": {
            "type": ["string", "null"]
        },
        "reward": {
            "type": ["string", "null"]
        },
        "costUnit": {
            "type": ["string", "null"]
        },
        "type": {
            "description": "Defines the type of the job opening (default value = 'DEFAULT'). Job openings with type 'MANAGED_BY_API' are for managing in external systems.",
            "enum": ["MANAGED_BY_API", "DEFAULT", "UNSOLICITED"]
        },
        "status": {
            "description": "Status cannot be changed to CLOSED by rest api",
            "enum": ["ACTIVE", "INACTIVE", "CLOSED"]
        },
        "companyId": {
            "type": ["string", "null"]
        },
        "userGroupIds": {
            "type": "array",
            "items": {
                "type": "integer"
            }
        },
        "categoryIds": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "locationIds": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "targetGroups": {
            "description": "Only internalNames defined in master data set by internal user are allowed. New systems contains: PROFESSIONALS, GRADUATES, STUDENTS, PUPILS, OTHERS",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "workingTimes": {
            "description": "Only internalNames defined in master data set by internal user are allowed. New systems contains: FULL_TIME, PART_TIME, MARGINAL_EMPLOYMENT",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "externalLinks": {
            "type": "array",
            "description": "These links are rendered as buttons to the actionbar in the show view of this specific job opening, e.g. deep back-links to your system.",
            "properties": {
                "label": {
                    "type": "string"
                },
                "url": {
                    "description": "Url of the external system. Has to start with 'http(s)://'",
                    "type": "string"
                },
                "faIcon": {
                    "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'. When none given, 'fa-external-link' will be used as icon",
                    "type": "string"
                }
            },
            "required": ["label", "url"]
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "jobOpeningUrl": {
            "description": "Deep link to the jobOpening in the d.vinci system,",
            "type": "string"
        },
        "applicationListUrl": {
            "description": "Deep link to the list of application for the given job opening in the d.vinci system",
            "type": "string"
        },
        "jobPublications": {
            "description": "A 'DEFAULT' or 'UNSOLICITED' job opening can have more than one job publications. 'MANAGED_BY_API' contains only one job publication.",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "position": {
                        "description": "Title of the job publication",
                        "type": "string"
                    },
                    "applicationFormUrls": {
                        "description": "List of links to application form for different application portals. First link of list is the default one, others sorted by org unit level.",
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "languageId": {
                        "description": "IsoA2 code of the requested language. Eg. 'de', 'en'. Property is only available for job opening with type 'DEFAULT' or 'UNSOLICITED'.",
                        "type": "string"
                    }
                }
            }
        },
        "formFields": {
            "description": "List of answered form fields. Form field types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
            "items": {
                "properties": {
                    "answers": {
                        "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "answer": {
                                    "type": "string"
                                }
                            }
                        },
                        "type": "array"
                    },
                    "answer": {
                        "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                        "type": "string"
                    },
                    "displayName": {
                        "description": "Display name of form field",
                        "type": "string"
                    },
                    "id": {
                        "description": "Identifier of form field",
                        "type": "string"
                    },
                    "type": {
                        "description": "Type of the form field",
                        "enum": [
                            "TEXT",
                            "TEXT_4_120",
                            "TEXTAREA",
                            "TEXTAREA_MAX_1200",
                            "FIVE_STAR_RATING",
                            "YES_NO",
                            "YES_NO_NOT_SPECIFIED",
                            "SINGLE_CHOICE",
                            "MULTI_CHOICE"
                        ]
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": ["name", "responsibleUserId", "status", "orgUnitId"]
}
```

### PUT /jobOpenings/{id}

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "name": {
            "description": "Name or main title of the job opening",
            "type": "string"
        },
        "earliestEntryDate": {
            "description": "EarliestEntryDate has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' earliestEntryDate can't be null.",
            "type": "string"
        },
        "responsibleUserId": {
            "type": "integer"
        },
        "department": {
            "description": "Department has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' department can't be null.",
            "type": "string"
        },
        "contractPeriod": {
            "description": "Only internalNames defined in master data set by internal user are allowed. New systems contains: LIMITED, UNLIMITED. It has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' contractPeriod can't be null.",
            "type": "string"
        },
        "reference": {
            "description": "Reference has one of following field types: 'GENERATED', 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' reference can't be null. In case of 'GENERATED' the value will be generated by the system.",
            "type": "string"
        },
        "reward": {
            "description": "Reward has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' reward can't be null.",
            "type": "string"
        },
        "costUnit": {
            "description": "CostUnit has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' costUnit can't be null.",
            "type": "string"
        },
        "status": {
            "description": "Status cannot be changed to CLOSED by rest api",
            "enum": ["ACTIVE", "INACTIVE", "CLOSED"]
        },
        "companyId": {
            "type": ["string", "null"]
        },
        "userGroupIds": {
            "type": "array",
            "items": {
                "type": "integer"
            }
        },
        "categoryIds": {
            "description": "CategoryIds has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' categoryIds can't be null.",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "locationIds": {
            "description": "LocationIds has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' locationIds can't be null.",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "targetGroups": {
            "description": "Only internalNames defined in master data set by internal user are allowed. New systems contains: PROFESSIONALS, GRADUATES, STUDENTS, PUPILS, OTHERS. It has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' targetGroups can't be null.",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "workingTimes": {
            "description": "Only internalNames defined in master data set by internal user are allowed. New systems contains: FULL_TIME, PART_TIME, MARGINAL_EMPLOYMENT. It has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' workingTimes can't be null.",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "externalLinks": {
            "type": "array",
            "description": "These links are rendered as buttons to the actionbar in the show view of this specific job opening, e.g. deep back-links to your system.",
            "properties": {
                "label": {
                    "type": "string"
                },
                "url": {
                    "description": "Url of the external system. Has to start with 'http(s)://'",
                    "type": "string"
                },
                "faIcon": {
                    "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'. When none given, 'fa-external-link' will be used as icon",
                    "type": "string"
                }
            },
            "required": ["label", "url"]
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "formFields": {
            "description": "List of answered form fields. Form field types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
            "items": {
                "properties": {
                    "answers": {
                        "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "string"
                                }
                            }
                        },
                        "type": "array"
                    },
                    "answer": {
                        "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                        "type": "string"
                    },
                    "id": {
                        "description": "Identifier of form field",
                        "type": "string"
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": ["version", "name", "responsibleUserId", "status"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "name": {
            "description": "Name or main title of the job opening",
            "type": "string"
        },
        "orgUnitId": {
            "description": "OrgUnitId cannot be changed for an existing job opening",
            "type": "integer"
        },
        "earliestEntryDate": {
            "type": ["string", "null"]
        },
        "responsibleUserId": {
            "type": "integer"
        },
        "department": {
            "type": ["string", "null"]
        },
        "contractPeriod": {
            "description": "Only internalNames defined in master data set by internal user are allowed. New systems contains: LIMITED, UNLIMITED",
            "type": ["string", "null"]
        },
        "reference": {
            "type": ["string", "null"]
        },
        "reward": {
            "type": ["string", "null"]
        },
        "costUnit": {
            "type": ["string", "null"]
        },
        "type": {
            "description": "Defines the type of the job opening (default value = 'DEFAULT'). Job openings with type 'MANAGED_BY_API' are for managing in external systems.",
            "enum": ["MANAGED_BY_API", "DEFAULT", "UNSOLICITED"]
        },
        "status": {
            "description": "Status cannot be changed to CLOSED by rest api",
            "enum": ["ACTIVE", "INACTIVE", "CLOSED"]
        },
        "companyId": {
            "type": ["string", "null"]
        },
        "userGroupIds": {
            "type": "array",
            "items": {
                "type": "integer"
            }
        },
        "categoryIds": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "locationIds": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "targetGroups": {
            "description": "Only internalNames defined in master data set by internal user are allowed. New systems contains: PROFESSIONALS, GRADUATES, STUDENTS, PUPILS, OTHERS",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "workingTimes": {
            "description": "Only internalNames defined in master data set by internal user are allowed. New systems contains: FULL_TIME, PART_TIME, MARGINAL_EMPLOYMENT",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "externalLinks": {
            "type": "array",
            "description": "These links are rendered as buttons to the actionbar in the show view of this specific job opening, e.g. deep back-links to your system.",
            "properties": {
                "label": {
                    "type": "string"
                },
                "url": {
                    "description": "Url of the external system. Has to start with 'http(s)://'",
                    "type": "string"
                },
                "faIcon": {
                    "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'. When none given, 'fa-external-link' will be used as icon",
                    "type": "string"
                }
            },
            "required": ["label", "url"]
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "jobOpeningUrl": {
            "description": "Deep link to the jobOpening in the d.vinci system,",
            "type": "string"
        },
        "applicationListUrl": {
            "description": "Deep link to the list of application for the given job opening in the d.vinci system",
            "type": "string"
        },
        "jobPublications": {
            "description": "A 'DEFAULT' or 'UNSOLICITED' job opening can have more than one job publications. 'MANAGED_BY_API' contains only one job publication.",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "position": {
                        "description": "Title of the job publication",
                        "type": "string"
                    },
                    "applicationFormUrls": {
                        "description": "List of links to application form for different application portals. First link of list is the default one, others sorted by org unit level.",
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "languageId": {
                        "description": "IsoA2 code of the requested language. Eg. 'de', 'en'. Property is only available for job opening with type 'DEFAULT' or 'UNSOLICITED'.",
                        "type": "string"
                    }
                }
            }
        },
        "formFields": {
            "description": "List of answered form fields. Form field types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED, SINGLE_CHOICE, MULTI_CHOICE",
            "items": {
                "properties": {
                    "answers": {
                        "description": "List of answers for types: SINGLE_CHOICE, MULTI_CHOICE",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "answer": {
                                    "type": "string"
                                }
                            }
                        },
                        "type": "array"
                    },
                    "answer": {
                        "description": "Answer of types: TEXT, TEXT_4_120, TEXTAREA, TEXTAREA_MAX_1200, FIVE_STAR_RATING, YES_NO, YES_NO_NOT_SPECIFIED",
                        "type": "string"
                    },
                    "displayName": {
                        "description": "Display name of form field",
                        "type": "string"
                    },
                    "id": {
                        "description": "Identifier of form field",
                        "type": "string"
                    },
                    "type": {
                        "description": "Type of the form field",
                        "enum": [
                            "TEXT",
                            "TEXT_4_120",
                            "TEXTAREA",
                            "TEXTAREA_MAX_1200",
                            "FIVE_STAR_RATING",
                            "YES_NO",
                            "YES_NO_NOT_SPECIFIED",
                            "SINGLE_CHOICE",
                            "MULTI_CHOICE"
                        ]
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": ["name", "responsibleUserId", "status", "orgUnitId"]
}
```

### GET /jobOpenings/{id}/history

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "comment": {
                "description": "The comment of the history entry",
                "type": ["string", "null"]
            },
            "dateCreated": {
                "description": "The creation-date of the history entry",
                "type": "string",
                "format": "date-time"
            },
            "description": {
                "description": "The human readable description of the history entry",
                "type": "string"
            },
            "dvinciUserId": {
                "description": "The dvinci user who has triggered the history entry",
                "type": "integer"
            },
            "externalId": {
                "description": "The unique identifier of the external system.",
                "type": ["string", "null"]
            },
            "externalUser": {
                "description": "A display name for a user, who does not exists in the dvinci system.",
                "type": ["string", "null"]
            },
            "type": {
                "description": "The type of the history entry.",
                "type": "string"
            }
        },
        "required": ["dateCreated", "type", "description", "dvinciUserId"]
    }
}
```

### PUT /jobOpenings/{id}/history

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "properties": {
        "dateCreated": {
            "description": "The creation-date of the history entry",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "description": {
            "description": "The description for the history entry",
            "type": "string"
        },
        "dvinciUserId": {
            "description": "The dvinci user who has triggered the history entry",
            "type": ["null", "integer"]
        },
        "externalUser": {
            "description": "A display name for a user, who does not exists in the dvinci system.",
            "type": ["string", "null"]
        },
        "externalId": {
            "description": "The unique identifier of the external system.",
            "type": "string"
        }
    },
    "required": ["description", "externalId"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "properties": {
        "comment": {
            "description": "The comment of the history entry",
            "type": ["string", "null"]
        },
        "dateCreated": {
            "description": "The creation-date of the history entry",
            "type": "string",
            "format": "date-time"
        },
        "description": {
            "description": "The human readable description of the history entry",
            "type": "string"
        },
        "dvinciUserId": {
            "description": "The dvinci user who has triggered the history entry",
            "type": "integer"
        },
        "externalId": {
            "description": "The unique identifier of the external system.",
            "type": ["string", "null"]
        },
        "externalUser": {
            "description": "A display name for a user, who does not exists in the dvinci system.",
            "type": ["string", "null"]
        },
        "type": {
            "description": "The type of the history entry.",
            "type": "string"
        }
    },
    "required": ["dateCreated", "type", "description", "dvinciUserId"]
}
```

### PUT /jobOpenings/{id}/history/{externalId}

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "dateCreated": {
            "description": "The creation-date of the history entry",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "description": {
            "description": "The description for the history entry",
            "type": "string"
        },
        "dvinciUserId": {
            "description": "The dvinci user who has triggered the history entry",
            "type": ["null", "integer"]
        },
        "externalUser": {
            "description": "A display name for a user, who does not exists in the dvinci system.",
            "type": ["string", "null"]
        }
    },
    "required": ["description"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "comment": {
            "description": "The comment of the history entry",
            "type": ["string", "null"]
        },
        "dateCreated": {
            "description": "The creation-date of the history entry",
            "type": "string",
            "format": "date-time"
        },
        "description": {
            "description": "The human readable description of the history entry",
            "type": "string"
        },
        "dvinciUserId": {
            "description": "The dvinci user who has triggered the history entry",
            "type": "integer"
        },
        "externalId": {
            "description": "The unique identifier of the external system.",
            "type": ["string", "null"]
        },
        "externalUser": {
            "description": "A display name for a user, who does not exists in the dvinci system.",
            "type": ["string", "null"]
        },
        "type": {
            "description": "The type of the history entry.",
            "type": "string"
        }
    },
    "required": ["dateCreated", "type", "description", "dvinciUserId"]
}
```

## Job publications

### GET /jobPublications/

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {
                "description": "Property is not settable - only returned by the system",
                "type": "integer"
            },
            "version": {
                "description": "Mandatory for all PUT requests",
                "type": "integer"
            },
            "type": {
                "description": "Defines the type of the job publication (default value = 'DEFAULT'). Job publications with type 'EXTERNAL' are only displayed in the job list and opened in new browser tab.",
                "enum": ["DEFAULT", "EXTERNAL"]
            },
            "jobOpeningId": {
                "type": "integer"
            },
            "position": {
                "description": "Name or position of the job publication",
                "type": "string"
            },
            "languageId": {
                "description": "IsoA2 code of the requested language. Eg. 'de', 'en'.",
                "type": "string"
            },
            "subtitle": {
                "type": ["string", "null"]
            },
            "introduction": {
                "description": "Publication introduction as HTML text.",
                "type": ["string", "null"]
            },
            "tasks": {
                "description": "Publication tasks as HTML text.",
                "type": ["string", "null"]
            },
            "profile": {
                "description": "Publication profile as HTML text.",
                "type": ["string", "null"]
            },
            "weOffer": {
                "description": "Publication we-offer as HTML text.",
                "type": ["string", "null"]
            },
            "closingText": {
                "description": "Publication closing text as HTML text.",
                "type": ["string", "null"]
            },
            "pageTitle": {
                "type": ["string", "null"]
            },
            "pageDescription": {
                "type": ["string", "null"]
            },
            "externalPublicationUrl": {
                "description": "Link to an external publication. Can only be set for type='EXTERNAL'",
                "type": ["string", "null"]
            },
            "externalId": {
                "description": "Can be used to identify this resource in other systems. Must be unique or null.",
                "type": ["string", "null"]
            },
            "status": {
                "description": "Defines the status of the job publication (default value = 'ACTIVE'). Status cannot be changed to IN_APPROVAL by REST API",
                "enum": ["ACTIVE", "DRAFT", "IN_APPROVAL"]
            },
            "placements": {
                "description": "List of placements that the job publication should be published on.",
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "channelId": {
                            "description": "Id of channel that should be published on. 'channelId' or 'internalName' are required.",
                            "type": "integer"
                        },
                        "internalName": {
                            "description": "Internal name of channel that should be published on. 'channelId' or 'internalName' are required.",
                            "type": ["string", "null"]
                        },
                        "startDate": {
                            "description": "Start date of publishing publication on defined channel. Can be 'null' or ISO8601 date-time format (yyyy-MM-dd'T'HH:mm:ss.SSSZZ).",
                            "type": ["string", "null"],
                            "format": "date-time"
                        },
                        "endDate": {
                            "description": "End date of publishing publication on defined channel. Can be 'null' or ISO8601 date-time format (yyyy-MM-dd'T'HH:mm:ss.SSSZZ).",
                            "type": ["string", "null"],
                            "format": "date-time"
                        }
                    }
                }
            }
        },
        "required": ["type", "jobOpeningId", "position", "languageId"]
    }
}
```

### POST /jobPublications/

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "type": {
            "description": "Defines the type of the job publication (default value = 'DEFAULT'). Job publications with type 'EXTERNAL' are only displayed in the job list and opened in new browser tab.",
            "enum": ["DEFAULT", "EXTERNAL"]
        },
        "jobOpeningId": {
            "type": "integer"
        },
        "position": {
            "description": "Name or position of the job publication",
            "type": "string"
        },
        "languageId": {
            "description": "IsoA2 code of the requested language. Eg. 'de', 'en'.",
            "type": "string"
        },
        "subtitle": {
            "description": "Subtitle has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' subtitle can't be null.",
            "type": ["string", "null"]
        },
        "introduction": {
            "description": "Publication introduction as HTML text. It has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' introduction can't be null.",
            "type": ["string", "null"]
        },
        "tasks": {
            "description": "Publication tasks as HTML text. It has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' tasks can't be null.",
            "type": ["string", "null"]
        },
        "profile": {
            "description": "Publication profile as HTML text. It has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' profile can't be null.",
            "type": ["string", "null"]
        },
        "weOffer": {
            "description": "Publication weOffer as HTML text. It has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' weOffer can't be null.",
            "type": ["string", "null"]
        },
        "closingText": {
            "description": "Publication closingText as HTML text. It has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' closingText can't be null.",
            "type": ["string", "null"]
        },
        "pageTitle": {
            "type": ["string", "null"]
        },
        "pageDescription": {
            "description": "PageDescription has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' pageDescription can't be null.",
            "type": ["string", "null"]
        },
        "externalPublicationUrl": {
            "description": "Link to an external publication. Can only be set for type='EXTERNAL'. It has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' externalPublicationUrl can't be null.",
            "type": ["string", "null"]
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "status": {
            "description": "Defines the status of the job publication (default value = 'ACTIVE').",
            "enum": ["ACTIVE", "DRAFT"]
        },
        "placements": {
            "description": "List of placements that the job publication should be published on.",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "channelId": {
                        "description": "Id of channel that should be published on. 'channelId' or 'internalName' are required.",
                        "type": "integer"
                    },
                    "internalName": {
                        "description": "Internal name of channel that should be published on. 'channelId' or 'internalName' are required.",
                        "type": ["string", "null"]
                    },
                    "startDate": {
                        "description": "Start date of publishing publication on defined channel. Can be 'null' or ISO8601 date-time format (yyyy-MM-dd'T'HH:mm:ss.SSSZZ).",
                        "type": ["string", "null"],
                        "format": "date-time"
                    },
                    "endDate": {
                        "description": "End date of publishing publication on defined channel. Can be 'null' or ISO8601 date-time format (yyyy-MM-dd'T'HH:mm:ss.SSSZZ).",
                        "type": ["string", "null"],
                        "format": "date-time"
                    }
                }
            }
        }
    },
    "required": ["type", "jobOpeningId", "position", "languageId"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "type": {
            "description": "Defines the type of the job publication (default value = 'DEFAULT'). Job publications with type 'EXTERNAL' are only displayed in the job list and opened in new browser tab.",
            "enum": ["DEFAULT", "EXTERNAL"]
        },
        "jobOpeningId": {
            "type": "integer"
        },
        "position": {
            "description": "Name or position of the job publication",
            "type": "string"
        },
        "languageId": {
            "description": "IsoA2 code of the requested language. Eg. 'de', 'en'.",
            "type": "string"
        },
        "subtitle": {
            "type": ["string", "null"]
        },
        "introduction": {
            "description": "Publication introduction as HTML text.",
            "type": ["string", "null"]
        },
        "tasks": {
            "description": "Publication tasks as HTML text.",
            "type": ["string", "null"]
        },
        "profile": {
            "description": "Publication profile as HTML text.",
            "type": ["string", "null"]
        },
        "weOffer": {
            "description": "Publication we-offer as HTML text.",
            "type": ["string", "null"]
        },
        "closingText": {
            "description": "Publication closing text as HTML text.",
            "type": ["string", "null"]
        },
        "pageTitle": {
            "type": ["string", "null"]
        },
        "pageDescription": {
            "type": ["string", "null"]
        },
        "externalPublicationUrl": {
            "description": "Link to an external publication. Can only be set for type='EXTERNAL'",
            "type": ["string", "null"]
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "status": {
            "description": "Defines the status of the job publication (default value = 'ACTIVE'). Status cannot be changed to IN_APPROVAL by REST API",
            "enum": ["ACTIVE", "DRAFT", "IN_APPROVAL"]
        },
        "placements": {
            "description": "List of placements that the job publication should be published on.",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "channelId": {
                        "description": "Id of channel that should be published on. 'channelId' or 'internalName' are required.",
                        "type": "integer"
                    },
                    "internalName": {
                        "description": "Internal name of channel that should be published on. 'channelId' or 'internalName' are required.",
                        "type": ["string", "null"]
                    },
                    "startDate": {
                        "description": "Start date of publishing publication on defined channel. Can be 'null' or ISO8601 date-time format (yyyy-MM-dd'T'HH:mm:ss.SSSZZ).",
                        "type": ["string", "null"],
                        "format": "date-time"
                    },
                    "endDate": {
                        "description": "End date of publishing publication on defined channel. Can be 'null' or ISO8601 date-time format (yyyy-MM-dd'T'HH:mm:ss.SSSZZ).",
                        "type": ["string", "null"],
                        "format": "date-time"
                    }
                }
            }
        }
    },
    "required": ["type", "jobOpeningId", "position", "languageId"]
}
```

### GET /jobPublications/?externalId={externalId}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "type": {
            "description": "Defines the type of the job publication (default value = 'DEFAULT'). Job publications with type 'EXTERNAL' are only displayed in the job list and opened in new browser tab.",
            "enum": ["DEFAULT", "EXTERNAL"]
        },
        "jobOpeningId": {
            "type": "integer"
        },
        "position": {
            "description": "Name or position of the job publication",
            "type": "string"
        },
        "languageId": {
            "description": "IsoA2 code of the requested language. Eg. 'de', 'en'.",
            "type": "string"
        },
        "subtitle": {
            "type": ["string", "null"]
        },
        "introduction": {
            "description": "Publication introduction as HTML text.",
            "type": ["string", "null"]
        },
        "tasks": {
            "description": "Publication tasks as HTML text.",
            "type": ["string", "null"]
        },
        "profile": {
            "description": "Publication profile as HTML text.",
            "type": ["string", "null"]
        },
        "weOffer": {
            "description": "Publication we-offer as HTML text.",
            "type": ["string", "null"]
        },
        "closingText": {
            "description": "Publication closing text as HTML text.",
            "type": ["string", "null"]
        },
        "pageTitle": {
            "type": ["string", "null"]
        },
        "pageDescription": {
            "type": ["string", "null"]
        },
        "externalPublicationUrl": {
            "description": "Link to an external publication. Can only be set for type='EXTERNAL'",
            "type": ["string", "null"]
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "status": {
            "description": "Defines the status of the job publication (default value = 'ACTIVE'). Status cannot be changed to IN_APPROVAL by REST API",
            "enum": ["ACTIVE", "DRAFT", "IN_APPROVAL"]
        },
        "placements": {
            "description": "List of placements that the job publication should be published on.",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "channelId": {
                        "description": "Id of channel that should be published on. 'channelId' or 'internalName' are required.",
                        "type": "integer"
                    },
                    "internalName": {
                        "description": "Internal name of channel that should be published on. 'channelId' or 'internalName' are required.",
                        "type": ["string", "null"]
                    },
                    "startDate": {
                        "description": "Start date of publishing publication on defined channel. Can be 'null' or ISO8601 date-time format (yyyy-MM-dd'T'HH:mm:ss.SSSZZ).",
                        "type": ["string", "null"],
                        "format": "date-time"
                    },
                    "endDate": {
                        "description": "End date of publishing publication on defined channel. Can be 'null' or ISO8601 date-time format (yyyy-MM-dd'T'HH:mm:ss.SSSZZ).",
                        "type": ["string", "null"],
                        "format": "date-time"
                    }
                }
            }
        }
    },
    "required": ["type", "jobOpeningId", "position", "languageId"]
}
```

### GET /jobPublications/{id}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "type": {
            "description": "Defines the type of the job publication (default value = 'DEFAULT'). Job publications with type 'EXTERNAL' are only displayed in the job list and opened in new browser tab.",
            "enum": ["DEFAULT", "EXTERNAL"]
        },
        "jobOpeningId": {
            "type": "integer"
        },
        "position": {
            "description": "Name or position of the job publication",
            "type": "string"
        },
        "languageId": {
            "description": "IsoA2 code of the requested language. Eg. 'de', 'en'.",
            "type": "string"
        },
        "subtitle": {
            "type": ["string", "null"]
        },
        "introduction": {
            "description": "Publication introduction as HTML text.",
            "type": ["string", "null"]
        },
        "tasks": {
            "description": "Publication tasks as HTML text.",
            "type": ["string", "null"]
        },
        "profile": {
            "description": "Publication profile as HTML text.",
            "type": ["string", "null"]
        },
        "weOffer": {
            "description": "Publication we-offer as HTML text.",
            "type": ["string", "null"]
        },
        "closingText": {
            "description": "Publication closing text as HTML text.",
            "type": ["string", "null"]
        },
        "pageTitle": {
            "type": ["string", "null"]
        },
        "pageDescription": {
            "type": ["string", "null"]
        },
        "externalPublicationUrl": {
            "description": "Link to an external publication. Can only be set for type='EXTERNAL'",
            "type": ["string", "null"]
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "status": {
            "description": "Defines the status of the job publication (default value = 'ACTIVE'). Status cannot be changed to IN_APPROVAL by REST API",
            "enum": ["ACTIVE", "DRAFT", "IN_APPROVAL"]
        },
        "placements": {
            "description": "List of placements that the job publication should be published on.",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "channelId": {
                        "description": "Id of channel that should be published on. 'channelId' or 'internalName' are required.",
                        "type": "integer"
                    },
                    "internalName": {
                        "description": "Internal name of channel that should be published on. 'channelId' or 'internalName' are required.",
                        "type": ["string", "null"]
                    },
                    "startDate": {
                        "description": "Start date of publishing publication on defined channel. Can be 'null' or ISO8601 date-time format (yyyy-MM-dd'T'HH:mm:ss.SSSZZ).",
                        "type": ["string", "null"],
                        "format": "date-time"
                    },
                    "endDate": {
                        "description": "End date of publishing publication on defined channel. Can be 'null' or ISO8601 date-time format (yyyy-MM-dd'T'HH:mm:ss.SSSZZ).",
                        "type": ["string", "null"],
                        "format": "date-time"
                    }
                }
            }
        }
    },
    "required": ["type", "jobOpeningId", "position", "languageId"]
}
```

### PUT /jobPublications/{id}

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "type": {
            "description": "Defines the type of the job publication (default value = 'DEFAULT'). Job publications with type 'EXTERNAL' are only displayed in the job list and opened in new browser tab.",
            "enum": ["DEFAULT", "EXTERNAL"]
        },
        "jobOpeningId": {
            "type": "integer"
        },
        "position": {
            "description": "Name or position of the job publication",
            "type": "string"
        },
        "languageId": {
            "description": "IsoA2 code of the requested language. Eg. 'de', 'en'.",
            "type": "string"
        },
        "subtitle": {
            "description": "Subtitle has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' subtitle can't be null.",
            "type": ["string", "null"]
        },
        "introduction": {
            "description": "Publication introduction as HTML text. It has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' introduction can't be null.",
            "type": ["string", "null"]
        },
        "tasks": {
            "description": "Publication tasks as HTML text. It has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' tasks can't be null.",
            "type": ["string", "null"]
        },
        "profile": {
            "description": "Publication profile as HTML text. It has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' profile can't be null.",
            "type": ["string", "null"]
        },
        "weOffer": {
            "description": "Publication weOffer as HTML text. It has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' weOffer can't be null.",
            "type": ["string", "null"]
        },
        "closingText": {
            "description": "Publication closingText as HTML text. It has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' closingText can't be null.",
            "type": ["string", "null"]
        },
        "pageTitle": {
            "type": ["string", "null"]
        },
        "pageDescription": {
            "description": "PageDescription has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' pageDescription can't be null.",
            "type": ["string", "null"]
        },
        "externalPublicationUrl": {
            "description": "Link to an external publication. Can only be set for type='EXTERNAL'. It has one of following field types: 'MANDATORY', 'OPTIONAL' or 'HIDDEN'. If field type is set to 'MANDATORY' externalPublicationUrl can't be null.",
            "type": ["string", "null"]
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "status": {
            "description": "Defines the status of the job publication (default value = 'ACTIVE').",
            "enum": ["ACTIVE", "DRAFT"]
        },
        "placements": {
            "description": "List of placements that the job publication should be published on.",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "channelId": {
                        "description": "Id of channel that should be published on. 'channelId' or 'internalName' are required.",
                        "type": "integer"
                    },
                    "internalName": {
                        "description": "Internal name of channel that should be published on. 'channelId' or 'internalName' are required.",
                        "type": ["string", "null"]
                    },
                    "startDate": {
                        "description": "Start date of publishing publication on defined channel. Can be 'null' or ISO8601 date-time format (yyyy-MM-dd'T'HH:mm:ss.SSSZZ).",
                        "type": ["string", "null"],
                        "format": "date-time"
                    },
                    "endDate": {
                        "description": "End date of publishing publication on defined channel. Can be 'null' or ISO8601 date-time format (yyyy-MM-dd'T'HH:mm:ss.SSSZZ).",
                        "type": ["string", "null"],
                        "format": "date-time"
                    }
                }
            }
        }
    },
    "required": [
        "version",
        "type",
        "jobOpeningId",
        "position",
        "languageId",
        "status"
    ]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "type": {
            "description": "Defines the type of the job publication (default value = 'DEFAULT'). Job publications with type 'EXTERNAL' are only displayed in the job list and opened in new browser tab.",
            "enum": ["DEFAULT", "EXTERNAL"]
        },
        "jobOpeningId": {
            "type": "integer"
        },
        "position": {
            "description": "Name or position of the job publication",
            "type": "string"
        },
        "languageId": {
            "description": "IsoA2 code of the requested language. Eg. 'de', 'en'.",
            "type": "string"
        },
        "subtitle": {
            "type": ["string", "null"]
        },
        "introduction": {
            "description": "Publication introduction as HTML text.",
            "type": ["string", "null"]
        },
        "tasks": {
            "description": "Publication tasks as HTML text.",
            "type": ["string", "null"]
        },
        "profile": {
            "description": "Publication profile as HTML text.",
            "type": ["string", "null"]
        },
        "weOffer": {
            "description": "Publication we-offer as HTML text.",
            "type": ["string", "null"]
        },
        "closingText": {
            "description": "Publication closing text as HTML text.",
            "type": ["string", "null"]
        },
        "pageTitle": {
            "type": ["string", "null"]
        },
        "pageDescription": {
            "type": ["string", "null"]
        },
        "externalPublicationUrl": {
            "description": "Link to an external publication. Can only be set for type='EXTERNAL'",
            "type": ["string", "null"]
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "status": {
            "description": "Defines the status of the job publication (default value = 'ACTIVE'). Status cannot be changed to IN_APPROVAL by REST API",
            "enum": ["ACTIVE", "DRAFT", "IN_APPROVAL"]
        },
        "placements": {
            "description": "List of placements that the job publication should be published on.",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "channelId": {
                        "description": "Id of channel that should be published on. 'channelId' or 'internalName' are required.",
                        "type": "integer"
                    },
                    "internalName": {
                        "description": "Internal name of channel that should be published on. 'channelId' or 'internalName' are required.",
                        "type": ["string", "null"]
                    },
                    "startDate": {
                        "description": "Start date of publishing publication on defined channel. Can be 'null' or ISO8601 date-time format (yyyy-MM-dd'T'HH:mm:ss.SSSZZ).",
                        "type": ["string", "null"],
                        "format": "date-time"
                    },
                    "endDate": {
                        "description": "End date of publishing publication on defined channel. Can be 'null' or ISO8601 date-time format (yyyy-MM-dd'T'HH:mm:ss.SSSZZ).",
                        "type": ["string", "null"],
                        "format": "date-time"
                    }
                }
            }
        }
    },
    "required": ["type", "jobOpeningId", "position", "languageId"]
}
```

### POST /jobPublications/{id}/delete

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        }
    },
    "required": ["success"]
}
```

## Job publication placements

### GET /jobPublicationPlacements/{partner_id}/placements

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "name": {
            "description": "The display name for the external placement",
            "type": "string"
        },
        "description": {
            "description": "additional information that is displayed",
            "type": ["string", "null"]
        },
        "status": {
            "description": "Status of external placement",
            "enum": ["ACTIVE", "INACTIVE", "IN_PROGRESS"]
        },
        "externalReference": {
            "description": "Reference for external purposes",
            "type": "string"
        },
        "jobPublicationId": {
            "description": "Reference for belonging job publication",
            "type": "integer"
        },
        "startDate": {
            "description": "Start date of external placement",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "endDate": {
            "description": "End date of external placement",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "externalLinks": {
            "type": "array",
            "description": "These links are rendered as buttons to the external placement view, e.g. deep back-links to your system.",
            "properties": {
                "label": {
                    "type": "string"
                },
                "url": {
                    "description": "Url of the external system. Has to start with 'http(s)://'",
                    "type": "string"
                },
                "faIcon": {
                    "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'. When none given, 'fa-external-link' will be used as icon",
                    "type": "string"
                }
            },
            "required": ["label", "url"]
        }
    },
    "required": ["name", "status", "externalReference", "jobPublicationId"]
}
```

### POST /jobPublicationPlacements/{partner_id}/placements

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "name": {
            "description": "The display name for the external placement",
            "type": "string"
        },
        "description": {
            "description": "additional information that is displayed",
            "type": ["string", "null"]
        },
        "status": {
            "description": "Status of external placement",
            "enum": ["ACTIVE", "INACTIVE", "IN_PROGRESS"]
        },
        "externalReference": {
            "description": "Reference for external purposes",
            "type": "string"
        },
        "jobPublicationId": {
            "description": "Reference for belonging job publication",
            "type": "integer"
        },
        "startDate": {
            "description": "Start date of external placement",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "endDate": {
            "description": "End date of external placement",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "externalLinks": {
            "type": "array",
            "description": "These links are rendered as buttons to the external placement view, e.g. deep back-links to your system.",
            "properties": {
                "label": {
                    "type": "string"
                },
                "url": {
                    "description": "Url of the external system. Has to start with 'http(s)://'",
                    "type": "string"
                },
                "faIcon": {
                    "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'. When none given, 'fa-external-link' will be used as icon",
                    "type": "string"
                }
            },
            "required": ["label", "url"]
        }
    },
    "required": ["name", "status", "externalReference", "jobPublicationId"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "name": {
            "description": "The display name for the external placement",
            "type": "string"
        },
        "description": {
            "description": "additional information that is displayed",
            "type": ["string", "null"]
        },
        "status": {
            "description": "Status of external placement",
            "enum": ["ACTIVE", "INACTIVE", "IN_PROGRESS"]
        },
        "externalReference": {
            "description": "Reference for external purposes",
            "type": "string"
        },
        "jobPublicationId": {
            "description": "Reference for belonging job publication",
            "type": "integer"
        },
        "startDate": {
            "description": "Start date of external placement",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "endDate": {
            "description": "End date of external placement",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "externalLinks": {
            "type": "array",
            "description": "These links are rendered as buttons to the external placement view, e.g. deep back-links to your system.",
            "properties": {
                "label": {
                    "type": "string"
                },
                "url": {
                    "description": "Url of the external system. Has to start with 'http(s)://'",
                    "type": "string"
                },
                "faIcon": {
                    "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'. When none given, 'fa-external-link' will be used as icon",
                    "type": "string"
                }
            },
            "required": ["label", "url"]
        }
    },
    "required": ["name", "status", "externalReference", "jobPublicationId"]
}
```

### GET /jobPublicationPlacements/{partner_id}/placements/?externalId={externalId}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "name": {
            "description": "The display name for the external placement",
            "type": "string"
        },
        "description": {
            "description": "additional information that is displayed",
            "type": ["string", "null"]
        },
        "status": {
            "description": "Status of external placement",
            "enum": ["ACTIVE", "INACTIVE", "IN_PROGRESS"]
        },
        "externalReference": {
            "description": "Reference for external purposes",
            "type": "string"
        },
        "jobPublicationId": {
            "description": "Reference for belonging job publication",
            "type": "integer"
        },
        "startDate": {
            "description": "Start date of external placement",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "endDate": {
            "description": "End date of external placement",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "externalLinks": {
            "type": "array",
            "description": "These links are rendered as buttons to the external placement view, e.g. deep back-links to your system.",
            "properties": {
                "label": {
                    "type": "string"
                },
                "url": {
                    "description": "Url of the external system. Has to start with 'http(s)://'",
                    "type": "string"
                },
                "faIcon": {
                    "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'. When none given, 'fa-external-link' will be used as icon",
                    "type": "string"
                }
            },
            "required": ["label", "url"]
        }
    },
    "required": ["name", "status", "externalReference", "jobPublicationId"]
}
```

### GET /jobPublicationPlacements/{partner_id}/placements/?jobPublicationId={jobPublicationId}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "name": {
            "description": "The display name for the external placement",
            "type": "string"
        },
        "description": {
            "description": "additional information that is displayed",
            "type": ["string", "null"]
        },
        "status": {
            "description": "Status of external placement",
            "enum": ["ACTIVE", "INACTIVE", "IN_PROGRESS"]
        },
        "externalReference": {
            "description": "Reference for external purposes",
            "type": "string"
        },
        "jobPublicationId": {
            "description": "Reference for belonging job publication",
            "type": "integer"
        },
        "startDate": {
            "description": "Start date of external placement",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "endDate": {
            "description": "End date of external placement",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "externalLinks": {
            "type": "array",
            "description": "These links are rendered as buttons to the external placement view, e.g. deep back-links to your system.",
            "properties": {
                "label": {
                    "type": "string"
                },
                "url": {
                    "description": "Url of the external system. Has to start with 'http(s)://'",
                    "type": "string"
                },
                "faIcon": {
                    "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'. When none given, 'fa-external-link' will be used as icon",
                    "type": "string"
                }
            },
            "required": ["label", "url"]
        }
    },
    "required": ["name", "status", "externalReference", "jobPublicationId"]
}
```

### GET /jobPublicationPlacements/{partner_id}/placements/{id}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "name": {
            "description": "The display name for the external placement",
            "type": "string"
        },
        "description": {
            "description": "additional information that is displayed",
            "type": ["string", "null"]
        },
        "status": {
            "description": "Status of external placement",
            "enum": ["ACTIVE", "INACTIVE", "IN_PROGRESS"]
        },
        "externalReference": {
            "description": "Reference for external purposes",
            "type": "string"
        },
        "jobPublicationId": {
            "description": "Reference for belonging job publication",
            "type": "integer"
        },
        "startDate": {
            "description": "Start date of external placement",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "endDate": {
            "description": "End date of external placement",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "externalLinks": {
            "type": "array",
            "description": "These links are rendered as buttons to the external placement view, e.g. deep back-links to your system.",
            "properties": {
                "label": {
                    "type": "string"
                },
                "url": {
                    "description": "Url of the external system. Has to start with 'http(s)://'",
                    "type": "string"
                },
                "faIcon": {
                    "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'. When none given, 'fa-external-link' will be used as icon",
                    "type": "string"
                }
            },
            "required": ["label", "url"]
        }
    },
    "required": ["name", "status", "externalReference", "jobPublicationId"]
}
```

### PUT /jobPublicationPlacements/{partner_id}/placements/{id}

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "name": {
            "description": "The display name for the external placement",
            "type": "string"
        },
        "description": {
            "description": "additional information that is displayed",
            "type": ["string", "null"]
        },
        "status": {
            "description": "Status of external placement",
            "enum": ["ACTIVE", "INACTIVE", "IN_PROGRESS"]
        },
        "externalReference": {
            "description": "Reference for external purposes",
            "type": "string"
        },
        "jobPublicationId": {
            "description": "Reference for belonging job publication",
            "type": "integer"
        },
        "startDate": {
            "description": "Start date of external placement",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "endDate": {
            "description": "End date of external placement",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "externalLinks": {
            "type": "array",
            "description": "These links are rendered as buttons to the external placement view, e.g. deep back-links to your system.",
            "properties": {
                "label": {
                    "type": "string"
                },
                "url": {
                    "description": "Url of the external system. Has to start with 'http(s)://'",
                    "type": "string"
                },
                "faIcon": {
                    "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'. When none given, 'fa-external-link' will be used as icon",
                    "type": "string"
                }
            },
            "required": ["label", "url"]
        }
    },
    "required": [
        "version",
        "name",
        "status",
        "externalReference",
        "jobPublicationId"
    ]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "name": {
            "description": "The display name for the external placement",
            "type": "string"
        },
        "description": {
            "description": "additional information that is displayed",
            "type": ["string", "null"]
        },
        "status": {
            "description": "Status of external placement",
            "enum": ["ACTIVE", "INACTIVE", "IN_PROGRESS"]
        },
        "externalReference": {
            "description": "Reference for external purposes",
            "type": "string"
        },
        "jobPublicationId": {
            "description": "Reference for belonging job publication",
            "type": "integer"
        },
        "startDate": {
            "description": "Start date of external placement",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "endDate": {
            "description": "End date of external placement",
            "type": ["string", "null"],
            "format": "date-time"
        },
        "externalLinks": {
            "type": "array",
            "description": "These links are rendered as buttons to the external placement view, e.g. deep back-links to your system.",
            "properties": {
                "label": {
                    "type": "string"
                },
                "url": {
                    "description": "Url of the external system. Has to start with 'http(s)://'",
                    "type": "string"
                },
                "faIcon": {
                    "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'. When none given, 'fa-external-link' will be used as icon",
                    "type": "string"
                }
            },
            "required": ["label", "url"]
        }
    },
    "required": [
        "version",
        "name",
        "status",
        "externalReference",
        "jobPublicationId"
    ]
}
```

### POST /jobPublicationPlacements/{partner_id}/placements/{id}/delete

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        }
    },
    "required": ["success"]
}
```

## Job publication channels

### GET /jobPublicationChannels/{id}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Internal name",
            "type": "string"
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "externalLinks": {
            "type": "array",
            "description": "These links are rendered as buttons to the job publication channel.",
            "properties": {
                "label": {
                    "type": "string"
                },
                "url": {
                    "description": "Url of the external system. Has to start with 'http(s)://'",
                    "type": "string"
                },
                "faIcon": {
                    "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'. When none given, 'fa-external-link' will be used as icon",
                    "type": "string"
                }
            },
            "required": ["label", "url"]
        }
    },
    "required": ["id", "version"]
}
```

### PUT /jobPublicationChannels/{id}

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "externalLinks": {
            "type": "array",
            "description": "These links are rendered as buttons to the job publication channel.",
            "properties": {
                "label": {
                    "type": "string"
                },
                "url": {
                    "description": "Url of the external system. Has to start with 'http(s)://'",
                    "type": "string"
                },
                "faIcon": {
                    "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'. When none given, 'fa-external-link' will be used as icon",
                    "type": "string"
                }
            },
            "required": ["label", "url"]
        }
    },
    "required": ["version"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Internal name",
            "type": "string"
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "externalLinks": {
            "type": "array",
            "description": "These links are rendered as buttons to the job publication channel.",
            "properties": {
                "label": {
                    "type": "string"
                },
                "url": {
                    "description": "Url of the external system. Has to start with 'http(s)://'",
                    "type": "string"
                },
                "faIcon": {
                    "description": "A Font Awesome icon of version 5.x that is displayed in regular (with class 'far'). Has to start with 'fa-'. When none given, 'fa-external-link' will be used as icon",
                    "type": "string"
                }
            },
            "required": ["label", "url"]
        }
    },
    "required": ["id", "version"]
}
```

## Locations

### GET /locations/

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {
                "type": "string",
                "description": "Specify an unique id for further usage with format: [A-Z0-9_]+"
            },
            "version": {
                "type": "integer"
            },
            "name": {
                "type": "string"
            },
            "externalName": {
                "type": "string"
            },
            "orgUnitId": {
                "type": "integer"
            },
            "isJobLocation": {
                "type": ["boolean", "null"]
            },
            "isDesiredLocation": {
                "type": ["boolean", "null"]
            },
            "isAppointmentLocation": {
                "type": ["boolean", "null"]
            },
            "country": {
                "type": "string"
            },
            "countryIsoA2": {
                "type": ["string", "null"],
                "description": "Country name with format: ISO ALPHA-2 Code"
            },
            "address1": {
                "type": ["string", "null"]
            },
            "address2": {
                "type": ["string", "null"]
            },
            "address3": {
                "type": ["string", "null"]
            },
            "address4": {
                "type": ["string", "null"]
            },
            "address5": {
                "type": ["string", "null"]
            },
            "usState": {
                "description": "Address-Field: Can only be set if countryIsoA2 is set to 'US'",
                "enum": [
                    null,
                    "AL",
                    "AK",
                    "AZ",
                    "AR",
                    "CA",
                    "CO",
                    "CT",
                    "DE",
                    "DC",
                    "FL",
                    "GA",
                    "HI",
                    "ID",
                    "IL",
                    "IN",
                    "IA",
                    "KS",
                    "KY",
                    "LA",
                    "ME",
                    "MD",
                    "MA",
                    "MI",
                    "MN",
                    "MS",
                    "MO",
                    "MT",
                    "NE",
                    "NV",
                    "NH",
                    "NJ",
                    "NM",
                    "NY",
                    "NC",
                    "ND",
                    "OH",
                    "OK",
                    "OR",
                    "PA",
                    "RI",
                    "SC",
                    "SD",
                    "TN",
                    "TX",
                    "UT",
                    "VT",
                    "VA",
                    "WA",
                    "WV",
                    "WI",
                    "WY"
                ]
            },
            "zipCode": {
                "type": ["string", "null"]
            },
            "city": {
                "type": ["string", "null"]
            },
            "latitude": {
                "type": ["number", "null"]
            },
            "longitude": {
                "type": ["number", "null"]
            },
            "additionalInformation": {
                "type": ["string", "null"]
            },
            "nameMessages": {
                "type": "object",
                "properties": {
                    "de": {
                        "type": "string"
                    },
                    "en": {
                        "type": "string"
                    }
                },
                "description": "The location name translated in the available languages"
            },
            "externalNameMessages": {
                "type": "object",
                "properties": {
                    "de": {
                        "type": "string"
                    },
                    "en": {
                        "type": "string"
                    }
                },
                "description": "The location external name for use outside of the d.vinci system, e. g. in job openings or correspondence templates, translated in the available languages"
            }
        },
        "required": [
            "id",
            "version",
            "name",
            "orgUnitId",
            "country",
            "countryIsoA2",
            "latitude",
            "longitude",
            "additionalInformation",
            "nameMessages"
        ]
    }
}
```

### POST /locations/

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "string",
            "description": "Specify an unique id for further usage with format: [A-Z0-9_]+"
        },
        "orgUnitId": {
            "type": "integer"
        },
        "isJobLocation": {
            "type": ["boolean", "null"]
        },
        "isDesiredLocation": {
            "type": ["boolean", "null"]
        },
        "isAppointmentLocation": {
            "type": ["boolean", "null"]
        },
        "address1": {
            "type": ["string", "null"]
        },
        "address2": {
            "type": ["string", "null"]
        },
        "address3": {
            "type": ["string", "null"]
        },
        "address4": {
            "type": ["string", "null"]
        },
        "address5": {
            "type": ["string", "null"]
        },
        "usState": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set to 'US'",
            "enum": [
                null,
                "AL",
                "AK",
                "AZ",
                "AR",
                "CA",
                "CO",
                "CT",
                "DE",
                "DC",
                "FL",
                "GA",
                "HI",
                "ID",
                "IL",
                "IN",
                "IA",
                "KS",
                "KY",
                "LA",
                "ME",
                "MD",
                "MA",
                "MI",
                "MN",
                "MS",
                "MO",
                "MT",
                "NE",
                "NV",
                "NH",
                "NJ",
                "NM",
                "NY",
                "NC",
                "ND",
                "OH",
                "OK",
                "OR",
                "PA",
                "RI",
                "SC",
                "SD",
                "TN",
                "TX",
                "UT",
                "VT",
                "VA",
                "WA",
                "WV",
                "WI",
                "WY"
            ]
        },
        "zipCode": {
            "type": ["string", "null"]
        },
        "city": {
            "type": ["string", "null"]
        },
        "latitude": {
            "type": ["number", "null"]
        },
        "longitude": {
            "type": ["number", "null"]
        },
        "additionalInformation": {
            "type": ["string", "null"]
        },
        "countryIsoA2": {
            "type": ["string", "null"],
            "description": "Country name with format: ISO ALPHA-2 Code"
        },
        "nameMessages": {
            "type": "object",
            "properties": {
                "de": {
                    "type": "string"
                },
                "en": {
                    "type": "string"
                }
            },
            "description": "The location name translated in the available languages"
        },
        "externalNameMessages": {
            "type": "object",
            "properties": {
                "de": {
                    "type": "string"
                },
                "en": {
                    "type": "string"
                }
            },
            "description": "The location external name for use outside of the d.vinci system, e. g. in job openings or correspondence templates, translated in the available languages"
        }
    },
    "required": ["id", "orgUnitId", "nameMessages"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "string",
            "description": "Specify an unique id for further usage with format: [A-Z0-9_]+"
        },
        "version": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "externalName": {
            "type": "string"
        },
        "orgUnitId": {
            "type": "integer"
        },
        "isJobLocation": {
            "type": ["boolean", "null"]
        },
        "isDesiredLocation": {
            "type": ["boolean", "null"]
        },
        "isAppointmentLocation": {
            "type": ["boolean", "null"]
        },
        "country": {
            "type": "string"
        },
        "countryIsoA2": {
            "type": ["string", "null"],
            "description": "Country name with format: ISO ALPHA-2 Code"
        },
        "address1": {
            "type": ["string", "null"]
        },
        "address2": {
            "type": ["string", "null"]
        },
        "address3": {
            "type": ["string", "null"]
        },
        "address4": {
            "type": ["string", "null"]
        },
        "address5": {
            "type": ["string", "null"]
        },
        "usState": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set to 'US'",
            "enum": [
                null,
                "AL",
                "AK",
                "AZ",
                "AR",
                "CA",
                "CO",
                "CT",
                "DE",
                "DC",
                "FL",
                "GA",
                "HI",
                "ID",
                "IL",
                "IN",
                "IA",
                "KS",
                "KY",
                "LA",
                "ME",
                "MD",
                "MA",
                "MI",
                "MN",
                "MS",
                "MO",
                "MT",
                "NE",
                "NV",
                "NH",
                "NJ",
                "NM",
                "NY",
                "NC",
                "ND",
                "OH",
                "OK",
                "OR",
                "PA",
                "RI",
                "SC",
                "SD",
                "TN",
                "TX",
                "UT",
                "VT",
                "VA",
                "WA",
                "WV",
                "WI",
                "WY"
            ]
        },
        "zipCode": {
            "type": ["string", "null"]
        },
        "city": {
            "type": ["string", "null"]
        },
        "latitude": {
            "type": ["number", "null"]
        },
        "longitude": {
            "type": ["number", "null"]
        },
        "additionalInformation": {
            "type": ["string", "null"]
        },
        "nameMessages": {
            "type": "object",
            "properties": {
                "de": {
                    "type": "string"
                },
                "en": {
                    "type": "string"
                }
            },
            "description": "The location name translated in the available languages"
        },
        "externalNameMessages": {
            "type": "object",
            "properties": {
                "de": {
                    "type": "string"
                },
                "en": {
                    "type": "string"
                }
            },
            "description": "The location external name for use outside of the d.vinci system, e. g. in job openings or correspondence templates, translated in the available languages"
        }
    },
    "required": [
        "id",
        "version",
        "name",
        "orgUnitId",
        "country",
        "countryIsoA2",
        "latitude",
        "longitude",
        "additionalInformation",
        "nameMessages"
    ]
}
```

### GET /locations/{id}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "string",
            "description": "Specify an unique id for further usage with format: [A-Z0-9_]+"
        },
        "version": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "externalName": {
            "type": "string"
        },
        "orgUnitId": {
            "type": "integer"
        },
        "isJobLocation": {
            "type": ["boolean", "null"]
        },
        "isDesiredLocation": {
            "type": ["boolean", "null"]
        },
        "isAppointmentLocation": {
            "type": ["boolean", "null"]
        },
        "country": {
            "type": "string"
        },
        "countryIsoA2": {
            "type": ["string", "null"],
            "description": "Country name with format: ISO ALPHA-2 Code"
        },
        "address1": {
            "type": ["string", "null"]
        },
        "address2": {
            "type": ["string", "null"]
        },
        "address3": {
            "type": ["string", "null"]
        },
        "address4": {
            "type": ["string", "null"]
        },
        "address5": {
            "type": ["string", "null"]
        },
        "usState": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set to 'US'",
            "enum": [
                null,
                "AL",
                "AK",
                "AZ",
                "AR",
                "CA",
                "CO",
                "CT",
                "DE",
                "DC",
                "FL",
                "GA",
                "HI",
                "ID",
                "IL",
                "IN",
                "IA",
                "KS",
                "KY",
                "LA",
                "ME",
                "MD",
                "MA",
                "MI",
                "MN",
                "MS",
                "MO",
                "MT",
                "NE",
                "NV",
                "NH",
                "NJ",
                "NM",
                "NY",
                "NC",
                "ND",
                "OH",
                "OK",
                "OR",
                "PA",
                "RI",
                "SC",
                "SD",
                "TN",
                "TX",
                "UT",
                "VT",
                "VA",
                "WA",
                "WV",
                "WI",
                "WY"
            ]
        },
        "zipCode": {
            "type": ["string", "null"]
        },
        "city": {
            "type": ["string", "null"]
        },
        "latitude": {
            "type": ["number", "null"]
        },
        "longitude": {
            "type": ["number", "null"]
        },
        "additionalInformation": {
            "type": ["string", "null"]
        },
        "nameMessages": {
            "type": "object",
            "properties": {
                "de": {
                    "type": "string"
                },
                "en": {
                    "type": "string"
                }
            },
            "description": "The location name translated in the available languages"
        },
        "externalNameMessages": {
            "type": "object",
            "properties": {
                "de": {
                    "type": "string"
                },
                "en": {
                    "type": "string"
                }
            },
            "description": "The location external name for use outside of the d.vinci system, e. g. in job openings or correspondence templates, translated in the available languages"
        }
    },
    "required": [
        "id",
        "version",
        "name",
        "orgUnitId",
        "country",
        "countryIsoA2",
        "latitude",
        "longitude",
        "additionalInformation",
        "nameMessages"
    ]
}
```

### PUT /locations/{id}

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "orgUnitId": {
            "type": "integer"
        },
        "isJobLocation": {
            "type": ["boolean", "null"]
        },
        "isDesiredLocation": {
            "type": ["boolean", "null"]
        },
        "isAppointmentLocation": {
            "type": ["boolean", "null"]
        },
        "address1": {
            "type": ["string", "null"]
        },
        "address2": {
            "type": ["string", "null"]
        },
        "address3": {
            "type": ["string", "null"]
        },
        "address4": {
            "type": ["string", "null"]
        },
        "address5": {
            "type": ["string", "null"]
        },
        "usState": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set to 'US'",
            "enum": [
                null,
                "AL",
                "AK",
                "AZ",
                "AR",
                "CA",
                "CO",
                "CT",
                "DE",
                "DC",
                "FL",
                "GA",
                "HI",
                "ID",
                "IL",
                "IN",
                "IA",
                "KS",
                "KY",
                "LA",
                "ME",
                "MD",
                "MA",
                "MI",
                "MN",
                "MS",
                "MO",
                "MT",
                "NE",
                "NV",
                "NH",
                "NJ",
                "NM",
                "NY",
                "NC",
                "ND",
                "OH",
                "OK",
                "OR",
                "PA",
                "RI",
                "SC",
                "SD",
                "TN",
                "TX",
                "UT",
                "VT",
                "VA",
                "WA",
                "WV",
                "WI",
                "WY"
            ]
        },
        "zipCode": {
            "type": ["string", "null"]
        },
        "city": {
            "type": ["string", "null"]
        },
        "latitude": {
            "type": ["number", "null"]
        },
        "longitude": {
            "type": ["number", "null"]
        },
        "additionalInformation": {
            "type": ["string", "null"]
        },
        "countryIsoA2": {
            "type": ["string", "null"],
            "description": "Country name with format: ISO ALPHA-2 Code"
        },
        "nameMessages": {
            "type": "object",
            "properties": {
                "de": {
                    "type": "string"
                },
                "en": {
                    "type": "string"
                }
            },
            "description": "The location name translated in the available languages"
        },
        "externalNameMessages": {
            "type": "object",
            "properties": {
                "de": {
                    "type": "string"
                },
                "en": {
                    "type": "string"
                }
            },
            "description": "The location external name for use outside of the d.vinci system, e. g. in job openings or correspondence templates, translated in the available languages"
        }
    },
    "required": ["version", "nameMessages"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "string",
            "description": "Specify an unique id for further usage with format: [A-Z0-9_]+"
        },
        "version": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "externalName": {
            "type": "string"
        },
        "orgUnitId": {
            "type": "integer"
        },
        "isJobLocation": {
            "type": ["boolean", "null"]
        },
        "isDesiredLocation": {
            "type": ["boolean", "null"]
        },
        "isAppointmentLocation": {
            "type": ["boolean", "null"]
        },
        "country": {
            "type": "string"
        },
        "countryIsoA2": {
            "type": ["string", "null"],
            "description": "Country name with format: ISO ALPHA-2 Code"
        },
        "address1": {
            "type": ["string", "null"]
        },
        "address2": {
            "type": ["string", "null"]
        },
        "address3": {
            "type": ["string", "null"]
        },
        "address4": {
            "type": ["string", "null"]
        },
        "address5": {
            "type": ["string", "null"]
        },
        "usState": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set to 'US'",
            "enum": [
                null,
                "AL",
                "AK",
                "AZ",
                "AR",
                "CA",
                "CO",
                "CT",
                "DE",
                "DC",
                "FL",
                "GA",
                "HI",
                "ID",
                "IL",
                "IN",
                "IA",
                "KS",
                "KY",
                "LA",
                "ME",
                "MD",
                "MA",
                "MI",
                "MN",
                "MS",
                "MO",
                "MT",
                "NE",
                "NV",
                "NH",
                "NJ",
                "NM",
                "NY",
                "NC",
                "ND",
                "OH",
                "OK",
                "OR",
                "PA",
                "RI",
                "SC",
                "SD",
                "TN",
                "TX",
                "UT",
                "VT",
                "VA",
                "WA",
                "WV",
                "WI",
                "WY"
            ]
        },
        "zipCode": {
            "type": ["string", "null"]
        },
        "city": {
            "type": ["string", "null"]
        },
        "latitude": {
            "type": ["number", "null"]
        },
        "longitude": {
            "type": ["number", "null"]
        },
        "additionalInformation": {
            "type": ["string", "null"]
        },
        "nameMessages": {
            "type": "object",
            "properties": {
                "de": {
                    "type": "string"
                },
                "en": {
                    "type": "string"
                }
            },
            "description": "The location name translated in the available languages"
        },
        "externalNameMessages": {
            "type": "object",
            "properties": {
                "de": {
                    "type": "string"
                },
                "en": {
                    "type": "string"
                }
            },
            "description": "The location external name for use outside of the d.vinci system, e. g. in job openings or correspondence templates, translated in the available languages"
        }
    },
    "required": [
        "id",
        "version",
        "name",
        "orgUnitId",
        "country",
        "countryIsoA2",
        "latitude",
        "longitude",
        "additionalInformation",
        "nameMessages"
    ]
}
```

### POST /locations/{id}/delete

#### Request

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        }
    },
    "required": ["success"]
}
```

## Onboardings

### GET /onboardings/

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": [
        {
            "type": "object",
            "properties": {
                "id": {
                    "description": "ID of the onboarding",
                    "type": "integer"
                },
                "orgUnitId": {
                    "description": "ID of organization unit linked to the onboarding",
                    "type": "integer"
                },
                "status": {
                    "description": "State of onboarding",
                    "enum": ["ACTIVE", "FINISHED"]
                },
                "entryReason": {
                    "description": "Reason for onboarding",
                    "enum": [
                        "NEW_EMPLOYMENT",
                        "RETURN_AFTER_PARENTAL_LEAVE",
                        "RETURN_AFTER_LONG_TERM_SICKNESS",
                        "RETURN_AFTER_SABBATICAL",
                        "TAKEOVER_AFTER_TRAINING_STUDY",
                        "INTERNSHIP",
                        "JOB_CHANGE",
                        "COMPANY_CHANGE",
                        "JOB_LOCATION_CHANGE",
                        "BRANCH_CHANGE",
                        "TEMPORARY_EMPLOYMENT",
                        "OTHER"
                    ]
                },
                "reasonForTermination": {
                    "description": "Reason for the termination of an onboarding. This property is only set for onboardings with status 'FINISHED'",
                    "enum": [
                        "SUCCESSFULLY_FINISHED",
                        "PREMATURELY_SUCCESSFULLY_FINISHED",
                        "OFFER_NOT_ACCEPTED",
                        "RESCINDED_FROM_CONTRACT",
                        "CONTRACT_TERMINATED_BY_EMPLOYEE_DURING_PROBATION",
                        "CONTRACT_TERMINATED_BY_EMPLOYER_DURING_PROBATION",
                        "CONTRACT_TERMINATED_BY_EMPLOYEE",
                        "CONTRACT_TERMINATED_BY_EMPLOYER",
                        "EMPLOYMENT_SUSPENDED",
                        "LONG_TERM_SICKNESS",
                        "MATERNITY_PATERNITY_OR_PARENTAL_LEAVE",
                        "INTERNAL_JOB_POSITION_CHANGE",
                        "OTHER"
                    ]
                },
                "dateOfStart": {
                    "description": "ISO8601 date format (yyyy-MM-dd)",
                    "type": "string"
                },
                "dateOfContract": {
                    "description": "ISO8601 date format (yyyy-MM-dd)",
                    "type": "string"
                },
                "dateOfEmployment": {
                    "description": "ISO8601 date format (yyyy-MM-dd)",
                    "type": "string"
                },
                "dateOfEnd": {
                    "description": "ISO8601 date format (yyyy-MM-dd)",
                    "type": "string"
                },
                "dateCreated": {
                    "description": "The creation-date of the onboarding",
                    "type": "string",
                    "format": "date-time"
                },
                "personTitle": {
                    "description": "Title of the person linked to the onboarding",
                    "type": ["string", "null"]
                },
                "personSalutation": {
                    "description": "Salutation of the person linked to the onboarding",
                    "enum": ["MR", "MS", "MX"]
                },
                "personFirstName": {
                    "description": "First name of the person linked to the onboarding",
                    "type": "string"
                },
                "personLastName": {
                    "description": "Last name of the person linked to the onboarding",
                    "type": "string"
                }
            },
            "required": [
                "id",
                "orgUnitId",
                "status",
                "entryReason",
                "dateOfStart",
                "dateOfContract",
                "dateOfEmployment",
                "dateOfEnd",
                "dateCreated",
                "personSalutation",
                "personFirstName",
                "personLastName"
            ]
        }
    ]
}
```

### GET /onboardings/{id}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "ID of the onboarding",
            "type": "integer"
        },
        "orgUnitId": {
            "description": "ID of organization unit linked to the onboarding",
            "type": "integer"
        },
        "status": {
            "description": "State of onboarding",
            "enum": ["ACTIVE", "FINISHED"]
        },
        "entryReason": {
            "description": "Reason for onboarding",
            "enum": [
                "NEW_EMPLOYMENT",
                "RETURN_AFTER_PARENTAL_LEAVE",
                "RETURN_AFTER_LONG_TERM_SICKNESS",
                "RETURN_AFTER_SABBATICAL",
                "TAKEOVER_AFTER_TRAINING_STUDY",
                "INTERNSHIP",
                "JOB_CHANGE",
                "COMPANY_CHANGE",
                "JOB_LOCATION_CHANGE",
                "BRANCH_CHANGE",
                "TEMPORARY_EMPLOYMENT",
                "OTHER"
            ]
        },
        "reasonForTermination": {
            "description": "Reason for the termination of an onboarding. This property is only set for onboardings with status 'FINISHED'",
            "enum": [
                null,
                "SUCCESSFULLY_FINISHED",
                "PREMATURELY_SUCCESSFULLY_FINISHED",
                "OFFER_NOT_ACCEPTED",
                "RESCINDED_FROM_CONTRACT",
                "CONTRACT_TERMINATED_BY_EMPLOYEE_DURING_PROBATION",
                "CONTRACT_TERMINATED_BY_EMPLOYER_DURING_PROBATION",
                "CONTRACT_TERMINATED_BY_EMPLOYEE",
                "CONTRACT_TERMINATED_BY_EMPLOYER",
                "EMPLOYMENT_SUSPENDED",
                "LONG_TERM_SICKNESS",
                "MATERNITY_PATERNITY_OR_PARENTAL_LEAVE",
                "INTERNAL_JOB_POSITION_CHANGE",
                "OTHER"
            ]
        },
        "dateOfStart": {
            "description": "ISO8601 date format (yyyy-MM-dd)",
            "type": "string"
        },
        "dateOfContract": {
            "description": "ISO8601 date format (yyyy-MM-dd)",
            "type": "string"
        },
        "dateOfEmployment": {
            "description": "ISO8601 date format (yyyy-MM-dd)",
            "type": "string"
        },
        "dateOfEnd": {
            "description": "ISO8601 date format (yyyy-MM-dd)",
            "type": "string"
        },
        "dateCreated": {
            "description": "The creation-date of the onboarding",
            "type": "string",
            "format": "date-time"
        },
        "language": {
            "description": "Language of the onboarding",
            "type": "string"
        },
        "position": {
            "description": "Position of the onboarding",
            "type": "string"
        },
        "personnelNumber": {
            "description": "Personnel number of the onboarding",
            "type": ["string", "null"]
        },
        "companyId": {
            "description": "Internal name of company",
            "type": ["string", "null"]
        },
        "applicationId": {
            "description": "Id of the corresponding application paper",
            "type": ["integer", "null"]
        },
        "person": {
            "description": "Person information corresponding to the onboarding",
            "properties": {
                "title": {
                    "type": ["string", "null"]
                },
                "salutation": {
                    "enum": [null, "MR", "MS", "MX"]
                },
                "firstname": {
                    "type": ["string", "null"]
                },
                "lastName": {
                    "type": ["string", "null"]
                },
                "dateOfBirth": {
                    "description": "ISO8601 date format (yyyy-MM-dd)",
                    "type": ["string", "null"]
                },
                "email": {
                    "type": ["string", "null"]
                },
                "businessEmail": {
                    "type": ["string", "null"]
                },
                "telephone": {
                    "type": ["string", "null"]
                },
                "alternativeTelephone": {
                    "type": ["string", "null"]
                },
                "skypeName": {
                    "type": ["string", "null"]
                },
                "profileLink": {
                    "type": ["string", "null"]
                },
                "address1": {
                    "type": ["string", "null"]
                },
                "address2": {
                    "type": ["string", "null"]
                },
                "address3": {
                    "type": ["string", "null"]
                },
                "address4": {
                    "type": ["string", "null"]
                },
                "address5": {
                    "type": ["string", "null"]
                },
                "usState": {
                    "type": ["string", "null"]
                },
                "zipCode": {
                    "type": ["string", "null"]
                },
                "city": {
                    "type": ["string", "null"]
                },
                "country": {
                    "description": "ISO A2 string of the corresponding country",
                    "type": ["string", "null"]
                }
            },
            "type": "object"
        },
        "responsibilities": {
            "description": "List of responsible users for the onboarding",
            "items": {
                "properties": {
                    "id": {
                        "description": "Internal name of the responsibility",
                        "type": "string"
                    },
                    "responsibilityGroup": {
                        "description": "Corresponding group for the responsibility",
                        "enum": [
                            "SUPERVISOR",
                            "LINE_MANAGER",
                            "BUDDY",
                            "SUPPORTER"
                        ]
                    },
                    "responsibleUserId": {
                        "description": "ID of the responsible user",
                        "type": "integer"
                    }
                }
            },
            "type": "array"
        },
        "additionalInformation": {
            "description": "List of all additional information provided for the onboarding",
            "items": {
                "properties": {
                    "id": {
                        "description": "ID of the form",
                        "type": "string"
                    },
                    "fields": {
                        "items": {
                            "properties": {
                                "id": {
                                    "description": "ID of the formField",
                                    "type": "string"
                                },
                                "type": {
                                    "description": "Type of the formField",
                                    "enum": [
                                        "TEXT",
                                        "TEXTAREA",
                                        "FIVE_STAR_RATING",
                                        "YES_NO",
                                        "YES_NO_NOT_SPECIFIED",
                                        "SINGLE_CHOICE",
                                        "MULTI_CHOICE",
                                        "IBAN"
                                    ]
                                },
                                "values": {
                                    "items": {
                                        "description": "List of entered values",
                                        "type": "string"
                                    },
                                    "type": "array"
                                }
                            }
                        },
                        "type": "array"
                    }
                }
            },
            "type": "array"
        }
    },
    "required": [
        "id",
        "orgUnitId",
        "status",
        "entryReason",
        "dateOfStart",
        "dateOfContract",
        "dateOfEmployment",
        "dateOfEnd",
        "dateCreated",
        "language",
        "position",
        "person",
        "responsibilities"
    ]
}
```

### GET /onboardings/{id}/attachments

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {
                "description": "Property is not settable - only returned by the system.",
                "type": "string"
            },
            "dateCreated": {
                "description": "Technical creation date of the attachment.",
                "type": "string",
                "format": "date-time"
            },
            "filename": {
                "description": "File name of the attachment.",
                "type": "string"
            },
            "fileSize": {
                "description": "File size of the attachment in Bytes.",
                "type": "integer"
            },
            "contentType": {
                "description": "Content type of the attachment.",
                "type": "string"
            },
            "description": {
                "description": "Description of the attachment.",
                "type": "string"
            },
            "employeeFileUpload": {
                "description": "Information whether the attachment was uploaded by an employee (true) or an onboarding user (false)",
                "type": "boolean"
            }
        },
        "required": [
            "id",
            "dateCreated",
            "filename",
            "fileSize",
            "contentType",
            "employeeFileUpload"
        ]
    }
}
```

### GET /onboardings/{id}/attachments/{attachmentId}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system.",
            "type": "string"
        },
        "dateCreated": {
            "description": "Technical creation date of the attachment.",
            "type": "string",
            "format": "date-time"
        },
        "filename": {
            "description": "File name of the attachment.",
            "type": "string"
        },
        "fileSize": {
            "description": "File size of the attachment in Bytes.",
            "type": "integer"
        },
        "contentType": {
            "description": "Content type of the attachment.",
            "type": "string"
        },
        "description": {
            "description": "Description of the attachment.",
            "type": "string"
        },
        "employeeFileUpload": {
            "description": "Information whether the attachment was uploaded by an employee (true) or an onboarding user (false)",
            "type": "boolean"
        },
        "contentAsBase64": {
            "description": "Content of the attachment file encoded as base64.",
            "type": "string"
        }
    },
    "required": [
        "id",
        "dateCreated",
        "filename",
        "fileSize",
        "contentType",
        "employeeFileUpload",
        "contentAsBase64"
    ]
}
```

### GET /onboardings/{id}/attachments/{attachmentId}/pdf

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system.",
            "type": "string"
        },
        "dateCreated": {
            "description": "Technical creation date of the attachment.",
            "type": "string",
            "format": "date-time"
        },
        "filename": {
            "description": "File name of the attachment.",
            "type": "string"
        },
        "fileSize": {
            "description": "File size of the attachment in Bytes.",
            "type": "integer"
        },
        "contentType": {
            "description": "Content type of the attachment.",
            "type": "string"
        },
        "description": {
            "description": "Description of the attachment.",
            "type": "string"
        },
        "employeeFileUpload": {
            "description": "Information whether the attachment was uploaded by an employee (true) or an onboarding user (false)",
            "type": "boolean"
        },
        "contentAsBase64": {
            "description": "Content of the attachment file encoded as base64.",
            "type": "string"
        }
    },
    "required": [
        "id",
        "dateCreated",
        "filename",
        "fileSize",
        "contentType",
        "employeeFileUpload",
        "contentAsBase64"
    ]
}
```

### POST /onboardings/{id}/delete

#### Request

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        }
    },
    "required": ["success"]
}
```

## Organisation units

### GET /orgUnits/

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": [
        {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                },
                "parentId": {
                    "type": ["integer", "null"]
                }
            },
            "required": ["id", "name"]
        }
    ]
}
```

### GET /orgUnits/{id}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "parentId": {
            "type": ["integer", "null"]
        }
    },
    "required": ["id", "name"]
}
```

## Persons

### GET /persons/

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {
                "description": "Property is not settable - only returned by the system",
                "type": "integer"
            },
            "externalId": {
                "description": "Can be used to identify this resource in other systems. Must be unique or null.",
                "type": ["string", "null"]
            },
            "version": {
                "description": "Mandatory for all PUT requests",
                "type": "integer"
            },
            "salutation": {
                "description": "Person's salutation",
                "enum": ["MS", "MR", "MX", null]
            },
            "title": {
                "description": "Person title",
                "type": ["string", "null"]
            },
            "firstName": {
                "description": "Person's first name",
                "type": "string"
            },
            "lastName": {
                "description": "Person's last name",
                "type": "string"
            },
            "dateOfBirth": {
                "description": "Person's date of birth. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
                "type": ["string", "null"]
            },
            "address1": {
                "description": "Address-Field: Can only be set if countryIsoA2 is set.",
                "type": ["string", "null"]
            },
            "address2": {
                "description": "Address-Field: Can only be set if countryIsoA2 is set.",
                "type": ["string", "null"]
            },
            "address3": {
                "description": "Address-Field: Can only be set if countryIsoA2 is set.",
                "type": ["string", "null"]
            },
            "address4": {
                "description": "Address-Field: Can only be set if countryIsoA2 is set.",
                "type": ["string", "null"]
            },
            "address5": {
                "description": "Address-Field: Can only be set if countryIsoA2 is set.",
                "type": ["string", "null"]
            },
            "usState": {
                "description": "Address-Field: Can only be set if countryIsoA2 is set to 'US'",
                "enum": [
                    null,
                    "AL",
                    "AK",
                    "AZ",
                    "AR",
                    "CA",
                    "CO",
                    "CT",
                    "DE",
                    "DC",
                    "FL",
                    "GA",
                    "HI",
                    "ID",
                    "IL",
                    "IN",
                    "IA",
                    "KS",
                    "KY",
                    "LA",
                    "ME",
                    "MD",
                    "MA",
                    "MI",
                    "MN",
                    "MS",
                    "MO",
                    "MT",
                    "NE",
                    "NV",
                    "NH",
                    "NJ",
                    "NM",
                    "NY",
                    "NC",
                    "ND",
                    "OH",
                    "OK",
                    "OR",
                    "PA",
                    "RI",
                    "SC",
                    "SD",
                    "TN",
                    "TX",
                    "UT",
                    "VT",
                    "VA",
                    "WA",
                    "WV",
                    "WI",
                    "WY"
                ]
            },
            "zipCode": {
                "description": "Address-Field: Can only be set if countryIsoA2 is set.",
                "type": ["string", "null"]
            },
            "city": {
                "description": "Address-Field: Can only be set if countryIsoA2 is set.",
                "type": ["string", "null"]
            },
            "countryIsoA2": {
                "description": "Address-Field: IsoA2 abbr. of person's country.",
                "type": ["string", "null"]
            },
            "email": {
                "description": "Person's email",
                "type": ["string", "null"]
            },
            "telephone": {
                "description": "Person's telephone",
                "type": ["string", "null"]
            },
            "alternativeTelephone": {
                "description": "Person's alternative telephone",
                "type": ["string", "null"]
            },
            "skypeName": {
                "description": "Person's skype name",
                "type": ["string", "null"]
            },
            "profileLink": {
                "description": "Person's profile link",
                "type": ["string", "null"]
            },
            "degreeId": {
                "description": "Person's degree - must match a configured internal-name of degree master data.",
                "type": ["string", "null"]
            },
            "education": {
                "description": "Vocational Education",
                "type": ["string", "null"]
            },
            "study": {
                "description": "Person's stury",
                "type": ["string", "null"]
            },
            "lastPosition": {
                "description": "Person's last position",
                "type": ["string", "null"]
            },
            "specialMarkIds": {
                "description": "List of special marks of person by internal-name.",
                "items": {
                    "type": ["string"]
                },
                "type": "array"
            },
            "specialMarkIA": {
                "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Internal Applicant')",
                "type": "boolean"
            },
            "specialMarkDIS": {
                "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Severely Disabled Applicant')",
                "type": "boolean"
            },
            "specialMarkREL": {
                "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Relatives Within Company')",
                "type": "boolean"
            },
            "specialMarkVIP": {
                "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'VIP Applicant')",
                "type": "boolean"
            },
            "specialMarkREF": {
                "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Employee Referral')",
                "type": "boolean"
            },
            "specialMarkHRP": {
                "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'HR Services Provider')",
                "type": "boolean"
            },
            "specialMarkBL": {
                "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Blacklist')",
                "type": "boolean"
            },
            "specialMarkGPA": {
                "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Group of Companies Applicant')",
                "type": "boolean"
            },
            "keywords": {
                "description": "Person's list of keywords",
                "items": {
                    "type": ["string"]
                },
                "type": "array"
            },
            "applications": {
                "description": "Person's list of applications",
                "items": {
                    "description": "",
                    "properties": {
                        "externalId": {
                            "description": "Optional external id of application",
                            "type": ["string", "null"]
                        },
                        "id": {
                            "description": "Identifier of application",
                            "type": "integer"
                        }
                    },
                    "type": "object"
                },
                "type": "array"
            }
        },
        "required": ["id", "firstName", "lastName"]
    }
}
```

### POST /persons/

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "salutation": {
            "description": "Person's salutation",
            "enum": ["MS", "MR", "MX", null]
        },
        "title": {
            "description": "Person title",
            "type": ["string", "null"]
        },
        "firstName": {
            "description": "Person's first name",
            "type": "string"
        },
        "lastName": {
            "description": "Person's last name",
            "type": "string"
        },
        "dateOfBirth": {
            "description": "Person's date of birth. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "address1": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address2": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address3": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address4": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address5": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "usState": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set to 'US'",
            "enum": [
                null,
                "AL",
                "AK",
                "AZ",
                "AR",
                "CA",
                "CO",
                "CT",
                "DE",
                "DC",
                "FL",
                "GA",
                "HI",
                "ID",
                "IL",
                "IN",
                "IA",
                "KS",
                "KY",
                "LA",
                "ME",
                "MD",
                "MA",
                "MI",
                "MN",
                "MS",
                "MO",
                "MT",
                "NE",
                "NV",
                "NH",
                "NJ",
                "NM",
                "NY",
                "NC",
                "ND",
                "OH",
                "OK",
                "OR",
                "PA",
                "RI",
                "SC",
                "SD",
                "TN",
                "TX",
                "UT",
                "VT",
                "VA",
                "WA",
                "WV",
                "WI",
                "WY"
            ]
        },
        "zipCode": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "city": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "countryIsoA2": {
            "description": "Address-Field: IsoA2 abbr. of person's country.",
            "type": ["string", "null"]
        },
        "email": {
            "description": "Person's email",
            "type": ["string", "null"]
        },
        "telephone": {
            "description": "Person's telephone",
            "type": ["string", "null"]
        },
        "alternativeTelephone": {
            "description": "Person's alternative telephone",
            "type": ["string", "null"]
        },
        "skypeName": {
            "description": "Person's skype name",
            "type": ["string", "null"]
        },
        "profileLink": {
            "description": "Person's profile link",
            "type": ["string", "null"]
        },
        "degreeId": {
            "description": "Person's degree - must match a configured internal-name of degree master data.",
            "type": ["string", "null"]
        },
        "education": {
            "description": "Vocational Education",
            "type": ["string", "null"]
        },
        "study": {
            "description": "Person's study",
            "type": ["string", "null"]
        },
        "lastPosition": {
            "description": "Person's last position",
            "type": ["string", "null"]
        },
        "specialMarkIds": {
            "description": "List of special marks of person by internal-name.",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "specialMarkIA": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Internal Applicant')",
            "type": "boolean"
        },
        "specialMarkDIS": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Severely Disabled Applicant')",
            "type": "boolean"
        },
        "specialMarkREL": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Relatives Within Company')",
            "type": "boolean"
        },
        "specialMarkVIP": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'VIP Applicant')",
            "type": "boolean"
        },
        "specialMarkREF": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Employee Referral')",
            "type": "boolean"
        },
        "specialMarkHRP": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'HR Services Provider')",
            "type": "boolean"
        },
        "specialMarkBL": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Blacklist')",
            "type": "boolean"
        },
        "specialMarkGPA": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Group of Companies Applicant')",
            "type": "boolean"
        }
    },
    "required": ["firstName", "lastName"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "salutation": {
            "description": "Person's salutation",
            "enum": ["MS", "MR", "MX", null]
        },
        "title": {
            "description": "Person title",
            "type": ["string", "null"]
        },
        "firstName": {
            "description": "Person's first name",
            "type": "string"
        },
        "lastName": {
            "description": "Person's last name",
            "type": "string"
        },
        "dateOfBirth": {
            "description": "Person's date of birth. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "address1": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address2": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address3": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address4": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address5": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "usState": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set to 'US'",
            "enum": [
                null,
                "AL",
                "AK",
                "AZ",
                "AR",
                "CA",
                "CO",
                "CT",
                "DE",
                "DC",
                "FL",
                "GA",
                "HI",
                "ID",
                "IL",
                "IN",
                "IA",
                "KS",
                "KY",
                "LA",
                "ME",
                "MD",
                "MA",
                "MI",
                "MN",
                "MS",
                "MO",
                "MT",
                "NE",
                "NV",
                "NH",
                "NJ",
                "NM",
                "NY",
                "NC",
                "ND",
                "OH",
                "OK",
                "OR",
                "PA",
                "RI",
                "SC",
                "SD",
                "TN",
                "TX",
                "UT",
                "VT",
                "VA",
                "WA",
                "WV",
                "WI",
                "WY"
            ]
        },
        "zipCode": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "city": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "countryIsoA2": {
            "description": "Address-Field: IsoA2 abbr. of person's country.",
            "type": ["string", "null"]
        },
        "email": {
            "description": "Person's email",
            "type": ["string", "null"]
        },
        "telephone": {
            "description": "Person's telephone",
            "type": ["string", "null"]
        },
        "alternativeTelephone": {
            "description": "Person's alternative telephone",
            "type": ["string", "null"]
        },
        "skypeName": {
            "description": "Person's skype name",
            "type": ["string", "null"]
        },
        "profileLink": {
            "description": "Person's profile link",
            "type": ["string", "null"]
        },
        "degreeId": {
            "description": "Person's degree - must match a configured internal-name of degree master data.",
            "type": ["string", "null"]
        },
        "education": {
            "description": "Vocational Education",
            "type": ["string", "null"]
        },
        "study": {
            "description": "Person's study",
            "type": ["string", "null"]
        },
        "lastPosition": {
            "description": "Person's last position",
            "type": ["string", "null"]
        },
        "specialMarkIds": {
            "description": "List of special marks of person by internal-name.",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "specialMarkIA": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Internal Applicant')",
            "type": "boolean"
        },
        "specialMarkDIS": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Severely Disabled Applicant')",
            "type": "boolean"
        },
        "specialMarkREL": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Relatives Within Company')",
            "type": "boolean"
        },
        "specialMarkVIP": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'VIP Applicant')",
            "type": "boolean"
        },
        "specialMarkREF": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Employee Referral')",
            "type": "boolean"
        },
        "specialMarkHRP": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'HR Services Provider')",
            "type": "boolean"
        },
        "specialMarkBL": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Blacklist')",
            "type": "boolean"
        },
        "specialMarkGPA": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Group of Companies Applicant')",
            "type": "boolean"
        },
        "keywords": {
            "description": "Person's list of keywords",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "applications": {
            "description": "Person's list of applications",
            "items": {
                "description": "",
                "properties": {
                    "externalId": {
                        "description": "Optional external id of application",
                        "type": ["string", "null"]
                    },
                    "id": {
                        "description": "Identifier of application",
                        "type": "integer"
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": ["id", "firstName", "lastName"]
}
```

### GET /persons/?externalId={externalId}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "salutation": {
            "description": "Person's salutation",
            "enum": ["MS", "MR", "MX", null]
        },
        "title": {
            "description": "Person title",
            "type": ["string", "null"]
        },
        "firstName": {
            "description": "Person's first name",
            "type": "string"
        },
        "lastName": {
            "description": "Person's last name",
            "type": "string"
        },
        "dateOfBirth": {
            "description": "Person's date of birth. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "address1": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address2": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address3": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address4": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address5": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "usState": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set to 'US'",
            "enum": [
                null,
                "AL",
                "AK",
                "AZ",
                "AR",
                "CA",
                "CO",
                "CT",
                "DE",
                "DC",
                "FL",
                "GA",
                "HI",
                "ID",
                "IL",
                "IN",
                "IA",
                "KS",
                "KY",
                "LA",
                "ME",
                "MD",
                "MA",
                "MI",
                "MN",
                "MS",
                "MO",
                "MT",
                "NE",
                "NV",
                "NH",
                "NJ",
                "NM",
                "NY",
                "NC",
                "ND",
                "OH",
                "OK",
                "OR",
                "PA",
                "RI",
                "SC",
                "SD",
                "TN",
                "TX",
                "UT",
                "VT",
                "VA",
                "WA",
                "WV",
                "WI",
                "WY"
            ]
        },
        "zipCode": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "city": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "countryIsoA2": {
            "description": "Address-Field: IsoA2 abbr. of person's country.",
            "type": ["string", "null"]
        },
        "email": {
            "description": "Person's email",
            "type": ["string", "null"]
        },
        "telephone": {
            "description": "Person's telephone",
            "type": ["string", "null"]
        },
        "alternativeTelephone": {
            "description": "Person's alternative telephone",
            "type": ["string", "null"]
        },
        "skypeName": {
            "description": "Person's skype name",
            "type": ["string", "null"]
        },
        "profileLink": {
            "description": "Person's profile link",
            "type": ["string", "null"]
        },
        "degreeId": {
            "description": "Person's degree - must match a configured internal-name of degree master data.",
            "type": ["string", "null"]
        },
        "education": {
            "description": "Vocational Education",
            "type": ["string", "null"]
        },
        "study": {
            "description": "Person's study",
            "type": ["string", "null"]
        },
        "lastPosition": {
            "description": "Person's last position",
            "type": ["string", "null"]
        },
        "specialMarkIds": {
            "description": "List of special marks of person by internal-name.",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "specialMarkIA": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Internal Applicant')",
            "type": "boolean"
        },
        "specialMarkDIS": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Severely Disabled Applicant')",
            "type": "boolean"
        },
        "specialMarkREL": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Relatives Within Company')",
            "type": "boolean"
        },
        "specialMarkVIP": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'VIP Applicant')",
            "type": "boolean"
        },
        "specialMarkREF": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Employee Referral')",
            "type": "boolean"
        },
        "specialMarkHRP": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'HR Services Provider')",
            "type": "boolean"
        },
        "specialMarkBL": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Blacklist')",
            "type": "boolean"
        },
        "specialMarkGPA": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Group of Companies Applicant')",
            "type": "boolean"
        },
        "keywords": {
            "description": "Person's list of keywords",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "applications": {
            "description": "Person's list of applications",
            "items": {
                "description": "",
                "properties": {
                    "externalId": {
                        "description": "Optional external id of application",
                        "type": ["string", "null"]
                    },
                    "id": {
                        "description": "Identifier of application",
                        "type": "integer"
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": ["id", "firstName", "lastName"]
}
```

### GET /persons/{id}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "salutation": {
            "description": "Person's salutation",
            "enum": ["MS", "MR", "MX", null]
        },
        "title": {
            "description": "Person title",
            "type": ["string", "null"]
        },
        "firstName": {
            "description": "Person's first name",
            "type": "string"
        },
        "lastName": {
            "description": "Person's last name",
            "type": "string"
        },
        "dateOfBirth": {
            "description": "Person's date of birth. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "address1": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address2": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address3": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address4": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address5": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "usState": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set to 'US'",
            "enum": [
                null,
                "AL",
                "AK",
                "AZ",
                "AR",
                "CA",
                "CO",
                "CT",
                "DE",
                "DC",
                "FL",
                "GA",
                "HI",
                "ID",
                "IL",
                "IN",
                "IA",
                "KS",
                "KY",
                "LA",
                "ME",
                "MD",
                "MA",
                "MI",
                "MN",
                "MS",
                "MO",
                "MT",
                "NE",
                "NV",
                "NH",
                "NJ",
                "NM",
                "NY",
                "NC",
                "ND",
                "OH",
                "OK",
                "OR",
                "PA",
                "RI",
                "SC",
                "SD",
                "TN",
                "TX",
                "UT",
                "VT",
                "VA",
                "WA",
                "WV",
                "WI",
                "WY"
            ]
        },
        "zipCode": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "city": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "countryIsoA2": {
            "description": "Address-Field: IsoA2 abbr. of person's country.",
            "type": ["string", "null"]
        },
        "email": {
            "description": "Person's email",
            "type": ["string", "null"]
        },
        "telephone": {
            "description": "Person's telephone",
            "type": ["string", "null"]
        },
        "alternativeTelephone": {
            "description": "Person's alternative telephone",
            "type": ["string", "null"]
        },
        "skypeName": {
            "description": "Person's skype name",
            "type": ["string", "null"]
        },
        "profileLink": {
            "description": "Person's profile link",
            "type": ["string", "null"]
        },
        "degreeId": {
            "description": "Person's degree - must match a configured internal-name of degree master data.",
            "type": ["string", "null"]
        },
        "education": {
            "description": "Vocational Education",
            "type": ["string", "null"]
        },
        "study": {
            "description": "Person's study",
            "type": ["string", "null"]
        },
        "lastPosition": {
            "description": "Person's last position",
            "type": ["string", "null"]
        },
        "specialMarkIds": {
            "description": "List of special marks of person by internal-name.",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "specialMarkIA": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Internal Applicant')",
            "type": "boolean"
        },
        "specialMarkDIS": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Severely Disabled Applicant')",
            "type": "boolean"
        },
        "specialMarkREL": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Relatives Within Company')",
            "type": "boolean"
        },
        "specialMarkVIP": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'VIP Applicant')",
            "type": "boolean"
        },
        "specialMarkREF": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Employee Referral')",
            "type": "boolean"
        },
        "specialMarkHRP": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'HR Services Provider')",
            "type": "boolean"
        },
        "specialMarkBL": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Blacklist')",
            "type": "boolean"
        },
        "specialMarkGPA": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Group of Companies Applicant')",
            "type": "boolean"
        },
        "keywords": {
            "description": "Person's list of keywords",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "applications": {
            "description": "Person's list of applications",
            "items": {
                "description": "",
                "properties": {
                    "externalId": {
                        "description": "Optional external id of application",
                        "type": ["string", "null"]
                    },
                    "id": {
                        "description": "Identifier of application",
                        "type": "integer"
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": ["id", "firstName", "lastName"]
}
```

### PUT /persons/{id}

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "salutation": {
            "description": "Person's salutation",
            "enum": ["MS", "MR", "MX", null]
        },
        "title": {
            "description": "Person title",
            "type": ["string", "null"]
        },
        "firstName": {
            "description": "Person's first name",
            "type": "string"
        },
        "lastName": {
            "description": "Person's last name",
            "type": "string"
        },
        "dateOfBirth": {
            "description": "Person's date of birth. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "address1": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address2": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address3": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address4": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address5": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "usState": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set to 'US'",
            "enum": [
                null,
                "AL",
                "AK",
                "AZ",
                "AR",
                "CA",
                "CO",
                "CT",
                "DE",
                "DC",
                "FL",
                "GA",
                "HI",
                "ID",
                "IL",
                "IN",
                "IA",
                "KS",
                "KY",
                "LA",
                "ME",
                "MD",
                "MA",
                "MI",
                "MN",
                "MS",
                "MO",
                "MT",
                "NE",
                "NV",
                "NH",
                "NJ",
                "NM",
                "NY",
                "NC",
                "ND",
                "OH",
                "OK",
                "OR",
                "PA",
                "RI",
                "SC",
                "SD",
                "TN",
                "TX",
                "UT",
                "VT",
                "VA",
                "WA",
                "WV",
                "WI",
                "WY"
            ]
        },
        "zipCode": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "city": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "countryIsoA2": {
            "description": "Address-Field: IsoA2 abbr. of person's country.",
            "type": ["string", "null"]
        },
        "email": {
            "description": "Person's email",
            "type": ["string", "null"]
        },
        "telephone": {
            "description": "Person's telephone",
            "type": ["string", "null"]
        },
        "alternativeTelephone": {
            "description": "Person's alternative telephone",
            "type": ["string", "null"]
        },
        "skypeName": {
            "description": "Person's skype name",
            "type": ["string", "null"]
        },
        "profileLink": {
            "description": "Person's profile link",
            "type": ["string", "null"]
        },
        "degreeId": {
            "description": "Person's degree - must match a configured internal-name of degree master data.",
            "type": ["string", "null"]
        },
        "education": {
            "description": "Vocational Education",
            "type": ["string", "null"]
        },
        "study": {
            "description": "Person's study",
            "type": ["string", "null"]
        },
        "lastPosition": {
            "description": "Person's last position",
            "type": ["string", "null"]
        },
        "specialMarkIds": {
            "description": "List of special marks of person by internal-name.",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "specialMarkIA": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Internal Applicant')",
            "type": "boolean"
        },
        "specialMarkDIS": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Severely Disabled Applicant')",
            "type": "boolean"
        },
        "specialMarkREL": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Relatives Within Company')",
            "type": "boolean"
        },
        "specialMarkVIP": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'VIP Applicant')",
            "type": "boolean"
        },
        "specialMarkREF": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Employee Referral')",
            "type": "boolean"
        },
        "specialMarkHRP": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'HR Services Provider')",
            "type": "boolean"
        },
        "specialMarkBL": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Blacklist')",
            "type": "boolean"
        },
        "specialMarkGPA": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Group of Companies Applicant')",
            "type": "boolean"
        }
    },
    "required": ["version", "firstName", "lastName"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "description": "Property is not settable - only returned by the system",
            "type": "integer"
        },
        "externalId": {
            "description": "Can be used to identify this resource in other systems. Must be unique or null.",
            "type": ["string", "null"]
        },
        "version": {
            "description": "Mandatory for all PUT requests",
            "type": "integer"
        },
        "salutation": {
            "description": "Person's salutation",
            "enum": ["MS", "MR", "MX", null]
        },
        "title": {
            "description": "Person title",
            "type": ["string", "null"]
        },
        "firstName": {
            "description": "Person's first name",
            "type": "string"
        },
        "lastName": {
            "description": "Person's last name",
            "type": "string"
        },
        "dateOfBirth": {
            "description": "Person's date of birth. Can be 'null' or ISO8601 date format (yyyy-MM-dd).",
            "type": ["string", "null"]
        },
        "address1": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address2": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address3": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address4": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "address5": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "usState": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set to 'US'",
            "enum": [
                null,
                "AL",
                "AK",
                "AZ",
                "AR",
                "CA",
                "CO",
                "CT",
                "DE",
                "DC",
                "FL",
                "GA",
                "HI",
                "ID",
                "IL",
                "IN",
                "IA",
                "KS",
                "KY",
                "LA",
                "ME",
                "MD",
                "MA",
                "MI",
                "MN",
                "MS",
                "MO",
                "MT",
                "NE",
                "NV",
                "NH",
                "NJ",
                "NM",
                "NY",
                "NC",
                "ND",
                "OH",
                "OK",
                "OR",
                "PA",
                "RI",
                "SC",
                "SD",
                "TN",
                "TX",
                "UT",
                "VT",
                "VA",
                "WA",
                "WV",
                "WI",
                "WY"
            ]
        },
        "zipCode": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "city": {
            "description": "Address-Field: Can only be set if countryIsoA2 is set.",
            "type": ["string", "null"]
        },
        "countryIsoA2": {
            "description": "Address-Field: IsoA2 abbr. of person's country.",
            "type": ["string", "null"]
        },
        "email": {
            "description": "Person's email",
            "type": ["string", "null"]
        },
        "telephone": {
            "description": "Person's telephone",
            "type": ["string", "null"]
        },
        "alternativeTelephone": {
            "description": "Person's alternative telephone",
            "type": ["string", "null"]
        },
        "skypeName": {
            "description": "Person's skype name",
            "type": ["string", "null"]
        },
        "profileLink": {
            "description": "Person's profile link",
            "type": ["string", "null"]
        },
        "degreeId": {
            "description": "Person's degree - must match a configured internal-name of degree master data.",
            "type": ["string", "null"]
        },
        "education": {
            "description": "Vocational Education",
            "type": ["string", "null"]
        },
        "study": {
            "description": "Person's study",
            "type": ["string", "null"]
        },
        "lastPosition": {
            "description": "Person's last position",
            "type": ["string", "null"]
        },
        "specialMarkIds": {
            "description": "List of special marks of person by internal-name.",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "specialMarkIA": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Internal Applicant')",
            "type": "boolean"
        },
        "specialMarkDIS": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Severely Disabled Applicant')",
            "type": "boolean"
        },
        "specialMarkREL": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Relatives Within Company')",
            "type": "boolean"
        },
        "specialMarkVIP": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'VIP Applicant')",
            "type": "boolean"
        },
        "specialMarkREF": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Employee Referral')",
            "type": "boolean"
        },
        "specialMarkHRP": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'HR Services Provider')",
            "type": "boolean"
        },
        "specialMarkBL": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Blacklist')",
            "type": "boolean"
        },
        "specialMarkGPA": {
            "description": "Deprecated! Use property 'specialMarkIds' instead. (Special Characteristic: 'Group of Companies Applicant')",
            "type": "boolean"
        },
        "keywords": {
            "description": "Person's list of keywords",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "applications": {
            "description": "Person's list of applications",
            "items": {
                "description": "",
                "properties": {
                    "externalId": {
                        "description": "Optional external id of application",
                        "type": ["string", "null"]
                    },
                    "id": {
                        "description": "Identifier of application",
                        "type": "integer"
                    }
                },
                "type": "object"
            },
            "type": "array"
        }
    },
    "required": ["id", "firstName", "lastName"]
}
```

### POST /persons/{id}/delete

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        }
    },
    "required": ["success"]
}
```

### GET /persons/{id}/photo

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "contentType": {
            "description": "Content type of the photo.",
            "type": "string"
        },
        "fileSize": {
            "description": "File size of the photo.",
            "type": "integer"
        },
        "dateCreated": {
            "description": "Technical creation date of the photo.",
            "type": "string",
            "format": "date-time"
        },
        "filename": {
            "description": "File name of the photo.",
            "type": "string"
        },
        "contentAsBase64": {
            "description": "Content of the photo encoded as base64.",
            "type": "string"
        }
    },
    "required": [
        "contentType",
        "fileSize",
        "dateCreated",
        "filename",
        "contentAsBase64"
    ]
}
```

### POST /persons/{id}/photo

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "filename": {
            "description": "File name of the photo.",
            "type": "string"
        },
        "contentAsBase64": {
            "description": "Content of the photo file encoded as base64.",
            "type": "string"
        }
    },
    "required": ["filename", "contentAsBase64"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        }
    },
    "required": ["success"]
}
```

### POST /persons/{id}/photo/delete

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        }
    },
    "required": ["success"]
}
```

## Users

### GET /dvinciUsers/

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": [
        {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "version": {
                    "type": "integer"
                },
                "externalId": {
                    "type": ["string", "null"]
                },
                "username": {
                    "type": "string"
                },
                "samlSsoEnabled": {
                    "type": "boolean"
                },
                "formAuthenticationEnabled": {
                    "type": "boolean"
                },
                "salutation": {
                    "enum": ["MR", "MS", "MX"]
                },
                "title": {
                    "type": ["string", "null"]
                },
                "firstName": {
                    "type": "string"
                },
                "lastName": {
                    "type": "string"
                },
                "displayName": {
                    "type": "string"
                },
                "email": {
                    "type": "string"
                },
                "orgUnitId": {
                    "type": "integer"
                },
                "languageId": {
                    "type": "string"
                },
                "street": {
                    "type": ["string", "null"]
                },
                "number": {
                    "type": ["string", "null"]
                },
                "additionalAddress": {
                    "type": ["string", "null"]
                },
                "zipCode": {
                    "type": ["string", "null"]
                },
                "city": {
                    "type": ["string", "null"]
                },
                "countryIsoA2": {
                    "type": "string"
                },
                "timeZone": {
                    "type": "string"
                },
                "telephone": {
                    "type": ["string", "null"]
                },
                "mobile": {
                    "type": ["string", "null"]
                },
                "companyId": {
                    "type": ["string", "null"]
                },
                "signingAuthority": {
                    "type": ["string", "null"]
                },
                "positionAuthority": {
                    "type": ["string", "null"]
                },
                "division": {
                    "type": ["string", "null"]
                },
                "dailyEmailNotification": {
                    "type": "boolean"
                },
                "dailyEmailNotificationTypes": {
                    "enum": [
                        "NEW_APPLICATIONS",
                        "OVERDUE_TASKS",
                        "EXPIRING_JOB_PUBLICATION_PLACEMENTS",
                        "EXPIRING_EXTERNAL_JOB_PUBLICATION_PLACEMENTS"
                    ]
                },
                "notifyOnNewCandidateCommunication": {
                    "type": "boolean"
                },
                "roleIds": {
                    "description": "List of roles",
                    "items": {
                        "type": ["string"]
                    },
                    "type": "array"
                },
                "userGroupIds": {
                    "description": "List of user group ids",
                    "items": {
                        "type": ["integer"]
                    },
                    "type": "array"
                },
                "dataForExternalSystems": {
                    "description": "Fields and values are freely configurable in d.vinci application",
                    "properties": {
                        "field": {
                            "type": ["string"]
                        },
                        "value": {
                            "type": ["string"]
                        }
                    },
                    "type": "array"
                }
            },
            "required": [
                "id",
                "version",
                "externalId",
                "username",
                "samlSsoEnabled",
                "formAuthenticationEnabled",
                "salutation",
                "title",
                "firstName",
                "lastName",
                "displayName",
                "email",
                "orgUnitId",
                "languageId",
                "street",
                "number",
                "additionalAddress",
                "zipCode",
                "city",
                "countryIsoA2",
                "timeZone",
                "telephone",
                "mobile",
                "companyId",
                "division",
                "dailyEmailNotification",
                "dailyEmailNotificationTypes",
                "notifyOnNewCandidateCommunication",
                "roleIds",
                "userGroupIds",
                "dataForExternalSystems"
            ]
        }
    ]
}
```

### POST /dvinciUsers/

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "username": {
            "type": "string"
        },
        "externalId": {
            "type": ["string", "null"]
        },
        "samlSsoEnabled": {
            "type": "boolean"
        },
        "formAuthenticationEnabled": {
            "type": "boolean"
        },
        "salutation": {
            "enum": ["MR", "MS", "MX"]
        },
        "title": {
            "type": ["string", "null"]
        },
        "firstName": {
            "type": "string"
        },
        "lastName": {
            "type": "string"
        },
        "email": {
            "type": "string"
        },
        "orgUnitId": {
            "type": "integer"
        },
        "languageId": {
            "type": "string"
        },
        "street": {
            "type": ["string", "null"]
        },
        "number": {
            "type": ["string", "null"]
        },
        "additionalAddress": {
            "type": ["string", "null"]
        },
        "zipCode": {
            "type": ["string", "null"]
        },
        "city": {
            "type": ["string", "null"]
        },
        "countryIsoA2": {
            "type": "string"
        },
        "telephone": {
            "type": ["string", "null"]
        },
        "mobile": {
            "type": ["string", "null"]
        },
        "companyId": {
            "type": ["string", "null"]
        },
        "signingAuthority": {
            "type": ["string", "null"]
        },
        "positionAuthority": {
            "type": ["string", "null"]
        },
        "division": {
            "type": ["string", "null"]
        },
        "dailyEmailNotification": {
            "type": "boolean"
        },
        "dailyEmailNotificationTypes": {
            "enum": [
                "NEW_APPLICATIONS",
                "OVERDUE_TASKS",
                "EXPIRING_JOB_PUBLICATION_PLACEMENTS",
                "EXPIRING_EXTERNAL_JOB_PUBLICATION_PLACEMENTS"
            ]
        },
        "notifyOnNewCandidateCommunication": {
            "type": "boolean"
        },
        "roleIds": {
            "description": "List of roles",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "userGroupIds": {
            "description": "List of user group ids",
            "items": {
                "type": ["integer"]
            },
            "type": "array"
        },
        "dataForExternalSystems": {
            "description": "Fields and values are freely configurable in d.vinci application",
            "properties": {
                "field": {
                    "type": ["string"]
                },
                "value": {
                    "type": ["string"]
                }
            },
            "type": "array"
        }
    },
    "required": [
        "username",
        "salutation",
        "firstName",
        "lastName",
        "email",
        "orgUnitId",
        "languageId",
        "roleIds"
    ]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "version": {
            "type": "integer"
        },
        "username": {
            "type": "string"
        },
        "externalId": {
            "type": ["string", "null"]
        },
        "samlSsoEnabled": {
            "type": "boolean"
        },
        "formAuthenticationEnabled": {
            "type": "boolean"
        },
        "salutation": {
            "enum": ["MR", "MS", "MX"]
        },
        "title": {
            "type": ["string", "null"]
        },
        "firstName": {
            "type": "string"
        },
        "lastName": {
            "type": "string"
        },
        "displayName": {
            "type": "string"
        },
        "email": {
            "type": "string"
        },
        "orgUnitId": {
            "type": "integer"
        },
        "languageId": {
            "type": "string"
        },
        "street": {
            "type": ["string", "null"]
        },
        "number": {
            "type": ["string", "null"]
        },
        "additionalAddress": {
            "type": ["string", "null"]
        },
        "zipCode": {
            "type": ["string", "null"]
        },
        "city": {
            "type": ["string", "null"]
        },
        "countryIsoA2": {
            "type": "string"
        },
        "timeZone": {
            "type": "string"
        },
        "telephone": {
            "type": ["string", "null"]
        },
        "mobile": {
            "type": ["string", "null"]
        },
        "companyId": {
            "type": ["string", "null"]
        },
        "signingAuthority": {
            "type": ["string", "null"]
        },
        "positionAuthority": {
            "type": ["string", "null"]
        },
        "division": {
            "type": ["string", "null"]
        },
        "dailyEmailNotification": {
            "type": "boolean"
        },
        "dailyEmailNotificationTypes": {
            "enum": [
                "NEW_APPLICATIONS",
                "OVERDUE_TASKS",
                "EXPIRING_JOB_PUBLICATION_PLACEMENTS",
                "EXPIRING_EXTERNAL_JOB_PUBLICATION_PLACEMENTS"
            ]
        },
        "notifyOnNewCandidateCommunication": {
            "type": "boolean"
        },
        "roleIds": {
            "description": "List of roles",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "userGroupIds": {
            "description": "List of user group ids",
            "items": {
                "type": ["integer"]
            },
            "type": "array"
        },
        "dataForExternalSystems": {
            "description": "Fields and values are freely configurable in d.vinci application",
            "properties": {
                "field": {
                    "type": ["string"]
                },
                "value": {
                    "type": ["string"]
                }
            },
            "type": "array"
        }
    },
    "required": [
        "id",
        "version",
        "externalId",
        "username",
        "samlSsoEnabled",
        "formAuthenticationEnabled",
        "salutation",
        "title",
        "firstName",
        "lastName",
        "displayName",
        "email",
        "orgUnitId",
        "languageId",
        "street",
        "number",
        "additionalAddress",
        "zipCode",
        "city",
        "countryIsoA2",
        "timeZone",
        "telephone",
        "mobile",
        "companyId",
        "division",
        "dailyEmailNotification",
        "dailyEmailNotificationTypes",
        "notifyOnNewCandidateCommunication",
        "roleIds",
        "userGroupIds",
        "dataForExternalSystems"
    ]
}
```

### GET /dvinciUsers/{id}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "version": {
            "type": "integer"
        },
        "username": {
            "type": "string"
        },
        "externalId": {
            "type": ["string", "null"]
        },
        "samlSsoEnabled": {
            "type": "boolean"
        },
        "formAuthenticationEnabled": {
            "type": "boolean"
        },
        "salutation": {
            "enum": ["MR", "MS", "MX"]
        },
        "title": {
            "type": ["string", "null"]
        },
        "firstName": {
            "type": "string"
        },
        "lastName": {
            "type": "string"
        },
        "displayName": {
            "type": "string"
        },
        "email": {
            "type": "string"
        },
        "orgUnitId": {
            "type": "integer"
        },
        "languageId": {
            "type": "string"
        },
        "street": {
            "type": ["string", "null"]
        },
        "number": {
            "type": ["string", "null"]
        },
        "additionalAddress": {
            "type": ["string", "null"]
        },
        "zipCode": {
            "type": ["string", "null"]
        },
        "city": {
            "type": ["string", "null"]
        },
        "countryIsoA2": {
            "type": "string"
        },
        "timeZone": {
            "type": "string"
        },
        "telephone": {
            "type": ["string", "null"]
        },
        "mobile": {
            "type": ["string", "null"]
        },
        "companyId": {
            "type": ["string", "null"]
        },
        "signingAuthority": {
            "type": ["string", "null"]
        },
        "positionAuthority": {
            "type": ["string", "null"]
        },
        "division": {
            "type": ["string", "null"]
        },
        "dailyEmailNotification": {
            "type": "boolean"
        },
        "dailyEmailNotificationTypes": {
            "enum": [
                "NEW_APPLICATIONS",
                "OVERDUE_TASKS",
                "EXPIRING_JOB_PUBLICATION_PLACEMENTS",
                "EXPIRING_EXTERNAL_JOB_PUBLICATION_PLACEMENTS"
            ]
        },
        "notifyOnNewCandidateCommunication": {
            "type": "boolean"
        },
        "roleIds": {
            "description": "List of roles",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "userGroupIds": {
            "description": "List of user group ids",
            "items": {
                "type": ["integer"]
            },
            "type": "array"
        },
        "dataForExternalSystems": {
            "description": "Fields and values are freely configurable in d.vinci application",
            "properties": {
                "field": {
                    "type": ["string"]
                },
                "value": {
                    "type": ["string"]
                }
            },
            "type": "array"
        }
    },
    "required": [
        "id",
        "version",
        "externalId",
        "username",
        "samlSsoEnabled",
        "formAuthenticationEnabled",
        "salutation",
        "title",
        "firstName",
        "lastName",
        "displayName",
        "email",
        "orgUnitId",
        "languageId",
        "street",
        "number",
        "additionalAddress",
        "zipCode",
        "city",
        "countryIsoA2",
        "timeZone",
        "telephone",
        "mobile",
        "companyId",
        "division",
        "dailyEmailNotification",
        "dailyEmailNotificationTypes",
        "notifyOnNewCandidateCommunication",
        "roleIds",
        "userGroupIds",
        "dataForExternalSystems"
    ]
}
```

### PUT /dvinciUsers/{id}

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "version": {
            "type": "integer"
        },
        "username": {
            "type": "string"
        },
        "externalId": {
            "type": ["string", "null"]
        },
        "samlSsoEnabled": {
            "type": "boolean"
        },
        "formAuthenticationEnabled": {
            "type": "boolean"
        },
        "salutation": {
            "enum": ["MR", "MS", "MX"]
        },
        "title": {
            "type": ["string", "null"]
        },
        "firstName": {
            "type": "string"
        },
        "lastName": {
            "type": "string"
        },
        "email": {
            "type": "string"
        },
        "languageId": {
            "type": "string"
        },
        "street": {
            "type": ["string", "null"]
        },
        "number": {
            "type": ["string", "null"]
        },
        "additionalAddress": {
            "type": ["string", "null"]
        },
        "zipCode": {
            "type": ["string", "null"]
        },
        "city": {
            "type": ["string", "null"]
        },
        "countryIsoA2": {
            "type": "string"
        },
        "timeZone": {
            "type": "string"
        },
        "telephone": {
            "type": ["string", "null"]
        },
        "mobile": {
            "type": ["string", "null"]
        },
        "companyId": {
            "type": ["string", "null"]
        },
        "signingAuthority": {
            "type": ["string", "null"]
        },
        "positionAuthority": {
            "type": ["string", "null"]
        },
        "division": {
            "type": ["string", "null"]
        },
        "dailyEmailNotification": {
            "type": "boolean"
        },
        "dailyEmailNotificationTypes": {
            "enum": [
                "NEW_APPLICATIONS",
                "OVERDUE_TASKS",
                "EXPIRING_JOB_PUBLICATION_PLACEMENTS",
                "EXPIRING_EXTERNAL_JOB_PUBLICATION_PLACEMENTS"
            ]
        },
        "notifyOnNewCandidateCommunication": {
            "type": "boolean"
        },
        "roleIds": {
            "description": "List of roles",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "userGroupIds": {
            "description": "List of user group ids",
            "items": {
                "type": ["integer"]
            },
            "type": "array"
        },
        "dataForExternalSystems": {
            "description": "Fields and values are freely configurable in d.vinci application",
            "properties": {
                "field": {
                    "type": ["string"]
                },
                "value": {
                    "type": ["string"]
                }
            },
            "type": "array"
        }
    },
    "required": [
        "version",
        "username",
        "salutation",
        "firstName",
        "lastName",
        "email",
        "languageId",
        "roleIds"
    ]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "version": {
            "type": "integer"
        },
        "username": {
            "type": "string"
        },
        "externalId": {
            "type": ["string", "null"]
        },
        "samlSsoEnabled": {
            "type": "boolean"
        },
        "formAuthenticationEnabled": {
            "type": "boolean"
        },
        "salutation": {
            "enum": ["MR", "MS", "MX"]
        },
        "title": {
            "type": ["string", "null"]
        },
        "firstName": {
            "type": "string"
        },
        "lastName": {
            "type": "string"
        },
        "displayName": {
            "type": "string"
        },
        "email": {
            "type": "string"
        },
        "orgUnitId": {
            "type": "integer"
        },
        "languageId": {
            "type": "string"
        },
        "street": {
            "type": ["string", "null"]
        },
        "number": {
            "type": ["string", "null"]
        },
        "additionalAddress": {
            "type": ["string", "null"]
        },
        "zipCode": {
            "type": ["string", "null"]
        },
        "city": {
            "type": ["string", "null"]
        },
        "countryIsoA2": {
            "type": "string"
        },
        "timeZone": {
            "type": "string"
        },
        "telephone": {
            "type": ["string", "null"]
        },
        "mobile": {
            "type": ["string", "null"]
        },
        "companyId": {
            "type": ["string", "null"]
        },
        "signingAuthority": {
            "type": ["string", "null"]
        },
        "positionAuthority": {
            "type": ["string", "null"]
        },
        "division": {
            "type": ["string", "null"]
        },
        "dailyEmailNotification": {
            "type": "boolean"
        },
        "dailyEmailNotificationTypes": {
            "enum": [
                "NEW_APPLICATIONS",
                "OVERDUE_TASKS",
                "EXPIRING_JOB_PUBLICATION_PLACEMENTS",
                "EXPIRING_EXTERNAL_JOB_PUBLICATION_PLACEMENTS"
            ]
        },
        "notifyOnNewCandidateCommunication": {
            "type": "boolean"
        },
        "roleIds": {
            "description": "List of roles",
            "items": {
                "type": ["string"]
            },
            "type": "array"
        },
        "userGroupIds": {
            "description": "List of user group ids",
            "items": {
                "type": ["integer"]
            },
            "type": "array"
        },
        "dataForExternalSystems": {
            "description": "Fields and values are freely configurable in d.vinci application",
            "properties": {
                "field": {
                    "type": ["string"]
                },
                "value": {
                    "type": ["string"]
                }
            },
            "type": "array"
        }
    },
    "required": [
        "id",
        "version",
        "externalId",
        "username",
        "samlSsoEnabled",
        "formAuthenticationEnabled",
        "salutation",
        "title",
        "firstName",
        "lastName",
        "displayName",
        "email",
        "orgUnitId",
        "languageId",
        "street",
        "number",
        "additionalAddress",
        "zipCode",
        "city",
        "countryIsoA2",
        "timeZone",
        "telephone",
        "mobile",
        "companyId",
        "division",
        "dailyEmailNotification",
        "dailyEmailNotificationTypes",
        "notifyOnNewCandidateCommunication",
        "roleIds",
        "userGroupIds",
        "dataForExternalSystems"
    ]
}
```

### POST /dvinciUsers/{id}/delete

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        }
    },
    "required": ["success"]
}
```

## User groups

### GET /userGroups/

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": [
        {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "version": {
                    "type": "integer"
                },
                "externalId": {
                    "type": ["string", "null"]
                },
                "name": {
                    "type": "string"
                },
                "orgUnitId": {
                    "type": "integer"
                }
            },
            "userIds": {
                "description": "List of user ids",
                "items": {
                    "type": ["integer"]
                },
                "type": "array"
            },
            "required": ["id", "version", "name", "orgUnitId"]
        }
    ]
}
```

### POST /userGroups/

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "externalId": {
            "type": ["string", "null"]
        }
    },
    "name": {
        "type": "string"
    },
    "orgUnitId": {
        "type": ["integer"]
    },
    "userIds": {
        "description": "List of user ids",
        "items": {
            "type": "integer"
        },
        "type": "array"
    },
    "required": ["name", "orgUnitId"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "version": {
            "type": "integer"
        },
        "externalId": {
            "type": ["string", "null"]
        },
        "name": {
            "type": "string"
        },
        "orgUnitId": {
            "type": "integer"
        }
    },
    "userIds": {
        "description": "List of user ids",
        "items": {
            "type": "integer"
        },
        "type": "array"
    },
    "required": ["id", "version", "name", "orgUnitId"]
}
```

### GET /userGroups/{id}

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "version": {
            "type": "integer"
        },
        "externalId": {
            "type": ["string", "null"]
        },
        "name": {
            "type": "string"
        },
        "orgUnitId": {
            "type": "integer"
        }
    },
    "userIds": {
        "description": "List of user ids",
        "items": {
            "type": "integer"
        },
        "type": "array"
    },
    "required": ["id", "version", "name", "orgUnitId"]
}
```

### PUT /userGroups/{id}

#### Request

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": ["integer", "null"]
        },
        "version": {
            "type": "integer"
        },
        "externalId": {
            "type": ["string", "null"]
        },
        "name": {
            "type": "string"
        },
        "orgUnitId": {
            "type": ["integer", "null"]
        }
    },
    "userIds": {
        "description": "List of user ids",
        "items": {
            "type": ["integer"]
        },
        "type": "array"
    },
    "required": ["name", "version"]
}
```

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "version": {
            "type": "integer"
        },
        "externalId": {
            "type": ["string", "null"]
        },
        "name": {
            "type": "string"
        },
        "orgUnitId": {
            "type": "integer"
        }
    },
    "userIds": {
        "description": "List of user ids",
        "items": {
            "type": "integer"
        },
        "type": "array"
    },
    "required": ["id", "version", "name", "orgUnitId"]
}
```

### POST /userGroups/{id}/delete

#### Request

---

#### Response

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        }
    },
    "required": ["success"]
}
```
