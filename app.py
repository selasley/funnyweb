from flask import Flask
import random

app = Flask(__name__)

_jokes = [
    'How do you get the code for the bank vault?<br>You checkout their branch.',
    'What do you call a busy waiter?<br>A server.',
    'Why did the security conscious engineer refuse to pay their dinner bill?<br>Because they could not verify the checksum.',
    'What did the array say after it was extended?<br>Stop objectifying me.',
    'Whats the object-oriented way to become wealthy?<br>Inheritance',
]


@app.get('/')
def tell_a_joke():
    joke = random.choice(_jokes)
    return f'<p>{joke}</p>'