import random
import string

filename = "secret"
min = 380000000 # acropol frequencies
max = 400000000
nbr = 5

units = ["Hz", "daHz", "hHz", "kHz", "MHz", "GHz", "THz", "PHz"]

with open(filename + ".in", "w") as f:
    f.write(f"{nbr}\n")

    answers = []

    for i in range(nbr):
        value = random.randrange(min, max)

        unit = random.choice(units)
        match unit:
            case "Hz":
                f.write(f"{value}{unit}\n")
                answers.append("++++++")
            case "daHz":
                value = value / 10
                f.write(f"{value}{unit}\n")
                answers.append("+++++")
            case "hHz":
                value = value / 100
                f.write(f"{value}{unit}\n")
                answers.append("++++")
            case "kHz":
                value = value / 1000
                f.write(f"{value}{unit}\n")
                answers.append("+++")
            case "MHz":
                value = value / 1000000
                f.write(f"{value}{unit}\n")
                answers.append("0")
            case "GHz": 
                value = value / 1000000000
                f.write(f"{value}{unit}\n")
                answers.append("---")
            case "THz":
                value = value / 1000000000000
                f.write(f"{value}{unit}\n")
                answers.append("------")
            case "PHz":
                value = value / 1000000000000000
                f.write(f"{value}{unit}\n")
                answers.append("---------")

    print(','. join(answers))

with open(filename + ".ans", "w") as f:
    f.write(f"{','. join(answers)}\n")
