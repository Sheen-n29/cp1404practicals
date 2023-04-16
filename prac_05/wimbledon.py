CSV_FILE = "wimbledon.csv"


def main():
    data = get_data(CSV_FILE)
    champions, countries = get_winners(data)
    show_winners(champions, countries)


def get_data(csv_file):
    data = []
    with open(csv_file, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            data.append(parts)
    return data


def get_winners(data):
    champions = {}
    countries = set()
    for line in data:
        countries.add(line[1])
        try:
            champions[line[2]] += 1
        except KeyError:
            champions[line[2]] = 1
    return champions, countries


def show_winners(champions, countries):
    print("Wimbledon Champions: ")
    for name, counter in champions.items():
        print(name, counter)
    print(f'These {len(countries)} countries have won Wimbledon')
    print(", ".join(country for country in sorted(countries)))


main()
