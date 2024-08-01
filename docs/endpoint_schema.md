# Endpoint Schemas

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

````json
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
                "ONLINE

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
````

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

#### Response

### PUT /configuration/{type}/externalLinks

#### Request

#### Response

## Hiring requests

### GET /hiringRequests/

#### Request

#### Response

### POST /hiringRequests/

#### Request

#### Response

### GET /hiringRequests/?externalId={externalId}

#### Request

#### Response

### GET /hiringRequests/{id}

#### Request

#### Response

### PUT /hiringRequests/{id}

#### Request

#### Response

### GET /hiringRequests/{id}/history

#### Request

#### Response

### GET /hiringRequests/{id}/approvers

#### Request

#### Response

## Job openings

### GET /jobOpenings/

#### Request

#### Response

### POST /jobOpenings/

#### Request

#### Response

### GET /jobOpenings/?externalId={externalId}

#### Request

#### Response

### GET /jobOpenings/{id}

#### Request

#### Response

### PUT /jobOpenings/{id}

#### Request

#### Response

### GET /jobOpenings/{id}/history

#### Request

#### Response

### PUT /jobOpenings/{id}/history

#### Request

#### Response

### PUT /jobOpenings/{id}/history/{externalId}

#### Request

#### Response

## Job publications

### GET /jobPublications/

#### Request

#### Response

### POST /jobPublications/

#### Request

#### Response

### GET /jobPublications/?externalId={externalId}

#### Request

#### Response

### GET /jobPublications/{id}

#### Request

#### Response

### PUT /jobPublications/{id}

#### Request

#### Response

### POST /jobPublications/{id}/delete

#### Request

#### Response

## Job publication placements

### GET /jobPublicationPlacements/{partner_id}/placements

#### Request

#### Response

### POST /jobPublicationPlacements/{partner_id}/placements

#### Request

#### Response

### GET /jobPublicationPlacements/{partner_id}/placements/?externalId={externalId}

#### Request

#### Response

### GET /jobPublicationPlacements/{partner_id}/placements/?jobPublicationId={jobPublicationId}

#### Request

#### Response

### GET /jobPublicationPlacements/{partner_id}/placements/{id}

#### Request

#### Response

### PUT /jobPublicationPlacements/{partner_id}/placements/{id}

#### Request

#### Response

### POST /jobPublicationPlacements/{partner_id}/placements/{id}/delete

#### Request

#### Response

## Job publication channels

### GET /jobPublicationChannels/{id}

#### Request

#### Response

### PUT /jobPublicationChannels/{id}

#### Request

#### Response

## Locations

### GET /locations/

#### Request

#### Response

### POST /locations/

#### Request

#### Response

### GET /locations/{id}

#### Request

#### Response

### PUT /locations/{id}

#### Request

#### Response

### POST /locations/{id}/delete

#### Request

#### Response

## Onboardings

### GET /onboardings/

#### Request

#### Response

### GET /onboardings/{id}

#### Request

#### Response

### GET /onboardings/{id}/attachments

#### Request

#### Response

### GET /onboardings/{id}/attachments/{attachmentId}

#### Request

#### Response

### GET /onboardings/{id}/attachments/{attachmentId}/pdf

#### Request

#### Response

### POST /onboardings/{id}/delete

#### Request

#### Response

## Organisation units

### GET /orgUnits/

#### Request

#### Response

### GET /orgUnits/{id}

#### Request

#### Response

## Persons

### GET /persons/

#### Request

#### Response

### POST /persons/

#### Request

#### Response

### GET /persons/?externalId={externalId}

#### Request

#### Response

### GET /persons/{id}

#### Request

#### Response

### PUT /persons/{id}

#### Request

#### Response

### POST /persons/{id}/delete

#### Request

#### Response

### GET /persons/{id}/photo

#### Request

#### Response

### POST /persons/{id}/photo

#### Request

#### Response

### POST /persons/{id}/photo/delete

#### Request

#### Response

## Users

### GET /dvinciUsers/

#### Request

#### Response

### POST /dvinciUsers/

#### Request

#### Response

### GET /dvinciUsers/{id}

#### Request

#### Response

### PUT /dvinciUsers/{id}

#### Request

#### Response

### POST /dvinciUsers/{id}/delete

#### Request

#### Response

## User groups

### GET /userGroups/

#### Request

#### Response

### POST /userGroups/

#### Request

#### Response

### GET /userGroups/{id}

#### Request

#### Response

### PUT /userGroups/{id}

#### Request

#### Response

### POST /userGroups/{id}/delete

#### Request

#### Response
