def find_the_redheads(fam):
    red=[]
    for name, col in fam.items():
        if col=="red":
            red.append(name)
    return red

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))
