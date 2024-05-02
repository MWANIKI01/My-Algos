# Author: Mr.Un1k0d3r - RingZer0 Team 2017
# COM Scriptlet payload obfuscator

import random
import string

def obfuscate_payload(original):
    obfuscated_payload = ""
    for char in original:
        if char.isdigit():
            newval = random.randint(1, 100)
            obfuscated_payload += char + "-" + str(newval)
        else:
            obfuscated_payload += char
    return obfuscated_payload

if __name__ == "__main__":
    print("COM Scriptlet payload (SCT file) obfuscator")
    print("Mr.Un1k0d3r - RingZer0 Team 2017\n\n")

    # Prompt user for payload input
    payload = input("Enter the payload:\n")

    try:
        # Obfuscate the payload
        obfuscated_payload = obfuscate_payload(payload)

        # Output the obfuscated payload
        print("\nObfuscated Payload:\n", obfuscated_payload)

    except Exception as e:
        print("Error:", e)
