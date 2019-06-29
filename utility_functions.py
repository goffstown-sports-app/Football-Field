import subprocess

def check_type(item, expected_type):
    """
    Checks a object to make sure that it is a certain type
    :param item: any type
    :param expected_type: string (ex:"str")
    :return: type
    """
    item_type = str(type(item))
    if "str" in expected_type.lower() and item_type == "<class 'str'>":
        pass
    elif "int" in expected_type.lower() and item_type == "<class 'int'>":
        pass
    elif "bool" in expected_type.lower() and item_type == "<class 'bool'>":
        pass
    elif "float" in expected_type.lower() and item_type == "<class 'float'>":
        pass
    elif "tuple" in expected_type.lower() and item_type == "<class 'tuple'>":
        pass
    elif "list" in expected_type.lower() and item_type == "<class 'list'>":
        pass
    elif "dict" in expected_type.lower() and item_type == "<class 'dict'>":
        pass
    else:
        raise Exception("{a} isn't a {b}".format(a=object, b=expected_type))
    return item_type


# Testing
# check_type(8, "int")
# check_type(1.1, "float")
# check_type([], "list")
# check_type({}, "dict")
# check_type((), "tuple")
# check_type(True, "bool")
# check_type("testing testing", "str")


def run_command(shell_command, get_output):
    """
    Will run a shell command using the subprocess module
    :param shell_command: The command that is going to be ran (str)
    :param get_output: Will capture the output of the command
    :return: the command output
    """
    # Type checking:
    check_type(shell_command, "str")
    check_type(get_output, "bool")

    # Main:
    command_parts = shell_command.split(" ")
    subprocess_command = subprocess.run(command_parts, capture_output=get_output)
    if get_output:
        string_command = str(subprocess_command)
        stdout_position = string_command.find("stdout")
        stderr_position = string_command.find("stderr")
        relative_string = string_command[stdout_position:stderr_position]
        final_string = relative_string[relative_string.find("'") + 1:-3]
        return final_string
    else:
        return subprocess_command
