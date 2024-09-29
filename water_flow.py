water_density = 998.2
gravity_acceleration = 9.80665

def water_column_height(tower_height, tank_height):
  water_column_height = tower_height + 3*tank_height/4
  return water_column_height

def pressure_gain_from_water_height(height):
  pressure = water_density*gravity_acceleration*height/1000
  return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length,friction_factor,fluid_velocity):
  pressure_loss = (-friction_factor*pipe_length*water_density*fluid_velocity**2)/(2000*pipe_diameter)
  return pressure_loss

def main():
  return 2 

if __name__ == '__main__':
  main()