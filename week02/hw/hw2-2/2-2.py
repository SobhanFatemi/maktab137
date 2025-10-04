import json

class InvalidConfigError(Exception):
    "Your config is invalid."


filepath = "Home Work/2/2/config.json"
def load_config(filepath):
    try:
        with open(filepath, 'r') as file:
            loaded_data = json.load(file)

        keys = list(loaded_data.keys())
        is_mode = False
        is_database_url = False
        is_api_key = False
        i = 0
        while i < len(keys):
            if keys[i] == "mode":
                is_mode = True
            elif keys[i] == "database_url":
                is_database_url = True
            elif keys[i] == "api_key":
                is_api_key = True
            i += 1
        
        if is_mode == False or is_database_url == False or is_api_key == False:
            raise InvalidConfigError("Your config is invalid.")
        
        if loaded_data.get("mode") != "production" and loaded_data.get("mode") != "debug":
            raise InvalidConfigError("Your config is invalid.")
        
        print(loaded_data)


    except FileNotFoundError as error:
        print(f"File was not found: {error}")
    except json.decoder.JSONDecodeError as error:
        print(f'Jason file invalid: {error}')
    except InvalidConfigError as error:
        print(f'Config format invalid: {error}')

load_config(filepath)