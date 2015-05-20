'use strict';

window.HL = window.HL || {};

/**
 * Constants and enums that are shared between the server and the client.
 * These should eventually be auto-generated.
 */
(function (obj) {
    var accountTypes = [
        { "value": 0, "name": "Caregiver" },
        { "value": 1, "name": "Careseeker" },
        { "value": 2, "name": "Business or Organization" }
    ];
    var states = [
        { "value": 0, "name": "AL", "description": "Alabama" },
        { "value": 1, "name": "AK", "description": "Alaska" },
        { "value": 2, "name": "AR", "description": "Arkansas" },
        { "value": 3, "name": "AZ", "description": "Arizona" },
    ];
    var languages = [
        { "value": 0, "name": "English" },
        { "value": 1, "name": "Arabic" },
        { "value": 2, "name": "French" },
        { "value": 3, "name":  "Gujarati" },
    ];
    var careServices = [
        {
            "value": 0,
            "name": "Companion",
            "description": "Companion",
            "skills": "Errands, Housekeeping, Transportation"
        },
        {
            "value": 1,
            "name": "Personal",
            "description": "Personal",
            "skills": "Bathing and dressing, Exercise and Mobility, Medication reminders"
        },
        {
            "value": 2,
            "name": "AlzheimerDimentia",
            "description": "Alzheimer's and Dimentia",
            "skills": "Companionship, Mental simulation, 24-hour care"
        }
    ];
    var allergies = [
        { "value": 0, "name": "Cats" },
        { "value": 1, "name": "Dogs" },
        { "value": 2, "name": "Smoking" }
    ];
    var transportation = [
        {
            "value": 0,
            "name": "CanProvide",
            "description": "I can provide a transportation for the patient"
        },
        {
            "value": 1,
            "name": "CanDrive",
            "description": "I can drive the patient's car"
        },
        {
            "value": 2,
            "name": "NotDrive",
            "description": "I prefer not to drive"
        }
    ];
    var expertise = [
        {
            "value": 0,
            "name": "ALS",
            "description": "ALS"
        },
        {
            "value": 1,
            "name": "AlzheimersDisease",
            "description": "Alzheimer's Disease"
        },
        {
            "value": 2,
            "name": "BloodDisorders",
            "description": "Blood Disorders"
        },
        {
            "value": 3,
            "name": "Cancer",
            "description": "Cancer"
        }
    ];

    obj.constants = {
        accountTypes: accountTypes,
        states: states,
        languages: languages,
        careServices: careServices,
        allergies: allergies,
        transportation: transportation,
        expertise: expertise
    };
}(window.HL));
