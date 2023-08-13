def add_route():
    return "add_route_success"

def add_rule(rule_name, rule_location, rule_value):
    if len(rule_name) == 0:
        raise ValueError("Rule name is not filled.")

    return "Rule added successfully."
