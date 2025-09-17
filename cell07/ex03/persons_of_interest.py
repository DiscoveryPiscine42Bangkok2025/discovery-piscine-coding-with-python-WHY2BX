def famous_births(dict):
    data = dict.values()
    sorted_data = sorted(data, key=lambda person: person["date_of_birth"])
    for p in sorted_data:
        print(f"{p['name']} is a great scientist born in {p['date_of_birth']}.")

women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecila Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
}

famous_births(women_scientists)