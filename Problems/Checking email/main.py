def check_email(string):
    if " " in string:
        return False
    if "@" not in string:
        return False
    dot_check = string.split("@")
    if dot_check[1][0] == ".":
        return False
    if "." not in dot_check[1][1:]:
        return False
    return True
