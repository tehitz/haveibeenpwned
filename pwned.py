#!/usr/bin/python3

import hashlib
import requests

def hash_password(password):
    hash_object = hashlib.sha1(password.encode())
    hex_dig = hash_object.hexdigest()
    hex_dig = hex_dig.upper()
    print("Hashed password: " + hex_dig)

    #hash_start = hex_dig[0:5]
    #end_hash = hex_dig[5:]
    return hex_dig


def get_site(hashed):
    hash_start = hashed[0:5]
    site = requests.get('https://api.pwnedpasswords.com/range/' + hash_start)
    site = str(site.content)
    site = site.split('\\r\\n')
    return site


def check_hash(site, hashed):
    parse_bytecode = 0
    end_hash = str(hashed[5:]).upper()
    for entry in site:
        entry = entry.replace("'", "")
        entry = entry.split(":")
        if(parse_bytecode == 0 and end_hash == entry[0][1:]):
            entry[0] = entry[0][1:]
            return entry
        elif(entry[0] == end_hash):
            return entry
        else:
            parse_bytecode += 1
            continue

    return None


def main():
    password = input("Enter a password to be hashed: ")
    hashed = hash_password(password)
    site = get_site(hashed)
    result = []
    result = check_hash(site, hashed)
    if(result is not None):
        print("Your password hash " + hashed + " has been used " + str(result[1]) + " times")
    else:
        print("Your password hash " + hashed + " wasn't found on the database.")

    choice = input("Would you like to search another hashed password? (y/n) \n")
    if choice == "y":
        main()
    else:
        exit()

if __name__ == "__main__":
    main()
