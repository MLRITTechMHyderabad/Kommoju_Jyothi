employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]
a= list(map (lambda e:{
    "name":e["name"],
    "salary":(
        e["salary"]+((e["salary"]*10)/100)
        if e["rating"] in [4,5]
        else
        e["salary"]+((e["salary"]*5)/100) if e["rating"] ==3
        else
        e["salary"]-((e["salary"]*3)/100) if e["rating"] in [1,2]
        else
        e["salary"]
        ), "rating": e["rating"]},employees))
print(a)
