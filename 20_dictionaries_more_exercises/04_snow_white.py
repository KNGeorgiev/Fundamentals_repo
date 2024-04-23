dwarves = {}


def dwarf_classificator(dwarf_data):

    name, color, physics = dwarf_data.split(" <:> ")
    physics = int(physics)

    if color not in dwarves:
        dwarves[color] = {}

    if name not in dwarves[color]:
        dwarves[color][name] = 0

    if dwarves[color][name] < physics:
        dwarves[color][name] = physics


def result_form(d):

    d_results = []

    for c in d.keys():
        for n, p in d[c].items():
            d_results.append({"color_len": len(d[c]), "dwarf_name": n, "physics": p, "color": c})

    for s in sorted(d_results, key=lambda i: (-i["physics"], -i["color_len"])):
        print(f"({s['color']}) {s['dwarf_name']} <-> {s['physics']}")


while True:

    input_line = input()

    if input_line == "Once upon a time":
        break

    dwarf_classificator(input_line)

result_form(dwarves)
