# health-care-app
A multi-module health care application to help a health center to manage their data.

## Devices
The following devices will ask for the user to enter readings taken by these devices in specified units, otherwise it will give an **error** and keep asking them agian and again until the correct values are entered.
* **Thermometer:** fahrenheit (F)
* **Weight Scale:** pounds (lbs)
* **Blood Pressure Monitor:** milimeter mercury (mmHg)
* **Pulse Oximeter**: beats per minute (BPM)
* **Oximeter:** Oxygen Level in (SpO2)
* **Glucometer:** (mmol/L)
* **Stadiometer:** inches (in)

## Tables Schema
### Phase 1
![Untitled](https://user-images.githubusercontent.com/61075964/153734581-decc5e81-26cc-45ea-bb3c-d0f55204e1f6.png)

## How To Run
```
python3 app.py
```
When you run it, it will ask you to enter the user ID and choose a device to take the reading. When the device is chossen it displays that device interface for you to enter the reading and then it will insert that to the database.

## Branches

> **Note:** A branches will be merged to the `main` branch after all the tests for that branch have passed and all functionalities are completed.

There will be a separate branch for every module, as descibed below (the list will be updated as the project progresses):
* **db-management-module**
* **device-module**
