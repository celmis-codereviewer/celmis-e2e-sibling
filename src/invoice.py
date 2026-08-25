"""Invoicing, which reads the settlement fee to compute what to bill."""

from src.config import FEE_RATE


def invoice_total(gross: float) -> float:
    """What the customer is billed, net of the platform fee."""
    return gross - (gross * FEE_RATE)
