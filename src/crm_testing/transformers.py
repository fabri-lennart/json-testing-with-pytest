import jq

def get_full_names(data):
    """Extract full names from customer data."""
    filter_ = r"""
        .data.customers[]
        | "\(.personal_info.first_name) \(.personal_info.last_name)"
    """
    result = jq.compile(filter_).input(data).all()
    return result
