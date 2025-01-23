# Contact Book Application  
A simple Python application to manage contacts. Add, edit, delete, and search contacts with a user-friendly interface.

## Features  
- Add, edit, and delete contacts  
- Search contacts with fuzzy matching  
- Data persistence using a CSV file, ensuring contacts are saved and reloaded upon restarting the application

## Requirements  
- Python 3.x  
- [RapidFuzz](https://pypi.org/project/rapidfuzz/) (for fuzzy matching)  

To install the required library, run:  
```bash  
pip install rapidfuzz  
```

## How to Run  
1. Clone or download this repository.  
2. Make sure you have Python 3.x installed.  
3. Install the required library using the command above.  
4. Run the application by executing:  
```bash  
python main.py  
```

## How It Works  
1. On startup, the application loads contacts from a CSV file (`contact_list.csv`). If the file doesn’t exist, it will be created automatically.  
2. You can perform the following actions:  
   - Add a new contact by entering the first name, last name, and phone number.  
   - Edit an existing contact by searching for it and updating its details.  
   - Delete a contact by searching for it and confirming the deletion.  
   - Search for contacts using fuzzy matching, which allows for partial matches or handling of typos.  
3. All changes are saved back to the CSV file automatically.  

## File Structure  
```plaintext  
project-folder/  
├── main.py          # Main application logic  
├── contact.py       # Contact class definition  
├── contact_list.csv # Stores contact information  
```

## Future Enhancements / Challenges  
Here are some ideas to extend the functionality of this project:  

1. **Sort Contacts:**  
   Add a feature to sort contacts alphabetically by first name, last name, or other fields.  

2. **Import/Export Contacts:**  
   Implement functionality to import contacts from or export contacts to other file formats, such as JSON or XML.  

3. **Validation:**  
   Ensure that user inputs are valid, such as enforcing a proper phone number format or email validation.  

4. **Group Contacts:**  
   Allow users to group contacts into categories, such as "Work," "Family," or "Friends," for better organization.  

5. **Backups:**  
   Add a backup feature to save a copy of the CSV file in case of accidental deletions or file corruption.  

6. **GUI:**  
   Build a graphical user interface (GUI) using libraries like `Tkinter`, `PyQt`, or `Kivy` for a more user-friendly experience.  

7. **Search Enhancements:**  
   Improve the fuzzy search to prioritize more relevant results or allow searching by phone number or email address.  

8. **Contact Logs:**  
   Add a feature to track changes made to contacts, such as edits or deletions, with timestamps for auditing purposes.  

9. **Birthday Notifications:**  
   Allow users to add birthdays to contacts and receive reminders for upcoming birthdays.  

10. **Cloud Sync:**  
    Implement a feature to sync contacts with cloud storage solutions like Google Drive, Dropbox, or OneDrive.  

11. **Encrypt Data:**  
    Add encryption for sensitive data in the CSV file to protect user information.  

12. **REST API:**  
    Develop a RESTful API to interact with the contact book, making it accessible to other applications or services.  
