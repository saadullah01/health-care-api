# Health Data Managing API
A multi-module health care application data management API to help a health center to manage their data.

## Users
* Medical Professionals (Nurses and Doctors)
* Patients
* Administrators
* Developers
> * Application Developers
> * Device Integrators
> * Machine Learning Scientists

## Branches
> **Note:** A branches will be merged to the `main` branch after all the tests for that branch have passed and all functionalities are completed.

There will be a separate branch for every module, as descibed below (the list will be updated as the project progresses):
* **db-management-module**
* **device-module**
* **chat-module**
* **speech-to-text-module**
* **user-module**

## 1) Database Module
### Database
We are using the **`database/health_care_DB.db`** ***sqlite3*** database for this project.
- **`database/db_management.py`**: creates a new database and all tables described in the schema
- **`database/db_populating.py`**: populates the database with dummy data to test basic functionalities

### Tables Schema
![Health Care DB](https://user-images.githubusercontent.com/61075964/163116862-93fdd7b0-7011-4ec6-bc9c-35ee6b19d6f2.png)

## 2) Devices Module
### Devices
The following devices will ask for the user to enter readings taken by these devices in specified units, otherwise it will give an **error** and keep asking them agian and again until the correct values are entered.

| ID | Type | Unit |
| :---: | :---: | :---: |
| 1 | Thermometer | Fahrenheit (F) |
| 2 | Weight Scale | Pounds (lbs) |
| 3 | Blood Pressure Monitor | milimeter mercury (mmHg) |
| 4 | Pulse Oximeter | beats per minute (BPM) |
| 5 | Oximeter | Oxygen Level in (SpO2) |
| 6 | Glucometer | (mmol/L) |
| 7 | Stadiometer | inches (in) |

### User Stories
For the above mentioned 7 devices a user can:
* Add data
* Get data

### Data Module
**`PUT` data:**
```py
request = {
  'request': 'PUT',
  'user_ID': _, # integer
  'device_ID': _, # integer
  'reading': _, # double
  'time': _, # datetime e.g. '%Y-%M-%D %H:%M:%S'
}

response = {
  success: _, # Boolean
  message: _ # Success or an error message
}
```
**`GET` data:**
```py
request = {
  'request': 'GET',
  'user_ID': _, # integer
}

response = {
  success: _, # Boolean
  message: _ # list of json objects or an error message
}
```

### How to Use
**PUT**
```
response = requests.put(URL + 'device', put_request)
```
**GET**
```
response = requests.get(URL + 'device', get_request)
```

## 3) Chat Module
### User Stories
A user can:
* Send text messages to other users
* Receive text messages from other users
* Send files (.txt/.wav/.mp4) to other users
* Receive files (.txt/.wav/.mp4) from other users
* Get conversation histories

### Message Types
| ID | Type |
| :---: | :---: |
| 1 | text message |
| 2 | .txt file |
| 3 | .wav file |
| 4 | .mp4 file |

### Data Module
**`Request` format to `PUT` data:**
```py
put_request = {
  'sender_ID': _, # integer
  'receiver_ID': _, # integer
  'conversation_ID': # integer
  'message_type': _, # integer (ID)
  'message': _, # text or path to .txt/.wav/.mp4 file depending on message type
  'time': _, # datetime e.g. '%Y-%M-%D %H:%M:%S'
}
```
**`Request` format to `GET` data:**
```py
get_request = {
  'conversation_ID': _, # integer
}
```
**`Response` Format:**
```
response = {
  success: _, # Boolean
  message: _ # Message includes success/error/data depending on the request
}
```

### How to Use
**PUT**
```
response = requests.put(URL + 'chat', put_request)
```
**GET**
```
response = requests.get(URL + 'chat', get_request)
```

## 4) Speech-to-Text Module
For this module, first run the following command in your terminal (if you are using Linux):
```
lscpu | egrep 'Model name|Socket|Thread|NUMA|CPU\(s\)'
```
It will tell you the `number of CPU cores` you have and the `number of threads` you can run per core. By this you can get the number of threads you can run at a time.
> **For example:** my system has 8 cores and one core can handle 2 threads at a time so the number of API calls it can handle at a time, considering one API call per thread, is 16.
### How to Use
```
python3 s2t.py <arguments>
```
**arguments**
* -h / --help
* -c / --cores <number_of_cores>
* -t / --threads <threads_per_core>
* -n / --num <number_of_API_requests>

**Example**
```
python3 speech2text/s2t.py -c 8 -t 2 -n 50
```
The tracking interface for this program will display the working of threads when in progress and done.

## 5) User Module
### User Stories
- GET user data by *email*
- ADD user to the database (check for existence of same user before through *email*)
- DELETE user
- GET PATIENTS for a user (i.e. medical professional)
- GET MEDICAL PROFESSIONALS for a user (i.e. patient)

### Data Module
**`GET` user data:**
```py
request = {
    'request': 'GET',
    'email': _ # string
}

response = {
  success: _, # boolean
  message: _ # json object for user data OR error message
}
```
**`ADD` user data:**
```py
request = {
    'request': 'ADD',
    'first_name': _, # string
    'last_name': _, # string
    'gender': _, # string
    'contact_no': _, # string
    'role_ID': _, # int
    'dob': _, # string date-time format
    'email': _, # string
    'address': _, # string
    'billing': _, # string
    'allergies': _, # string
    'medical_ID': _, # string
    'family': _, # string
    'medical_history': _, # string
    'medical_condition': _, # string
    'emergency_contact': _, # string
}

response = {
  success: _, # boolean
  message: _ # success message OR error message
}
```
**`DELETE` user data:**
```py
request = {
    'request': 'DELETE',
    'email': _ # string
}

response = {
  success: _, # boolean
  message: _ # success message OR error message
}
```
**`GET PATIENTS` data for a medical professional:**
```py
request = {
    'request': 'GET_P',
    'mp_ID': _ # int
}

response = {
  success: _, # boolean
  message: _ # list of json objects of user data OR error message
}
```
**`GET MEDICAL PROFESSIONALS` data for a patient:**
```py
request = {
    'request': 'GET_MP',
    'p_ID': _ # int
}

response = {
  success: _, # boolean
  message: _ # list of json objects of user data OR error message
}
```
