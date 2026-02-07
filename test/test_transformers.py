from crm_testing.transformers import get_full_names

def test_get_full_names():
    data = {
        "data": {
            "customers": [
                {"personal_info": {"first_name": "Juan", "last_name": "Pérez"}}
            ]
        }
    }
    result = get_full_names(data)
    assert result == ["Juan Pérez"]
