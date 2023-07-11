import sys
from .constants import plz_branch
from .utils import is_main_branch, is_valid_branch_name, get_error_message, get_branch_name


def main():

    branch_name: str = get_branch_name()

    if is_main_branch(branch_name):
        print("You are not allowed to commit in main. Please create a new branch and do your changes there.")
        return sys.exit(1)
    if is_valid_branch_name(plz_branch, branch_name):
        return sys.exit(0)
    else:
        error_message: str = get_error_message(branch_name, plz_branch)
        print(error_message)

    return sys.exit(1)


if __name__ == "__main__":
    main()

