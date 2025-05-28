import os
import re
import shutil


def OPKG_to_APK_Translator(input_directory):
        opkg_to_apk_map = [
            (r'\bopkg update\b', "apk update"),
            (r'\bopkg install\b', "apk add"),
            (r'\bopkg remove\b', "apk del"),
            (r'\bopkg upgrade\b', "apk upgrade"),
            (r'\bopkg list-installed\b', "apk list"),
            (r'\bopkg search\b', "apk search"),
            (r'\bopkg info\b', "apk info"),
            (r'\bopkg\b', "apk"),
        ]

        # Confirm before proceed
        user_input = input(
        "This function will check user_directory for .sh files"
        "Proceed? (yes/no)"
        ).lower()
        if user_input == "no":
            print("User declined")
            return
        for root, _, files in os.walk(input_directory):
            for filename in files:
                if filename.lower().endswith(".sh"):
                    filepath = os.path.join(root, filename)
                    print(f"Processing {filepath}")
                    shutil.copy2(filepath, f"{filepath}.bak")
                    with open(filepath, 'r') as file:
                        file_script = file.read()
                        # Replace contents
                        for key, value in opkg_to_apk_map:
                            file_script = re.sub(key, value, file_script)
                    with open(filepath, 'w+') as file:
                        file.write(file_script)


#Prompt for input_user_directory
input_directory = input(
"Enter the path to the directory containing your .sh files "
"(leave empty for current directory): "
).strip()

#Default user_directory
if not input_directory:
    input_directory = "."

OPKG_to_APK_Translator(input_directory)