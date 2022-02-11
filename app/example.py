import itertools
import string


def dupa_printing(var: str) -> bool:
    return isinstance(var, str) and var == "dupa1"


def get_name_list_from_description(namekey: str, contents: dict):
    return [x for x in contents.keys() if x == namekey]


def main():
    # Generate a gen() object
    contents = ((f"type_{i}", i + 1) for i in range(len(string.ascii_lowercase)))
    print(contents)
    description = {
        # Slice gen() to [0:10] with step 1
        "table_two_content": dict(itertools.islice(contents, 0, 10, 1)),
        # Remaining part of the gen() object
        "table_one_content": dict(itertools.islice(contents, 0)),
    }

    content_key = "table_one_content"
    namekey = "type_20"
    name_list = (
        get_name_list_from_description(namekey, description[content_key])
        if content_key in description
        else []
    )
    print(name_list)


if __name__ == "__main__":
    main()
