
from datetime import date
from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel, Field


class InvoiceItem(BaseModel):
    description: str
    quantity: Optional[Decimal] = None
    unit_price: Optional[Decimal] = None
    amount: Optional[Decimal] = None


class Invoice(BaseModel):
    invoice_number: Optional[str] = None
    vendor_name: Optional[str] = None
    customer_name: Optional[str] = None
    invoice_date: Optional[date] = None
    due_date: Optional[date] = None
    currency: Optional[str] = None

    items: List[InvoiceItem] = Field(default_factory=list)

    subtotal: Optional[Decimal] = None
    tax: Optional[Decimal] = None
    total: Optional[Decimal] = None
