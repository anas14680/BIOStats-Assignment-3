"""This is a test file to test our functions in the Main file."""
import pytest
import pytest_cov
from Bio_stats_assignment import (
    parse_data,
    num_older_than,
    sick_patients,
    patient_age_on_first_test,
)

# test the parse data function


def test_parse_data():
    """Test Parse Data."""
    # test data with only columns
    columns_only = "columns only.txt"
    data_columns_only = {
        "PatientID": [],
        "LabName": [],
        "LabValue": [],
        "LabDateTime": [],
    }

    # test a simple sample data
    simple_data = "simple data.txt"
    data_simple_parse = {
        "Name": ["Anas", "Jon Snow", "Rumi"],
        "Age": ["25", "31", "21"],
        "City": ["Durham", "The Wall", "Ohio"],
        "Major": ["Data Science", "Ranger", "CS"],
    }

    # test a patient data
    patient_test_data = "Patient test.txt"
    parsed_patient_test = {
        "PatientID": ["ANAS123", "JON234", "RUMI874", "JONNA465"],
        "PatientGender": ["M", "M", "M", "F"],
        "PatientDateOfBirth": [
            "1996-04-04 02:45:40.547",
            "1976-12-28 02:45:40.547",
            "1984-02-28 02:45:40.547",
            "1990-07-28 02:45:40.547",
        ],
        "PatientRace": ["Asian ", "White", "Asian", "White"],
    }

    # test a sample lab test data
    labs_data_test = "LABS TEST.txt"
    parsed_patient_labs = {
        "PatientID": [
            "ANAS123",
            "ANAS123",
            "ANAS123",
            "JON234",
            "JON234",
            "JON234",
            "RUMI874",
            "RUMI874",
            "RUMI874",
            "JONNA465",
            "JONNA465",
            "JONNA465",
            "JONNA465",
        ],
        "LabName": [
            "METABOLIC: TOTAL PROTEIN",
            "CBC: HEMATOCRIT",
            "URINALYSIS: RED BLOOD CELLS",
            "METABOLIC: GLUCOSE",
            "URINALYSIS: RED BLOOD CELLS",
            "CBC: HEMATOCRIT",
            "METABOLIC: GLUCOSE",
            "URINALYSIS: RED BLOOD CELLS",
            "CBC: HEMATOCRIT",
            "METABOLIC: TOTAL PROTEIN",
            "URINALYSIS: RED BLOOD CELLS",
            "CBC: HEMATOCRIT",
            "METABOLIC: GLUCOSE",
        ],
        "LabValue": [
            "4.2",
            "3.5",
            "10.8",
            "10.0",
            "12.4",
            "9.9",
            "23.0",
            "3.8",
            "18.3",
            "14.0",
            "15.4",
            "13.1",
            "12.3",
        ],
        "LabDateTime": [
            "2021-07-01 01:36:17.910",
            "2022-01-01 01:36:17.910",
            "2021-10-01 01:36:17.910",
            "2004-07-01 01:36:17.910",
            "2012-07-01 01:36:17.910",
            "2014-07-01 01:36:17.910",
            "2011-07-01 01:36:17.910",
            "2012-07-01 01:36:17.910",
            "2013-07-01 01:36:17.910",
            "2011-07-01 01:36:17.910",
            "2011-07-01 01:36:17.910",
            "2011-07-01 01:36:17.910",
            "2011-07-01 01:36:17.910",
        ],
    }

    assert parse_data(columns_only) == data_columns_only
    assert parse_data(simple_data) == data_simple_parse
    assert parse_data(patient_test_data) == parsed_patient_test
    assert parse_data(labs_data_test) == parsed_patient_labs


# test num_older function
def test_num_older():
    """Test number older than a particular age."""
    columns_only = "columns only.txt"
    data_columns = parse_data(columns_only)

    patient_test_data = "Patient test.txt"
    patient_data = parse_data(patient_test_data)

    # 25, 45, 34, 32

    assert num_older_than(26, patient_data) == 3
    assert (
        num_older_than(25, patient_data) == 4
    )  # checks if age integer is greater than actual age like
    # person who is aged 25 is technically older than 25. Becasue he
    # 25 months X months
    assert num_older_than(38, data_columns) == "No information found regarding Age"


# test Sick patients function


def test_sick_patients():
    """Test Sick Patients fucntion."""
    labs_data_test = "LABS TEST.txt"
    parsed_lab_data = parse_data(labs_data_test)

    columns_only = "columns only.txt"
    data_columns = parse_data(columns_only)

    patient_test_data = "Patient test.txt"
    patient_data = parse_data(patient_test_data)

    # in the function i convert to a set and then list to check for unique values
    # this procedure sometimes shuffles the order of the list
    # hence had to check if this way of testing is fine
    # or should I make changes to the function
    assert sick_patients("METABOLIC: TOTAL PROTEIN", ">", 4, parsed_lab_data) in [
        [
            "JONNA465",
            "ANAS123",
        ],
        ["ANAS123", "JONNA465"],
    ]

    assert sick_patients("METABOLIC: TOTAL PROTEIN", ">", 5, parsed_lab_data) == [
        "JONNA465"
    ]

    # test how function responds with data of none of the patients meeting
    # the criteria
    assert sick_patients("CBC: HEMATOCRIT", "<", 3, parsed_lab_data) == []

    # test for value error
    with pytest.raises(ValueError):
        sick_patients("CBC: HEMATOCRIT", "=", 3, parsed_lab_data)


# check patients age on first lab test
def test_patient_age_on_first_test():
    """Test patient age on first lab test."""
    labs_data_test = "LABS TEST.txt"
    parsed_lab_data = parse_data(labs_data_test)

    simple_data = "simple data.txt"
    data_simple = parse_data(simple_data)

    patient_test_data = "Patient test.txt"
    patient_data = parse_data(patient_test_data)

    # a basic test to see if the function works correctly
    assert patient_age_on_first_test("ANAS123", parsed_lab_data, patient_data) == 25

    # To check if the function works fine if patient not found in data
    assert (
        patient_age_on_first_test("ANNA123", parsed_lab_data, patient_data)
        == "No information available on patient with ID:ANNA123"
    )
