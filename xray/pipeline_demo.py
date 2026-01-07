from xray.sdk import start_run, xray_step

# fake product candidates
candidates = [
    {"id": 1, "name": "Phone Case", "price": 500},
    {"id": 2, "name": "Laptop Stand", "price": 2000},
    {"id": 3, "name": "Wireless Charger", "price": 1200},
    {"id": 4, "name": "Cheap Phone Case", "price": 300},
]

run_id = start_run("competitor_selection")


@xray_step(name="price_filter", run_id=run_id)
def filter_by_price(items):
    return [c for c in items if c["price"] < 1000]


filtered = filter_by_price(candidates)

print("FINAL OUTPUT:", filtered)
