#205/60R15 - 205 = w, 60 = a, 15 = d
#v = volume in liters
#pi = 3.14159 math.pi
#w - width in cm
#a - aspect ratio
#d - diameter in inches
#v = (pi * w^2 * a * (w * a + 2540 * d)) / 1000000
import math
from datetime import datetime

tire_volume = lambda w, a, d: math.pi * w**2 * a * (w * a + 2540 * d) / 10000000000

def ask_for_input():
  width = input('Enter the width of the tire in mm (ex 205):')
  aspect_ratio = input('Enter the aspect ratio of the tire (ex 60):')
  diameter = input('Enter the diameter of the wheel in inches (ex 15):')

  return width, aspect_ratio, diameter

def main():
  while True:
        width, aspect_ratio, diameter = ask_for_input()
        
        if (width.isnumeric() and aspect_ratio.isnumeric() and diameter.isnumeric() and 
            int(width) > 0 and int(aspect_ratio) > 0 and int(diameter) > 0):
            break
        else:
            print("Invalid input. Please enter positive numeric values for width, aspect ratio, and diameter.")
  
  volume = round(tire_volume(int(width), int(aspect_ratio), int(diameter)),2)
  print(f'The approximate volume is: {volume} liters')

  current_date = f"{datetime.now():%Y-%m-%d}"
  
  while True:
    client_is_buying = input('Are you interested in buying a tire with the specified dimensions? (y/n)')
    match client_is_buying.lower():
      case 'y':
        print('Great! We have a variety of tires in stock.')
        phone_number = input('Please enter your phone number so we can contact you to discuss the options:')
        open('volumes.txt', 'at').write(f'Client number: {phone_number} - ')
        break
      case 'n':
        print('No problem! If you change your mind, feel free to contact us.')
        break
      case _:
        print('Invalid input. Please enter y or n.')

  open('volumes.txt', 'at').write(f'{current_date}, {width}, {aspect_ratio}, {diameter}, {volume}\n')

main()