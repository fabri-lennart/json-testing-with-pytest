
from crm_testing.extractors import extract_mails

def test_extract_mails_only_com():
    data = {
        "data": {
            "customers": [
                {
                    "personal_info": {
                        "email": "juan@gmail.com"
                    }
                },
                {
                    "personal_info": {
                        "email": "ana@yahoo.es"
                    }
                },
                {
                    "personal_info": {
                        "email": "pedro@hotmail.com"
                    }
                }
            ]
        }
    }

    result = extract_mails(data)

    assert result == [
        "juan@gmail.com",
        "pedro@hotmail.com"
    ]
