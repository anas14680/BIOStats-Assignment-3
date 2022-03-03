"""This is a test file to test our functions in the Main file."""
import pytest
import pytest_cov
from Ehr_OOP import Patient, Lab, parse_data, num_older_than, sick_patients

# test the parse data function


def test_parse_data():
    """Test Parse data function."""
    labtest = "LABS TEST.txt"
    pattest = "Patient test.txt"
    anas = Patient(
        "ANAS123",
        "M",
        "1996-04-04 02:45:40.547",
        "Asian",
        [
            Lab(
                "URINALYSIS: RED BLOOD CELLS",
                "rbc/hpf",
                "1.8",
                "1999-07-01 01:36:17.910",
            ),
            Lab("METABOLIC: GLUCOSE", "mg/dL", "103.3", "1998-06-30 09:35:52.383"),
        ],
    )

    jon = Patient(
        "JON234",
        "M",
        "1976-12-28 02:45:40.547",
        "White",
        [
            Lab("CBC: MCH", "pg", "35.8", "1992-06-30 03:50:11.777"),
            Lab("METABOLIC: CALCIUM", "mg/dL", "8.9", "1992-06-30 12:09:46.107"),
        ],
    )

    answer = {"ANAS123": anas, "JON234": jon}

    test = parse_data(labtest, pattest)

    for i, j in zip(answer, test):
        assert answer[i].patientID == test[j].patientID
        assert answer[i].gender == test[j].gender
        assert answer[i].DOB == test[j].DOB
        assert answer[i].race == test[j].race

        answer_lab = answer[i].labs
        test_lab = test[j].labs

        for k, l in zip(answer_lab, test_lab):
            assert k.labname == l.labname
            assert k.units == l.units
            assert k.value == l.value
            assert k.labDate == l.labDate


def test_first_test_age():
    """Test age property."""
    anas = Patient(
        "ANAS123",
        "M",
        "1996-04-04 02:45:40.547",
        "Asian",
        [
            Lab(
                "URINALYSIS: RED BLOOD CELLS",
                "rbc/hpf",
                "1.8",
                "1999-07-01 01:36:17.910",
            ),
            Lab("METABOLIC: GLUCOSE", "mg/dL", "103.3", "1998-06-30 09:35:52.383"),
        ],
    )

    assert anas.age == 25


def test_age():
    """Test age property."""
    anas = Patient(
        "ANAS123",
        "M",
        "1996-04-04 02:45:40.547",
        "Asian",
        [
            Lab(
                "URINALYSIS: RED BLOOD CELLS",
                "rbc/hpf",
                "1.8",
                "1999-07-01 01:36:17.910",
            ),
            Lab("METABOLIC: GLUCOSE", "mg/dL", "103.3", "1998-06-30 09:35:52.383"),
        ],
    )

    assert anas.age_first_admission == 2


def test_num_older_than():
    """Test num older than function."""
    anas = Patient(
        "ANAS123",
        "M",
        "1996-04-04 02:45:40.547",
        "Asian",
        [
            Lab(
                "URINALYSIS: RED BLOOD CELLS",
                "rbc/hpf",
                "1.8",
                "1999-07-01 01:36:17.910",
            ),
            Lab("METABOLIC: GLUCOSE", "mg/dL", "103.3", "1998-06-30 09:35:52.383"),
        ],
    )

    jon = Patient(
        "JON234",
        "M",
        "1976-12-28 02:45:40.547",
        "White",
        [
            Lab("CBC: MCH", "pg", "35.8", "1992-06-30 03:50:11.777"),
            Lab("METABOLIC: CALCIUM", "mg/dL", "8.9", "1992-06-30 12:09:46.107"),
        ],
    )

    answer = {"ANAS123": anas, "JON234": jon}

    num_older_than(answer, 12) == 2


def test_sick_patients():
    """Test sick patients."""
    jon = [
        Lab("CBC: MCH", "pg", "35.8", "1992-06-30 03:50:11.777"),
        Lab("METABOLIC: CALCIUM", "mg/dL", "8.9", "1992-06-30 12:09:46.107"),
    ]
    anas = [
        Lab("CBC: MCH", "rbc/hpf", "1.8", "1999-07-01 01:36:17.910"),
        Lab("METABOLIC: GLUCOSE", "mg/dL", "103.3", "1998-06-30 09:35:52.383"),
    ]

    answer = {"ANAS123": anas, "JON234": jon}

    assert sick_patients("CBC: MCH", answer, ">", 1) == ["ANAS123", "JON234"]
