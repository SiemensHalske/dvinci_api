# Parameters of the different endpoints

## Applications

-   /applications/ (GET)
    -   Query Parameters
        -   byJobOpeningId: (number)
            -   Filter list by given job opening id.
        -   byJobOpeningExternalId: (string)
            -   Filter list by given job opening externalId.
        -   byApplicationStatusId: (string)
            -   Filter list by given application status internal-name.
        -   byOrgUnitId: (number)
            -   Filter list by given organisation unit id.
        -   byDateCreatedFrom: (date)
            -   Filter list by given creation date of application (from).
        -   byDateCreatedTo: (date)
            -   Filter list by given creation date of application (to).
        -   byLastStatusChangeDateFrom: (date)
            -   Filter list by given last status change date of application (from).
        -   byLastStatusChangeDateTo: (date)
            -   Filter list by given last status change date of application (to).
-   /applications/?externalId={externalId} (GET)
    -   URI Parameters
        -   externalId: required (string)
            -   externalId of the requested application
-   /applications/{id} (GET)
    -   URI Parameters
        -   id: required (number)
            -   id of the requested application
-   /applications/{id} (PUT)
    -   URI Parameters
        -   id: required (number)
            -   id of the requested application
-   /applications/{id}/delete (POST)
    -   URI Parameters
        -   id: required (number)
            -   id of the requested application
-   /applications/{id}/statusChange/{statusId} (POST)
    -   URI Parameters
        -   id: required (number)
            -   id of the requested application
        -   statusId: required (number)
            -   id of the target application status.
-   /applications/{id}/jobOpeningMove/{jobOpeningId} (POST)
    -   URI Parameters
        -   id: required (number)
            -   id of the application to change job opening for.
        -   jobOpeningId: required (number)
            -   id of the target job opening.
-   /applications/{id}/attachments (GET)
    -   URI Parameters
        -   id: required (number)
            -   id of the requested application
-   /applications/{id}/attachments (POST)
    -   URI Parameters
        -   id: required (number)
            -   id of the requested application
-   /applications/{id}/attachments/{attachmentId} (GET)
    -   URI Parameters
        -   id: required (number)
            -   id of the requested application
        -   attachmentId: required (number)
            -   id of the requested attachment
-   /applications/{id}/attachments/{attachmentId}/pdf (GET)
    -   URI Parameters
        -   id: required (number)
            -   id of the requested application
        -   attachmentId: required (number)
            -   id of the requested attachment
-   /applications/{id}/history (GET)
    -   URI Parameters
        -   id: required (number)
            -   id of the requested application
-   /applications/{id}/history (PUT)
    -   URI Parameters
        -   id: required (number)
            -   id of the requested application
-   /applications/{id}/history/{externalId} (PUT)
    -   URI Parameters
        -   id: required (number)
            -   id of the requested application
        -   externalId: required (string)
            -   external id of the history entry to create or update

## Configuration

-   /configuration/{type}/externalLinks (GET)
    -   URI Parameters
        -   type: required (string)
            -   type of requested external links. Currently available types: "applications", "jobPublications".
-   /configuration/{type}/externalLinks (PUT)
    -   URI Parameters
        -   type: required (string)
            -   type of requested external links. Currently available types: "applications", "jobPublications".

## Hiring Requests

-   /hiringRequests/ (GET)
    -   Query Parameters
        -   byDateCreatedFrom: (date)
            -   Filter list by given creation date of hiring request (from).
        -   byDateCreatedTo: (date)
            -   Filter list by given creation date of hiring request (to).
-   /hiringRequests/?externalId={externalId} (GET)
    -   URI Parameters
        -   externalId: required (string)
-   /hiringRequests/{id} (GET)
    -   URI Parameters
        -   id: required (number)
-   /hiringRequests/{id} (PUT)
    -   URI Parameters
        -   id: required (number)
-   /hiringRequests/{id}/history (GET)
    -   URI Parameters
        -   id: required (number)
