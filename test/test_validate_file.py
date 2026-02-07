from crm_testing.validate_file import validate_json_extension
import pytest

def test_valid_json_file():
    result = validate_json_extension("data.json")
    assert result == "data.json"

def test_invalid_txt_file():
    with pytest.raises(ValueError):
        validate_json_extension("data.txt")
