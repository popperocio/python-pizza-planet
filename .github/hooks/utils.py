import re
import subprocess


def get_branch_name() -> str:
    return str(
        subprocess.run(
            "git rev-parse --abbrev-ref HEAD", shell=True, check=True, stdout=subprocess.PIPE
        ).stdout
    )[2:-3]


def is_main_branch(branch_name) -> bool:
    return branch_name == "main"


def is_valid_branch_name(regular_expression, branch_name) -> bool:
    return bool(re.match(regular_expression, branch_name))


def get_error_message(branch_name, regular_expression):
    return f'''\n
        Error message:
            The following name is not allowed: {branch_name}
            Please rename your branch with using the following regex: 
            {regular_expression} 
            or PlZ-<number_ticket>-<title_ticket> 
            You won't be able to push or commit your changes until the issue is solved.
            '''

