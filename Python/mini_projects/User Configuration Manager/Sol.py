def add_setting(settings: dict[str, str], new_setting: tuple[str, str]) -> str:
    
    key = new_setting[0].lower()
    value = new_setting[1].lower()
    
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings: dict[str, str], new_setting: tuple[str, str]) -> str:
    key = new_setting[0].lower()
    value = new_setting[1].lower()
    
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings: dict[str, str], key_to_delete: str) -> str:
    key = key_to_delete.lower()
    
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(settings: dict[str, str]) -> str:
    if not settings:
        return "No settings available."
    
    output_string = "Current User Settings:\n"
    
    for key, value in settings.items():
        output_string += f"{key.capitalize()}: {value}\n"
        
    return output_string