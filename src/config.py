"""Runtime configuration for the invoicing service.

Shares the settlement contract with celmis-e2e-probe: the two services must
agree on the fee and the retry count or invoices and settlements diverge.
"""

import os

SETTLEMENT_CURRENCY = os.environ.get("SETTLEMENT_CURRENCY", "EUR")
FEE_RATE = float(os.environ.get("FEE_RATE", "0.029"))
#: How many times the settlement webhook is retried before giving up.
WEBHOOK_RETRIES = int(os.environ.get("WEBHOOK_RETRIES", "3"))
