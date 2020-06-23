import argparse
import re


def header2dot(filename):
    with open(filename, "r") as f:
        header = f.read().replace("\n", "@")
    struc_regex = re.compile(r"@struct (rs_\w+) \{(@.*?;@)\};@", re.MULTILINE)
    pointer_regex = re.compile(r"(rs_\w+?)\*")
    strucs = struc_regex.findall(header)
    print("digraph restruc {")
    for struc in strucs:
        pointers = []
        for pointer in pointer_regex.findall(struc[1]):
            pointers.append(pointer)
        if pointers:
            print("    {} -> {{ {} }}".format(struc[0], ", ".join(pointers)))
    print("}")


def main():
    parser = argparse.ArgumentParser(
        "Converts output from restruc to dot (graph description language)")
    parser.add_argument("-H", "--header", dest="header",
                        required=True, help="Output file from restruc")
    args = parser.parse_args()
    header2dot(args.header)


if __name__ == "__main__":
    main()
