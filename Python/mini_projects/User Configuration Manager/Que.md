## Description
 
build a User Configuration Manager that allows users to manage their settings such as theme, language, and notifications. You will implement functions to add, update, delete, and view user settings.

**Objective:** Fulfill the user stories below and get all the tests to pass to complete the lab.

### User Stories:

1. You should define a function named add_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair

2. **add_setting function should:**

- Convert the key and value to lowercase.
- If the key setting exists, return Setting '[key]' already exists! Cannot add a new setting with this name.
- If the key setting doesn't exist, add the key-value pair to the given dictionary of settings and return Setting '[key]' added with value '[value]' successfully!.
- The messages returned should have the key and value in lowercase.

3. You should define a function named update_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair.

4. **update_setting function should:**

- Convert the key and value to lowercase.
- If the key setting exists, update its value in the given dictionary of settings and return: Setting '[key]' updated to '[value]' successfully!
- If the key setting doesn't exist, return Setting '[key]' does not exist! Cannot update a non-existing setting.
- The messages returned should have the key and value in lowercase.

5. You should define a function named delete_setting with two parameters representing a dictionary of settings and a key.

6. **delete_setting function should:**

- Convert the key passed to lowercase.
- If the key setting exists, remove the key-value pair from the given dictionary of settings and return Setting '[key]' deleted successfully!
- If the key setting does not exist, return Setting not found!
- The messages returned should have the key in lowercase.

7. You should define a function named view_settings with one parameter representing a dictionary of settings.

8. **view_settings function should:**

- Return No settings available. if the given dictionary of settings is empty.
- If the dictionary contains any settings, return a string displaying the settings. The string should start with Current User Settings: followed by the key-value pairs, each on a new line and with the key capitalized. For example, view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}) should return:
```
Current User Settings:
Theme: dark
Notifications: enabled
Volume: high
```

9. For testing the code, you should create a dictionary named test_settings to store some user configuration preferences.

### Tests:

- 1. You should create a dictionary named test_settings and add some values to it.
- 2. You should define a function named add_setting.
- 3. The add_setting function should have two parameters.
- 4. add_setting should convert the key to lowercase.
- 5. add_setting should convert the value to lowercase.
- 6. add_setting({'theme': 'light'}, ('THEME', 'dark')) should return the error message Setting 'theme' already exists! Cannot add a new setting with this name..
- 7. add_setting({'theme': 'light'}, ('volume', 'high')) should add a new key-value pair and return the success message Setting 'volume' added with value 'high' successfully!.
-  8. add_setting should correctly add the given key-value pair to the dictionary.
- 9. You should define a function named update_setting.
- 10. The update_setting function should have two parameters.
- 11. The update_setting function should convert key to lowercase.
- 12. The update_setting function should convert value to lowercase.
- 13. update_setting({'theme': 'light'}, ('theme', 'dark')) should update an existing key and return the success message Setting 'theme' updated to 'dark' successfully!.
- 14. update_setting({'theme': 'light'}, ('volume', 'high')) should return the error message Setting 'volume' does not exist! Cannot update a non-existing setting. when the key doesn't exist.
- 15. update_setting should correctly update the given key-value pair in the dictionary.
- 16. You should define a function named delete_setting.
- 17. The delete_setting function should have two parameters.
- 18. delete_setting should convert the key to lowercase.
- 19. delete_setting({'theme': 'light'}, 'theme') should remove the existing key and return the success message Setting 'theme' deleted successfully!.
- 20. delete_setting should return the error message Setting not found! when the key doesn't exist.
- 21. delete_setting should correctly remove the given key from the dictionary.
- 22. You should define a function named view_settings.
- 23. The view_settings function should have one parameter.
- 24. view_settings should return the message No settings available. if the given dictionary is empty.
- 25. view_settings should return formatted settings for non-empty dictionary.
- 26. view_settings should capitalize the first letter of each setting name.
- 27. view_settings should display the correct results and end with a newline character.