from pytest import approx
import pytest
from water_flow import kpa_to_psi,water_column_height,pressure_gain_from_water_height,pressure_loss_from_pipe,pressure_loss_from_fittings,reynolds_number,pressure_loss_from_pipe_reduction

test_water_column_height_data = [
  {'tower_height': 0, 'tank_height': 0, 'expected': 0},
  {'tower_height': 0, 'tank_height': 10, 'expected': 7.5},
  {'tower_height': 25, 'tank_height': 0, 'expected': 25},
  {'tower_height': 48.3, 'tank_height': 12.8, 'expected': 57.9},
  ]

def test_water_column_height():
  for i in range(len(test_water_column_height_data)):
    test_subject = test_water_column_height_data[i]
    assert water_column_height(test_subject['tower_height'], test_subject['tank_height']) == approx(test_subject['expected'])


test_pressure_gain_from_water_height_data = [
  {'height': 0,'expected': 0, 'abs_tolerance':0.001},
  {'height': 30.2,'expected': 295.628 , 'abs_tolerance':0.001},
  {'height': 50,'expected': 489.450, 'abs_tolerance':0.001}
]

def test_pressure_gain_from_water_height():
  for i in range(len(test_pressure_gain_from_water_height_data)):
    test_subject = test_pressure_gain_from_water_height_data[i]
    assert pressure_gain_from_water_height(test_subject['height']) == approx(test_subject['expected'], abs=test_subject['abs_tolerance'])

test_pressure_loss_from_pipe_data = [
  {'pipe_diameter': 0.048692, 'pipe_length': 0, 'friction_factor': 0.018, 'fluid_velocity': 1.75, 'expected': 0, 'abs_tolerance':0.001},	
  {'pipe_diameter': 0.048692, 'pipe_length': 200, 'friction_factor': 0, 'fluid_velocity': 1.75, 'expected': 0,'abs_tolerance':0.001},	
  {'pipe_diameter': 0.048692, 'pipe_length': 200, 'friction_factor': 0.018, 'fluid_velocity': 0, 'expected': 0,'abs_tolerance':0.001},	
  
  {'pipe_diameter': 0.048692, 'pipe_length': 200, 'friction_factor': 0.018, 'fluid_velocity': 1.75, 'expected': -113.008,'abs_tolerance':0.001},	
  
  {'pipe_diameter': 0.048692, 'pipe_length': 200, 'friction_factor': 0.018, 'fluid_velocity': 1.65, 'expected': -100.462,'abs_tolerance':0.001},	
  {'pipe_diameter': 0.286870, 'pipe_length': 1000, 'friction_factor': 0.013, 'fluid_velocity': 1.65, 'expected': -61.576,'abs_tolerance':0.001},	
  {'pipe_diameter': 0.286870, 'pipe_length': 1800.75, 'friction_factor': 0.013, 'fluid_velocity': 1.65, 'expected': -110.884,'abs_tolerance':0.001},	
]

def test_pressure_loss_from_pipe():
  for i in range(len(test_pressure_loss_from_pipe_data)):
    test_subject = test_pressure_loss_from_pipe_data[i]
    assert pressure_loss_from_pipe(test_subject['pipe_diameter'], test_subject['pipe_length'], test_subject['friction_factor'], test_subject['fluid_velocity']) == approx(test_subject['expected'], abs=test_subject['abs_tolerance'])

test_pressure_loss_from_fittings_data = [
  {'fluid_velocity': 0, 'quantity_of_fittings': 3, 'expected': 0, 'abs_tolerance': 0.001},
  {'fluid_velocity': 1.65, 'quantity_of_fittings': 0, 'expected': 0, 'abs_tolerance': 0.001},
  {'fluid_velocity': 1.65, 'quantity_of_fittings': 2, 'expected': -0.109, 'abs_tolerance': 0.001},
  {'fluid_velocity': 1.75, 'quantity_of_fittings': 2, 'expected': -0.122, 'abs_tolerance': 0.001},
  {'fluid_velocity': 1.75, 'quantity_of_fittings': 5, 'expected': -0.306, 'abs_tolerance': 0.001},
]

def test_pressure_loss_from_fittings():
  for i in range(len(test_pressure_loss_from_fittings_data)):
    test_subject = test_pressure_loss_from_fittings_data[i]
    assert pressure_loss_from_fittings(test_subject['fluid_velocity'], test_subject['quantity_of_fittings']) == approx(test_subject['expected'], abs=test_subject['abs_tolerance'])


test_reynolds_number_data = [
  {'hydraulic_diameter': 0.048692, 'fluid_velocity': 0.00, 'expected': 0, 'abs_tolerance': 1},
  {'hydraulic_diameter': 0.048692, 'fluid_velocity': 1.65, 'expected': 80069, 'abs_tolerance': 1},
  {'hydraulic_diameter': 0.048692, 'fluid_velocity': 1.75, 'expected': 84922, 'abs_tolerance': 1},
  {'hydraulic_diameter': 0.286870, 'fluid_velocity': 1.65, 'expected': 471729, 'abs_tolerance': 1},
  {'hydraulic_diameter': 0.286870, 'fluid_velocity': 1.75, 'expected': 500318, 'abs_tolerance': 1},
]

def test_reynolds_number():
  for i in range(len(test_reynolds_number_data)):
    test_subject = test_reynolds_number_data[i]
    assert reynolds_number(test_subject['hydraulic_diameter'], test_subject['fluid_velocity']) == approx(test_subject['expected'], abs=test_subject['abs_tolerance'])


test_pressure_loss_from_pipe_reduction_data = [
  {'larger_diameter': 0.28687, 'fluid_velocity': 0.00, 'reynolds_number': 1, 'smaller_diameter': 0.048692, 'expected': 0.000, 'abs_tolerance': 0.001},
  {'larger_diameter': 0.28687, 'fluid_velocity': 1.65, 'reynolds_number': 471729, 'smaller_diameter': 0.048692, 'expected': -163.744, 'abs_tolerance': 0.001},
  {'larger_diameter': 0.28687, 'fluid_velocity': 1.75, 'reynolds_number': 500318, 'smaller_diameter': 0.048692, 'expected': -184.182, 'abs_tolerance': 0.001},
]

def test_pressure_loss_from_pipe_reduction():
  for i in range(len(test_pressure_loss_from_pipe_reduction_data)):
    test_subject = test_pressure_loss_from_pipe_reduction_data[i]
    assert pressure_loss_from_pipe_reduction(
      test_subject['larger_diameter'], 
      test_subject['fluid_velocity'], 
      test_subject['reynolds_number'], 
      test_subject['smaller_diameter']
    ) == approx(test_subject['expected'], abs=test_subject['abs_tolerance'])


test_kpa_to_psi_data = [
  {'kpa': 0, 'expected': 0, 'abs_tolerance': 0.001},
  {'kpa': 101.325, 'expected': 14.696, 'abs_tolerance': 0.001},
  {'kpa': 50, 'expected': 7.2519, 'abs_tolerance': 0.001},
  {'kpa': 200, 'expected': 29.0076, 'abs_tolerance': 0.001},
  {'kpa': 500, 'expected': 72.519, 'abs_tolerance': 0.001},
]

def test_kpa_to_psi():
  for i in range(len(test_kpa_to_psi_data)):
    test_subject = test_kpa_to_psi_data[i]
    assert kpa_to_psi(test_subject['kpa']) == approx(test_subject['expected'], abs=test_subject['abs_tolerance'])

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])