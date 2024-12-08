import requests
import os
import bs4
from dotenv import load_dotenv

load_dotenv()

def make_cookie_jar():
    jar = requests.cookies.RequestsCookieJar()
    jar.set('session', os.getenv('SECRET'))
    return jar

def print_row(row):
    position = row.select_one('.privboard-position')
    if position:
        score = position.next_sibling
        name = row.select_one('.privboard-name').getText()
        print(position.getText(), ' ',score, ' ', name)

def print_leader_board():
    leaders = 'https://adventofcode.com/2024/leaderboard/private/view/1031380'
    r = requests.get(leaders, cookies=make_cookie_jar())
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    people = soup.select('.privboard-row')
    people.pop(0)
    for p in people:
        print_row(p)


def get_input_file(day, year=2024):
    input_url = F'https://adventofcode.com/{year}/day/{day}/input'
    r = requests.get(input_url, cookies=make_cookie_jar())
    with open(F"day{day}/long.txt","w") as f:
        f.write(r.text)
    # print(r.content)

def get_sample_data(day, year=2024):
    input_url = F'https://adventofcode.com/{year}/day/{day}'
    r = requests.get(input_url, cookies=make_cookie_jar())
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    sample_code = soup.code
    with open(F'day{day}/short.txt', 'w') as f:
        f.write(sample_code.get_text())
    print(sample_code.get_text())


if __name__ == '__main__':
    print_leader_board()
    # day = 5
    # get_input_file(day)
    # get_sample_data(day)
