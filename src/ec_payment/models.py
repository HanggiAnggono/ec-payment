from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field


class PaymentStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class PaymentMethod(str, Enum):
    CREDIT_CARD = "credit_card"
    DEBIT_CARD = "debit_card"
    PAYPAL = "paypal"
    BANK_TRANSFER = "bank_transfer"


class OrderStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class Payment(BaseModel):
    id: str = Field(..., description="Unique payment identifier")
    order_id: str = Field(..., description="Associated order identifier")
    amount: Decimal = Field(..., description="Payment amount", gt=0)
    currency: str = Field(..., description="Currency code (e.g., USD, EUR)")
    status: PaymentStatus = Field(..., description="Payment status")
    method: PaymentMethod = Field(..., description="Payment method used")
    created_at: datetime = Field(..., description="Payment creation timestamp")
    updated_at: datetime = Field(..., description="Payment last update timestamp")
    description: Optional[str] = Field(None, description="Payment description")


class OrderItem(BaseModel):
    id: str = Field(..., description="Item identifier")
    name: str = Field(..., description="Item name")
    quantity: int = Field(..., description="Item quantity", gt=0)
    price: Decimal = Field(..., description="Item unit price", gt=0)


class Order(BaseModel):
    id: str = Field(..., description="Unique order identifier")
    customer_id: str = Field(..., description="Customer identifier")
    items: List[OrderItem] = Field(..., description="List of order items")
    total_amount: Decimal = Field(..., description="Total order amount", gt=0)
    currency: str = Field(..., description="Currency code (e.g., USD, EUR)")
    status: OrderStatus = Field(..., description="Order status")
    created_at: datetime = Field(..., description="Order creation timestamp")
    updated_at: datetime = Field(..., description="Order last update timestamp")
    shipping_address: Optional[str] = Field(None, description="Shipping address")
    notes: Optional[str] = Field(None, description="Order notes")