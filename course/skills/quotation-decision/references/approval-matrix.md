# Approval Matrix

## Product / specification
- Product not found -> REJECT.
- status = REVIEW_ONLY -> REVIEW.
- Required temperature above product rating -> REJECT.
- RoHS required but product rohs=N -> REJECT.
- Custom printing requested but product custom_print=N -> REVIEW.
- Quantity below MOQ -> REVIEW.

## Capacity / lead time
- requested lead time shorter than standard lead time -> REVIEW.
- requested quantity exceeds available capacity -> REVIEW.
- If expedite_possible=N and capacity is insufficient, production manager approval is mandatory.

## Final
- Any REJECT rule -> REJECT.
- Otherwise any REVIEW rule -> REVIEW.
- Otherwise -> APPROVE.
