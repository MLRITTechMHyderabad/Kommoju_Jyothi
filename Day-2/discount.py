def eligible(c):
    return 18 <= c["age"] <= 40

def discount(c):
    if 18 <= c["age"] <= 25:
        dis = c["total_purchase"] - ((c["total_purchase"] * 10) / 100)
    elif 26 <= c["age"] <= 40:
        dis = c["total_purchase"] - ((c["total_purchase"] * 5) / 100)
    else:
        dis = c["total_purchase"]  
    return {
        "name": c["name"],
        "age": c["age"],
        "total_purchase": dis  
    }

customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]

eligible_customers = filter(eligible, customers)
discounted_customers = list(map(discount, eligible_customers))
print(discounted_customers)
