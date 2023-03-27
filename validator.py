"""! Verify the validity of the given dictionary object.
 The definition for the object is: data = {
   "id": <required: Integer value> 
   "name": <required: string value, must be at least two, space separated values> 
   "email": <optional: string> 
   "is_active": <required: boolean> 
   "roles": [], <required: array of strings, van be empty> 
   "last_login": <required: time stamp string> 
} @result The return value is True if the passed in object is valid, False if an error was found. """

def validate_data(data):
    
    if not isinstance(data, dict):
        return False
    # Validate "id"
    if not isinstance(data["id"], int):
        return False

    # Validate "name"
    if not isinstance(data["name"], str) or len(data["name"].split()) < 2:
        return False

    # Validate "email"
    if email is in data and not isinstance(data["email"], str):
        return False

    # Validate "is_active"
    if not isinstance(data["is_active"], bool):
        return False

    # Validate "roles"
    if not isinstance(data["roles"], list):
        return False
    # Validate "last_login"
    if not isinstance(data["last_login"], str):
        return False

    return True
