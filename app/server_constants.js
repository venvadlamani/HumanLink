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
            "description": "Companionship",
            "skills": "All things companions do"
        },
        {
            "value": 1,
            "name": "Grooming",
            "description": "Personal Grooming",
            "skills": "Bathing and dressing"
        },
        {
            "value": 2,
            "name": "Meals",
            "description": "Meal Preparations",
            "skills": "Hot/cold meal preparations"
        },
        {
            "value": 3,
            "name": "Housekeeping",
            "description": "Housekeeping",
            "skills": "Housekeeping - Laundry and cleaning"
        },
        {
            "value": 4,
            "name": "Medication",
            "description": "Medication reminders",
            "skills": "Medication reminders"
        },
        {
            "value": 5,
            "name": "Transportation",
            "description": "Transportation",
            "skills": "Transportation from home to clinic and back"
        },
        {
            "value": 6,
            "name": "Alzheimers",
            "description": "Alzheimer's and Dementia",
            "skills": "Companionship, Mental simulation, 24-hour care"
        },
        {
            "value": 7,
            "name": "Mobility",
            "description": "Mobility assistance",
            "skills": "Mobility assistance"
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
