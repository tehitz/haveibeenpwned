# HaveIBeenPwned
This is a small Python program that utilises haveibeenpwned's API to see if a password has been compromised in any security breach.
After hashing the password, 5 bytes of that SHA-1 hash are being sent to haveibeenpwned.com's API, which they use to list passwords.
The match is then being made from results got from API.
Finally you will either get a result and the number will be displayed for quantity of that passwords usage on victims of any known breach or then you will get a notification telling that specific password wasn't in the database. 

# Demonstration
First of all, remember to chmod that file or run it in Python 3.

# to be updated