-   /hiringRequests/{id}/approvers (GET)
    -   URI Parameters
        -   id: required (number)

## Job Openings

-   /jobOpenings/ (GET)
    -   Query Parameters
        -   byDateCreatedFrom: (date)
        -   byDateCreatedTo: (date)
-   /jobOpenings/?externalId={externalId} (GET)
    -   URI Parameters
        -   externalId: required (string)
-   /jobOpenings/{id} (GET)
    -   URI Parameters
        -   id: required (number)
-   /jobOpenings/{id} (PUT)
    -   URI Parameters
        -   id: required (number)
-   /jobOpenings/{id}/history (GET)
    -   URI Parameters
        -   id: required (number)
-   /jobOpenings/{id}/history (PUT)
    -   URI Parameters
        -   id: required (number)
-   /jobOpenings/{id}/history/{externalId} (PUT)
    -   URI Parameters
        -   id: required (number)
        -   externalId: required (string)

## Job Publications

-   /jobPublications/?externalId={externalId} (GET)
    -   URI Parameters
        -   externalId: required (string)
-   /jobPublications/{id} (GET)
    -   URI Parameters
        -   id: required (number)
-   /jobPublications/{id} (PUT)
    -   URI Parameters
        -   id: required (number)
-   /jobPublications/{id}/delete (POST)
    -   URI Parameters
        -   id: required (number)

## Job Publication Channels

-   /jobPublicationChannels/{id} (GET)
    -   URI Parameters
        -   id: required (string)
-   /jobPublicationChannels/{id} (PUT)
    -   URI Parameters
        -   id: required (string)

## Job Publication

-   /jobPublicationPlacements/{partner_id}/placements (GET)
    -   URI Parameters
        -   partner_id: required (string)
            -   Alphanumeric string [a-zA-Z0-9] with 3 - 15 characters
-   /jobPublicationPlacements/{partner_id}/placements (POST)
    -   URI Parameters
        -   partner_id: required (string)
            -   Alphanumeric string [a-zA-Z0-9] with 3 - 15 characters
-   /jobPublicationPlacements/{partner_id}/placements/?externalId={externalId} (GET)
    -   URI Parameters
        -   partner_id: required (string)
            -   Alphanumeric string [a-zA-Z0-9] with 3 - 15 characters
        -   externalId: required (string)
-   /jobPublicationPlacements/{partner_id}/placements/?jobPublicationId={jobPublicationId} (GET)
    -   URI Parameters
        -   partner_id: required (string)
            -   Alphanumeric string [a-zA-Z0-9] with 3 - 15 characters
        -   jobPublicationId: required (number)
-   /jobPublicationPlacements/{partner_id}/placements/{id} (GET)
    -   URI Parameters
        -   partner_id: required (string)
            -   Alphanumeric string [a-zA-Z0-9] with 3 - 15 characters
        -   id: required (number)
-   /jobPublicationPlacements/{partner_id}/placements/{id} (PUT)
    -   URI Parameters
        -   partner_id: required (string)
            -   Alphanumeric string [a-zA-Z0-9] with 3 - 15 characters
        -   id: required (number)
-   /jobPublicationPlacements/{partner_id}/placements/{id}/delete (POST)
    -   URI Parameters
        -   partner_id: required (string)
            -   Alphanumeric string [a-zA-Z0-9] with 3 - 15 characters
        -   id: required (number)

## Locations

-   /locations/ (GET)
    -   Query Parameters
        -   forJobOpeningByOrgUnitId: (number)
            -   Filter list of locations that can be assigned to job openings of the given organisation unit.
-   /locations/{id} (GET)
    -   URI Parameters
        -   id: required (string)
-   /locations/{id} (PUT)
    -   URI Parameters
        -   id: required (string)
-   /locations/{id}/delete (POST)
    -   URI Parameters
        -   id: required (string)

## Onboardings

