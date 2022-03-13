# health-care-app
A multi-module health care application to help a health center to manage their data.

## Devices Module
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

### Data Module
**`Request` format to `PUT` data:**
```py
request = {
  'user_ID': _, # integer
  'device_ID': _, # integer
  'reading': _, # double
  'time': _, # datetime e.g. '%Y-%M-%D %H:%M:%S'
}
```
**`Request` format to `GET` data:**
```py
request = {
  'user_ID': _, # integer
  'device_ID': _, # integer
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
```terminal
curl https://health-care-api.herokuapp.com/device-module -X PUT -d '{"user_ID":1,"device_ID":1,"reading":99,"time":"2022-02-15 12:30:00"}' -H 'CONTENT-TYPE: application/json'
```

## Chat Module
### Chat Types

| ID | Type | File Format |
| :---: | :---: | :---: |
| 1 | Text | .txt |
| 2 | Audio | .wav |
| 3 | Video | .mp4 |

### Data Module
**`Request` format to `PUT` data:**
```py
request = {
  'sender_ID': _, # integer
  'receiver_ID': _, # integer
  'message_type': _, # integer
  'message': _, # path to .txt/.wav/.mp4 file depending on message type
  'time': _, # datetime e.g. '%Y-%M-%D %H:%M:%S'
}
```
**`Request` format to `GET` data:**
```py
request = {
  'sender_ID': _, # integer
  'receiver_ID': _, # integer
}
```
**`Response` Format:**
```
response = {
  success: _, # Boolean
  message: _ # Message includes success/error/data depending on the request
}
```

## Tables Schema
### Phase 1
![Untitled](https://user-images.githubusercontent.com/61075964/153734581-decc5e81-26cc-45ea-bb3c-d0f55204e1f6.png)

### Phase 2


## Branches

> **Note:** A branches will be merged to the `main` branch after all the tests for that branch have passed and all functionalities are completed.

There will be a separate branch for every module, as descibed below (the list will be updated as the project progresses):
* **db-management-module**
* **device-module**
* **chat-module**
