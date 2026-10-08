import json
import sys

def calculate(cost: float, suggested_price: float | None = None):
    floor_price = cost / (1 - 0.12)
    target_price = cost / (1 - 0.18)
    price = suggested_price if suggested_price is not None else target_price
    margin = (price - cost) / price
    return {
        "cost": round(cost, 2),
        "floor_price_12pct": round(floor_price, 2),
        "target_price_18pct": round(target_price, 2),
        "price_used": round(price, 2),
        "margin_pct": round(margin * 100, 1),
    }

if __name__ == "__main__":
    cost = float(sys.argv[1])
    suggested = float(sys.argv[2]) if len(sys.argv) > 2 else None
    print(json.dumps(calculate(cost, suggested), ensure_ascii=False))
