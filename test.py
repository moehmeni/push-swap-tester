from itertools import permutations
import subprocess


def test(n: int, max_instructions: int):
    ns = [i for i in range(n)]
    perms = permutations(ns)
    failed = []
    for perm in perms:
        arg = " ".join([str(i) for i in perm])
        print(arg)
        ps = subprocess.run(["../push_swap", arg], capture_output=True)
        check = subprocess.run(
            ["../checker_Mac", arg], input=ps.stdout, capture_output=True
        )
        check = check.stdout.decode("utf-8").strip()
        o = ps.stdout.decode("utf-8").strip().split("\n")
        print(" ".join(o) if o[0] else "(already sorted)")
        print("Actions:", len(o) if o[0] else 0)
        print("Result:", check)
        print("----------------------")
        if check == "KO" or len(o) > max_instructions:
            failed.append(arg)
    if failed:
        print(len(failed), "Tests failed ❌")
        for t in failed:
            print(t)
        print("----------------------\n")
    else:
        print(
            "Congrats! all tests passed ✅\nYour push_swap works perfectly for any combination of",
            n,
            "numbers\n",
        )


if __name__ == "__main__":
    test(3, 3)
    c = input("Do you want to test 5 numbers as well? [y/n]: ")
    if c.lower() == "y" or c == "":
        test(5, 12)
        