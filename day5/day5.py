def get_input(file_name):
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    return lines


def generate_updates(first_element, page_updates: list[str], pairs=[]):
    if len(page_updates) > 0:
        pairs = pairs + (list(map(lambda u: f'{first_element}|{u}', page_updates)))
        return generate_updates(page_updates.pop(0), page_updates, pairs)
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
    total_middle_page_numbers = 0
    while len(updates) > 0:
        one_set_of_page_updates = updates.pop(0)
        middle_page_number = one_set_of_page_updates[int(len(one_set_of_page_updates)/2)]
        page_updates = generate_updates(one_set_of_page_updates.pop(0), one_set_of_page_updates)
        print('page update: ', page_updates)
        if check_updates_against_rules(page_ordering_rules, page_updates):
            total_middle_page_numbers = total_middle_page_numbers + int(middle_page_number)
    print('part 1: ', total_middle_page_numbers)

        


def part2():
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
    total_middle_page_numbers = 0
    while len(updates) > 0:
        one_set_of_page_updates = updates.pop(0)
        sorted_page_updates_just_in_case = sorted(one_set_of_page_updates, reverse=True)
        middle_page_number = sorted_page_updates_just_in_case[int(len(sorted_page_updates_just_in_case)/2)]
        print(sorted_page_updates_just_in_case, middle_page_number)
        page_updates = generate_updates(one_set_of_page_updates.pop(0), one_set_of_page_updates)
        if not check_updates_against_rules(page_ordering_rules, page_updates):
            total_middle_page_numbers = total_middle_page_numbers + int(middle_page_number)
    print('part 2:', total_middle_page_numbers)

if __name__ == "__main__":
    part1()
    part2()