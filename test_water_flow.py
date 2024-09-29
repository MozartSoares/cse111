from pytest import approx
import pytest
from water_flow import water_column_height,pressure_gain_from_water_height,pressure_loss_from_pipe

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
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])