import base64

def obscure_value(encoded_value):
    # Replace characters with underscores to obscure the encoded value
    obscured_value = encoded_value.replace('=', '_').replace('/', '-').replace('+', '~')
    return obscured_value

# Prompt the user to input the desired file name
file_name = input("Enter the desired file name: ")

# Encode the file name using Base64
encoded_name_bytes = base64.b64encode(file_name.encode())
encoded_name = encoded_name_bytes.decode()

# Obscure the encoded value
obscured_name = obscure_value(encoded_name)

# Output the obscured encoded value
print("Obfuscated encoded file name:", obscured_name)
