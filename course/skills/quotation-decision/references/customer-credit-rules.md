# Customer Credit Rules

- credit_status = BLOCKED -> REJECT.
- credit_status = WATCH -> REVIEW.
- payment_terms_days > max_payment_terms_days -> REVIEW.
- GOOD status with terms within limit passes the customer-credit check.
