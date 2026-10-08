---
name: quotation-decision
description: >
  Evaluate manufacturing quotation requests. Use this skill whenever a salesperson
  asks whether a quotation can be issued, what price range should be proposed,
  whether a customer/order needs approval, or what quotation risks must be reviewed.
---

# Quotation Decision Skill

## Goal
Produce a traceable quotation recommendation:
- APPROVE
- REVIEW
- REJECT

The agent must not invent enterprise facts. Use available tools to obtain customer,
product, cost, order-history, and capacity data.

## Required workflow
1. Identify the customer and product.
2. Read `references/customer-credit-rules.md`.
3. Read `references/pricing-rules.md`.
4. Read `references/approval-matrix.md`.
5. Use enterprise tools to obtain:
   - customer profile
   - product capability
   - latest cost
   - recent WON order history
   - available capacity
6. Use `scripts/calculate_margin.py` for deterministic price and margin calculations when needed.
7. Compare facts with the approval rules.
8. Return APPROVE / REVIEW / REJECT.
9. For REVIEW, clearly state which human role should confirm the exception.
10. Never present the result as a legally binding customer quotation.

## Required output
Customer:
Product:
Quantity:
Requested lead time:

Decision: APPROVE / REVIEW / REJECT

Latest cost:
12% margin floor:
18% target price:
Historical WON prices:
Suggested price:

Risks:
Next action:

## Governance
- Missing data must be labeled as missing.
- Never fabricate ERP / CRM / MES values.
- Any REVIEW requires human approval before customer commitment.
- REJECT reasons must cite the failed rule in plain language.
