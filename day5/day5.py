def get_input(file_name):
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    return lines


def generate_updates(first_element, page_updates: list[str]):
    pairs = list(map(lambda u: f'{first_element}|{u}', page_updates))
    print(pairs)
    if len(page_updates) > 1:
        return pairs.append(generate_updates(page_updates.pop(0), page_updates))
    return pairs


def check_updates_against_rules(rules: list[str], updates: list[str]):
    for u in updates:
        if u not in rules:
            return False
    return True

def part1():
    lines = get_input('short.txt')
    reading_rules = True
    page_ordering_rules = []
    updates = []
    for l in lines:
        if len(l) == 0:
            reading_rules = False
            continue
        if reading_rules:
            page_ordering_rules.append(l)
        else:
            updates.append( l.split(','))  
    while len(updates) > 0:
        one_set_of_page_updates = updates.pop(0)
        page_updates = generate_updates(one_set_of_page_updates.pop(0), one_set_of_page_updates)
        print(page_updates)
        # if check_updates_against_rules(page_ordering_rules, page_updates):
        #     print(page_updates)

        


def part2():
    pass


if __name__ == "__main__":
    part1()