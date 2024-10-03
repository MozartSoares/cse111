from names import make_full_name,extract_family_name, extract_given_name
import pytest

test_subjects = [
  {'given_name': 'Alex', 'family_name': 'Smith'},
  {'given_name': 'Elizabeth', 'family_name': 'Morrison-Jones'},
  {'given_name': 'Kai', 'family_name': 'Lee'},
  {'given_name': 'Charlotte-Rose', 'family_name': 'Dupont'},
  {'given_name': 'Maximiliano', 'family_name': 'Rodríguez'},
  {'given_name': 'Liam', 'family_name': 'Nguyen'},
  {'given_name': 'Olivia', 'family_name': 'Kim-Park'},
  {'given_name': 'Ava', 'family_name': 'Johnson'},
  {'given_name': 'William', 'family_name': "O'Leary"},
  {'given_name': 'Sophia', 'family_name': 'Almeida-Santos'},
  {'given_name': 'Noah', 'family_name': 'Baker'},
  {'given_name': 'Gabriel', 'family_name': 'Fernández'},
  {'given_name': 'Mia', 'family_name': 'Chen'},
  {'given_name': 'Léa', 'family_name': 'Dubois'},
  {'given_name': 'Alexander', 'family_name': 'Garcia-Hernandez'},
  {'given_name': 'Emily', 'family_name': 'Thompson'},
  {'given_name': 'Zoe', 'family_name': 'Martin'},
  {'given_name': 'Isabella', 'family_name': 'MacKenzie'},
  {'given_name': 'Oscar', 'family_name': 'Svensson'},
  {'given_name': 'Amélie', 'family_name': 'Petrovic'}
]

def test_make_full_name():
  for i in range(len(test_subjects)):
    
    test_subject = test_subjects[i]
    given_name = test_subject['given_name']
    family_name = test_subject['family_name']
    
    assert make_full_name(given_name,family_name) == f"{family_name}; {given_name}"


def test_extract_family_name():
  for i in range(len(test_subjects)):
    test_subject = test_subjects[i]
    given_name = test_subject['given_name']
    family_name = test_subject['family_name']
    full_name = make_full_name(given_name,family_name)
    
    assert extract_family_name(full_name) == family_name


def test_extract_given_name():
  for i in range(len(test_subjects)):
    test_subject = test_subjects[i]
    given_name = test_subject['given_name']
    family_name = test_subject['family_name']
    full_name = make_full_name(given_name,family_name)
    
    assert extract_given_name(full_name) == given_name


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])