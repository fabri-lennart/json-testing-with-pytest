import jq

def extract_mails(data):
    """Extract emails ending with .com using jq"""
    filter_ = '.data.customers[].personal_info.email | select(endswith(".com"))'
    return jq.compile(filter_).input(data).all()
