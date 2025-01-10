

def parse_input(filename_):
    # get the input as one large blob (not efficient for large input)
    with open(filename_) as f:
        input_data = f.read()

    # Split the input into ordering rules and updates
    rules_section, updates_section = input_data.strip().split("\n\n")
    rules = [tuple(map(int, rule.split("|")))
             for rule in rules_section.splitlines()]
    updates = [list(map(int, update.split(",")))
               for update in updates_section.splitlines()]
    return rules, updates


def build_graph(rules):
    # Create connections list
    graph, invert_graph = {}, {}

    for X, Y in rules:
        if X not in graph:
            graph[X] = set()
        graph[X].add(Y)
        if Y not in invert_graph:
            invert_graph[Y] = set()
        invert_graph[Y].add(X)

    # print(f"Invert_graph:")
    # for aKey in sorted(invert_graph.keys()):
    #     print(f"Priors {aKey}: {invert_graph[aKey]}")
    #     print(f"Afters {aKey}: {graph.get(aKey , None)}")
    # print(f"End of invert_graph \n")

    return graph, invert_graph


def validate_update(afters, priors, one_update):
    valid_updates = False
    # print(f"One update---> {anupdate}")
    for j, apage in enumerate(one_update):
        prvs = set(one_update[:j])
        afts = set(one_update[j+1:])
        # print(j, apage, '\tprvs  ', prvs)
        # print(j, apage, '\tpriors', priors.get(apage, {}))
        # print(j, apage, '\tafts  ', afts)
        # print(j, apage, '\tafters', afters.get(apage, {}))
        # print("Priors contains no afts", afts.isdisjoint(priors.get(apage, {})))
        # print("Afters contains no prvs", prvs.isdisjoint(afters.get(apage, {})))
        # print("Prvs a subset of Priors", afts.issubset(afters.get(apage, {})))
        # print("Afts a subset of Afters", prvs.issubset(priors.get(apage, {})))

        valid_updates = afts.isdisjoint(priors.get(apage, {})) \
            and prvs.isdisjoint(afters.get(apage, {})) \
            and afts.issubset(afters.get(apage, {})) \
            and prvs.issubset(priors.get(apage, {}))
        if not valid_updates:
            break
        pass

    return valid_updates


test = 0
filename = "aoc05-inp.txt" if test else "aoc05-inp copy.txt"

rules, updates = parse_input(filename)
# print(f"Parsed input: \n\tRules  : {rules} \n\n \tUpdates: {updates}")

line_graph, opp_graph = build_graph(rules)

midsum = 0
good, bad = 0,0
for i, anupdate in enumerate(updates):
    update_valid = validate_update(line_graph, opp_graph, anupdate)
    if update_valid:
        good += 1
    else:
        bad += 1
    # print(f"{i+1:3d} Update {anupdate} is {'OK' if update_valid else 'Bad.'}", end=' ' if update_valid else '\n')
    if update_valid:
        # print(f"mid {len(anupdate)//2}, value {anupdate[len(anupdate)//2]}")
        midsum += anupdate[len(anupdate)//2]
print(f"Sum of middle pages is : {midsum}.\n Good count {good} \t Bad Count {bad}")


# print(f"Rules Graph: Keys: {len(line_graph)}")
# for aKey in sorted(line_graph.keys()):
#     print(f"{aKey}: {line_graph[aKey]}")
