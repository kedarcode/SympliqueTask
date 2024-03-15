This document outlines the implementation of API endpoints for the Remind-me-later project using Django, a high-level Python web framework. These endpoints facilitate user registration, authentication, setting reminders, and retrieving reminders.

**API Endpoints**
**User Registration**

**Description**:
Registers a new user with the Remind-me-later service.

Endpoint: POST /symplique/auth/users/

Request Body:

{
    "email": "testkedar@gmail.com",
    "name": "kedar",
    "password": "kedartest",
    "first_name": "Kedar",
    "last_name": "Shelar",
    "re_password": "kedartest",
    "username": "kedar"
}
Response: HTTP 201 Created on success

**Activate User**

**Description**:
Activates the user account by confirming the email address.

Endpoint: POST /symplique/auth/users/activate/

Request Body:

{
    "uid": "NjA",
    "token": "bqzh1r-39c5b530ddd400c42ff0bfe1a4fa2e65"
}
Response: HTTP 200 OK on success

**User Login**

**Description**:
Logs in the user and generates a JWT token for authentication.

Endpoint: POST /symplique/users/login/

Request Body:

{
    "email": "testkedar@gmail.com",
    "password": "kedartest"
}
Response:
{
    "access_token": "<generated_access_token>"
}

**Set Reminder**

Endpoint: POST /symplique/setreminder/

**Description**:
Creates a new reminder for the user to be sent at a specified time.

Request Body:

{
    "channel": "SMS",
    "message": "Do Something",
    "notifyon": "2024-03-07 05:21:00",
    "timezone": "Asia/Kolkata"
}
Headers:

Authorization: Bearer <generated_access_token>

Response: HTTP 201 Created on success

**Get Reminders**

**Description**:
Retrieves all reminders set by the user.

Endpoint: GET /symplique/setreminder/

Headers:

Authorization: Bearer <generated_access_token>

Response:

[
    {
        "id": 1,
        "channel": "SMS",
        "message": "Do Something",
        "notifyon": "2024-03-07 05:21:00",
        "timezone": "Asia/Kolkata"
    },
    {
        "id": 2,
        "channel": "EMAIL",
        "message": "Another Reminder",
        "notifyon": "2024-03-08 08:00:00",
        "timezone": "Asia/Kolkata"
    }
]
