# car-maintenance-tracker
Vehicle Maintenance Reminder Program
This program helps track vehicle maintenance by using the current mileage of a vehicle and referencing a JSON-based maintenance log. It identifies any maintenance tasks that are due or overdue and sends an email notification if necessary.

How It Works
Initialization
Upon execution, the main script defines a dictionary containing the recommended mileage intervals for various maintenance tasks (e.g., oil changes, tire rotations, etc.).

Maintenance Log Reference
The program reads a Matience_Logs_JSONS\2017_Toyota_Corolla_MLog.json file, which stores the last recorded mileage at which each maintenance task was completed.

Note: Make sure to update this JSON file each time maintenance is performed.

User Input
The user is prompted to enter the current mileage of their vehicle.

Maintenance Check
The script compares the current mileage against the last recorded mileage for each maintenance task. If the difference exceeds the recommended interval, that task is flagged as overdue.

Notification
Any overdue tasks are compiled into a list, and an email is sent to the address specified in the .env file with a summary of the required maintenance.


