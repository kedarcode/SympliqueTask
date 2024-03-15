This document outlines the implementation of API endpoints for the Remind-me-later project using Django, a high-level Python web framework. These endpoints facilitate user registration, authentication, setting reminders, and retrieving reminders.

**API Endpoints
****User Registration**
Endpoint: POST /symplique/auth/users/

Request Body:
{
    "email": "kedaranimate@gmail.com",
    "name": "kedar",
    "password": "kedar232323",
    "first_name": "Kedar",
    "last_name": "Shelar",
    "re_password": "kedar232323",
    "username": "kedar"
}
Response: HTTP 201 Created on success

**Activate User
**Endpoint: POST /symplique/auth/users/activate/

Request Body:
{
    "uid": "NjA",
    "token": "bqzh1r-39c5b530ddd400c42ff0bfe1a4fa2e65"
}
Response: HTTP 200 OK on success

**User Login
**Endpoint: POST /symplique/users/login/

Request Body:
{
    "email": "kedaranimate@gmail.com",
    "password": "kedar232323"
}
Response:
{
    "access_token": "<generated_access_token>"
}

**Set Reminder
**Endpoint: POST /symplique/setreminder/

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

**Get Reminders
**Endpoint: GET /symplique/setreminder/

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
