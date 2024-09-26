import math


def compute_volume(radius,height):
  volume = math.pi * radius**2 * height
  return volume

def compute_surface_area(radius, height):
  surface_area = 2 * math.pi * radius * (radius + height) 
  return surface_area

def compute_cost_efficiency(volume, cost):
  cost_efficiency = volume / cost
  return cost_efficiency

def main():
  name = ['#1 Picnic', '#1 Tall', '#2', '#2.5', '#3 Cylinder', '#5', '#6Z', '#8Z short', '#10', '#211', '#300', '#303']
  radius = [6.82, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
  height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
  cost = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]
  
  
  best_can_efficiency = 0
  best_storage_efficiency = 0
  for i in range(len(name)):
    can_name = name[i]
    can_radius = radius[i]
    can_height = height[i]
    can_cost = cost[i]
  
    can_volume = compute_volume(can_radius,can_height)
    can_surface = compute_surface_area(can_radius,can_height)
    
    can_efficiency = can_volume / can_surface
    if best_can_efficiency < can_efficiency:
      best_can_efficiency = can_efficiency

    can_cost_efficiency = compute_cost_efficiency(can_volume,can_cost)
    if best_storage_efficiency < can_cost_efficiency:
      best_storage_efficiency = can_cost_efficiency
      
    print(f"{can_name} {round(can_efficiency)} with a {can_cost_efficiency:.2f}")
  print(f"The highest can efficiency is {best_can_efficiency:.2f}")
  print(f"The highest storage efficiency is {best_storage_efficiency:.2f}")

main()

#highest cost_efficiency: #5 3 with a 9169.08