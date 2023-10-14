import sys
import time
import telepot
import RPi.GPIO as GPIO

# Initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)  # Pin 11 as output

# Function to turn on the LED
def on(pin):
    GPIO.output(pin, GPIO.HIGH)
    return 'LED is ON'

# Function to turn off the LED
def off(pin):
    GPIO.output(pin, GPIO.LOW)
    return 'LED is OFF'

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    if command == '/on':
        bot.sendMessage(chat_id, on(11))
    elif command == '/off':
        bot.sendMessage(chat_id, off(11))

# Replace 'Bot Token' with your actual bot token
bot = telepot.Bot('Bot Token')
bot.message_loop(handle)

print('I am listening...')

while 1:
    time.sleep(10)
