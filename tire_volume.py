#205/60R15 - 205 = w, 60 = a, 15 = d
#v = volume in liters
#pi = 3.14159 math.pi
#w - width in cm
#a - aspect ratio
#d - diameter in inches
#v = (pi * w^2 * a * (w * a + 2540 * d)) / 1000000
import math
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

  print(f'The approximate volume is: {round(tire_volume(int(width), int(aspect_ratio), int(diameter)),2)} liters')

main()