def check_rule(resource, rule):
    # la règle s'applique seulement si c'est le bon type
    if resource["type"] != rule["type"]:
        return None

    field_value = resource.get(rule["field"])

    if field_value != rule["expected"]:
        return False, rule["message"]

    return True, "OK"
