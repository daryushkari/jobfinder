#from django.test import TestCase

# Create your tests here.
import bcrypt

password = 'foobar'
password_hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
print(str(password_hashed))
j = 'c.jpg'
print(j.split('.')[-1])

