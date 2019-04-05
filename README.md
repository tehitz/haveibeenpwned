# HaveIBeenPwned
This is a small Python program that utilises haveibeenpwned's API to see if a password has been compromised in any security breach.
After hashing the password, 5 bytes of that SHA-1 hash are being sent to haveibeenpwned.com's API, which they use to list passwords.
The match is then being made from results got from API.
Finally you will either get a result and the number will be displayed for quantity of that passwords usage on victims of any known breach or then you will get a notification telling that specific password wasn't in the database. 

# Demonstration
First of all, remember to chmod that file to be executable or run it in Python 3.
You will need Python 3 in order to run this program. 

Usage: 

$ python3 pwned.py 

Enter a password to be hashed: asdf

Hashed password: 3DA541559918A808C2402BBA5012F6C60B27661C

Your password hash 3DA541559918A808C2402BBA5012F6C60B27661C has been used 313219 times

Would you like to search another hashed password? (y/n) 

y

Enter a password to be hashed: pasdf

Hashed password: FC0BCC818FB8965927874DC83C275F9A94E9E748

Your password hash FC0BCC818FB8965927874DC83C275F9A94E9E748 has been used 13 times

Would you like to search another hashed password? (y/n)

n

# Acknowledgements
I know that this could've been done more easily and the quality of code isn't great.
Maybe next time I will research more before I start doing. 
I hope that at least someone would enjoy this. 
