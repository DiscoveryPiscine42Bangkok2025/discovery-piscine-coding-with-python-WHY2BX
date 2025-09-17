def array_of_names(persons):
    arr=[]
    for first, last in persons.items():
        name = first.capitalize()+" "+last.capitalize()
        arr.append(name)
    return(arr)

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))