-   /onboardings/ (GET)
    -   Query Parameters
        -   status: (one of ACTIVE, FINISHED)
            -   Filter onboardings by state
        -   orgUnitId: (integer)
            -   Filter onboardings by corresponding organization unit
        -   applicationId: (integer)
            -   Filter onboardings by corresponding application paper
        -   fromDateOfStart: (string)
            -   ISO8601 date format (e.g. 2020-08-20), filter onboardings greater than equal entered date
        -   fromDateOfContract: (string)
            -   ISO8601 date format (e.g. 2020-08-20), filter onboardings greater than equal entered date
        -   fromDateOfEmployment: (string)
            -   ISO8601 date format (e.g. 2020-08-20), filter onboardings greater than equal entered date
        -   fromDateOfEnd: (string)
            -   ISO8601 date format (e.g. 2020-08-20), filter onboardings greater than equal entered date
        -   fromDateCreated: (string)
            -   ISO8601 date-time format (e.g. 2020-08-20T07:45:00Z), filter onboardings greater than equal entered date-time
-   /onboardings/{id} (GET)
    -   URI Parameters
        -   id: required (number)
            -   id of the requested onboarding
-   /onboardings/{id}/attachments (GET)
    -   URI Parameters
        -   id: required (number)
            -   id of the requested onboarding
-   /onboardings/{id}/attachments/{attachmentId} (GET)
    -   URI Parameters
        -   id: required (number)
            -   id of the requested onboarding
        -   attachmentId: required (string)
            -   id of the requested attachment
-   /onboardings/{id}/attachments/{attachmentId}/pdf (GET)
    -   URI Parameters
        -   id: required (number)
            -   id of the requested onboarding
        -   attachmentId: required (string)
            -   id of the requested attachment
-   /onboardings/{id}/delete (POST)
    -   URI Parameters
        -   id: required (number)
            -   id of the requested onboarding

## Organisation Units

-   /orgUnits/{id} (GET)
    -   URI Parameters
        -   id: required (number)
            -   id of the requested organisation unit

## Persons

-   /persons/?externalId={externalId} (GET)
    -   URI Parameters
        -   externalId: required (string)
-   /persons/{id} (GET)
    -   URI Parameters
        -   id: required (number)
-   /persons/{id} (PUT)
    -   URI Parameters
        -   id: required (number)
-   /persons/{id}/delete (POST)
    -   URI Parameters
        -   id: required (number)
-   /persons/{id}/photo (GET)
    -   URI Parameters
        -   id: required (number)
-   /persons/{id}/photo (POST)
    -   URI Parameters
        -   id: required (number)
-   /persons/{id}/photo/delete (POST)
    -   URI Parameters
        -   id: required (number)

## Users

-   /users/ (GET)

    -   Query Parameters

        -   lang: (string)
        -   Use given locale for Translations. If not defined the locale/language of the api user is used. Supported fields: displayName Returns HTTP Status Error 422, if passed locale is not supported.
            Example:
            -   en
            -   de_DE
        -   externalId: (string)
            Filter list by given dvinci user externalId.
        -   forJobOpeningByOrgUnitId: (number)
            Filter list by users that can be selected as responsible users for job openings of the given organisation unit.

-   /users/{id} (GET)
    -   URI Parameters
        -   id: required (number)
-   /users/{id} (PUT)
    -   URI Parameters
        -   id: required (number)
-   /users/{id}/delete (POST)
    -   URI Parameters
        -   id: required (number)

## User Groups

-   /userGroups/ (GET)
    -   URI Parameters
        -   forJobOpeningByOrgUnitId: (number)
            -   Filter list to user groups that can be assigned to job openings of the given organisation unit.
        -   externalId: (string)
            -   Filter list by given user group externalId.
-   /userGroups/{id} (GET)
    -   URI Parameters
        -   id: required (number)
-   /userGroups/{id} (PUT)
    -   URI Parameters
        -   id: required (number)
-   /userGroups/{id}/delete (POST)
    -   URI Parameters
        -   id: required (number)
