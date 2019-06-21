def check_type(object, expected_type):
    """
    Checks a object to make sure that it is a certain type
    :param object: any type
    :param expected_type: string (ex:"str")
    :return: none
    """
    object_type = type(object)
    if "str" in expected_type.lower() and object_type == "<class 'str'>":
        pass
    elif "int" in expected_type.lower() and object_type == "<class 'int'>":
        pass
    elif "bool" in expected_type.lower() and object_type == "<class 'bool'>":
        pass
    elif "float" in expected_type.lower() and object_type == "<class 'float'>":
        pass
    elif "tuple" in expected_type.lower() and object_type == "<class 'tuple'>":
        pass
    elif "list" in expected_type.lower() and object_type == "<class 'list'>":
        pass
    elif "dict" in expected_type.lower() and object_type == "<class 'dict'>":
        pass
    else:
        raise Exception("{a} isn't a {b}".format(a=object, b=expected_type))