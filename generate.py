import yaml
import argparse

parser = argparse.ArgumentParser(
    prog="generate", description="generate author list from yaml file"
)
parser.add_argument("path", help="Path to author list yaml file")

if __name__ == "__main__":
    args = parser.parse_args()

    with open(args.path) as f:
        author_list = yaml.safe_load(f)

    letter_ix = 0
    letters = "ᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ"

    affiliations = {}
    for author, info in author_list.items():
        for affiliation in info["affiliations"]:
            if not affiliation in affiliations:
                affiliations[affiliation] = letters[letter_ix]
                letter_ix += 1

    output = ""
    for info in author_list.values():
        first_name = ".".join([name[0] for name in info["first name"].split()])
        if info["middle names"]:
            middle_names = ".".join([name[0] for name in info["middle names"].split()])
        else:
            middle_names = ""
        last_name = info["last name"]
        titles = info["titles"]
        letters = ",".join([affiliations[a] for a in info["affiliations"]])

        element = f"{first_name}.{middle_names}{'.' if middle_names else ''} {last_name}{letters} {titles}, "

        output += element

    output = output[:-2] + "\n\n"

    for affiliation, letter in affiliations.items():
        element = f"{letter} {affiliation}\n"
        output += element

    print(output)
