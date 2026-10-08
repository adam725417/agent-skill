from pathlib import Path
import pandas as pd
from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

PRODUCTS = pd.read_csv(DATA / "products.csv")
CUSTOMERS = pd.read_csv(DATA / "customers.csv")
COSTS = pd.read_csv(DATA / "costs.csv")
ORDERS = pd.read_csv(DATA / "orders.csv")
CAPACITY = pd.read_csv(DATA / "capacity.csv")

mcp = FastMCP("quotation-enterprise-tools")

@mcp.tool()
def customer_lookup(customer_query: str) -> dict:
    """Look up customer credit status, payment terms, tier, and currency."""
    q = customer_query.strip().lower()
    row = CUSTOMERS[
        CUSTOMERS.customer_code.astype(str).str.lower().eq(q)
        | CUSTOMERS.customer_name.astype(str).str.lower().str.contains(q, regex=False)
    ]
    return {"found": False, "query": customer_query} if row.empty else {"found": True, **row.iloc[0].to_dict()}

@mcp.tool()
def product_lookup(product_code: str) -> dict:
    """Look up product capability, temperature rating, RoHS, custom print, MOQ, and standard lead time."""
    row = PRODUCTS[PRODUCTS.product_code.astype(str).str.upper() == product_code.upper()]
    return {"found": False, "product_code": product_code} if row.empty else {"found": True, **row.iloc[0].to_dict()}

@mcp.tool()
def latest_cost(product_code: str) -> dict:
    """Return the latest available total unit cost for a product."""
    row = COSTS[COSTS.product_code.astype(str).str.upper() == product_code.upper()].sort_values("effective_month")
    return {"found": False, "product_code": product_code} if row.empty else {"found": True, **row.iloc[-1].to_dict()}

@mcp.tool()
def order_history(customer_code: str, product_code: str, limit: int = 3) -> dict:
    """Return recent WON order prices for the customer and product."""
    row = ORDERS[
        (ORDERS.customer_code.astype(str) == customer_code)
        & (ORDERS.product_code.astype(str).str.upper() == product_code.upper())
        & (ORDERS.result.astype(str).str.upper() == "WON")
    ].sort_values("order_date", ascending=False).head(limit)
    return {"found": not row.empty, "records": row.to_dict(orient="records")}

@mcp.tool()
def capacity_check(product_code: str, month: str = "2026-10") -> dict:
    """Return monthly capacity, committed quantity, available quantity, and expedite capability."""
    row = CAPACITY[
        (CAPACITY.product_code.astype(str).str.upper() == product_code.upper())
        & (CAPACITY.month.astype(str) == month)
    ]
    return {"found": False, "product_code": product_code, "month": month} if row.empty else {"found": True, **row.iloc[0].to_dict()}

if __name__ == "__main__":
    mcp.run()
