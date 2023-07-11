#!/usr/bin/env python3

import sys


def main():
    with open(sys.argv[1], "r", encoding="utf-8") as f_p:

        commit_prefix = ('fix:', 'feat:', 'refactor:', 'test:', 'merge:')

        lines = f_p.readlines()

        for commit_msg in lines:

            if commit_msg[0] == "#":
                continue
            if commit_msg.startswith(commit_prefix):
                print("Commit message is valid")
                print(commit_msg)
                return sys.exit(0)
            else:
                print(
                    f"""Commit error: The commit message should start with 
                    {','.join(commit_prefix)}'"""
                )

    return sys.exit(1)



if __name__ == "__main__":
    main()
