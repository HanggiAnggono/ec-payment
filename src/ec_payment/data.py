from datetime import datetime, timezone
from decimal import Decimal
from typing import List

from .models import Payment, Order, OrderItem, PaymentStatus, PaymentMethod, OrderStatus


# Static payment data
PAYMENTS: List[Payment] = [
    Payment(
        id="pay_001",
        order_id="ord_001",
        amount=Decimal("99.99"),
        currency="USD",
        status=PaymentStatus.COMPLETED,
        method=PaymentMethod.CREDIT_CARD,
        created_at=datetime(2024, 1, 15, 10, 30, 0, tzinfo=timezone.utc),
        updated_at=datetime(2024, 1, 15, 10, 35, 0, tzinfo=timezone.utc),
        description="Payment for electronics order"
    ),
    Payment(
        id="pay_002",
        order_id="ord_002",
        amount=Decimal("149.50"),
        currency="USD",
        status=PaymentStatus.PENDING,
        method=PaymentMethod.PAYPAL,
        created_at=datetime(2024, 1, 16, 14, 20, 0, tzinfo=timezone.utc),
        updated_at=datetime(2024, 1, 16, 14, 20, 0, tzinfo=timezone.utc),
        description="Payment for clothing order"
    ),
    Payment(
        id="pay_003",
        order_id="ord_003",
        amount=Decimal("75.25"),
        currency="EUR",
        status=PaymentStatus.COMPLETED,
        method=PaymentMethod.DEBIT_CARD,
        created_at=datetime(2024, 1, 17, 9, 15, 0, tzinfo=timezone.utc),
        updated_at=datetime(2024, 1, 17, 9, 18, 0, tzinfo=timezone.utc),
        description="Payment for books order"
    ),
    Payment(
        id="pay_004",
        order_id="ord_004",
        amount=Decimal("299.99"),
        currency="USD",
        status=PaymentStatus.FAILED,
        method=PaymentMethod.CREDIT_CARD,
        created_at=datetime(2024, 1, 18, 16, 45, 0, tzinfo=timezone.utc),
        updated_at=datetime(2024, 1, 18, 16, 50, 0, tzinfo=timezone.utc),
        description="Payment for furniture order"
    ),
    Payment(
        id="pay_005",
        order_id="ord_005",
        amount=Decimal("45.00"),
        currency="USD",
        status=PaymentStatus.COMPLETED,
        method=PaymentMethod.BANK_TRANSFER,
        created_at=datetime(2024, 1, 19, 11, 0, 0, tzinfo=timezone.utc),
        updated_at=datetime(2024, 1, 19, 11, 5, 0, tzinfo=timezone.utc),
        description="Payment for accessories order"
    )
]

# Static order data
ORDERS: List[Order] = [
    Order(
        id="ord_001",
        customer_id="cust_001",
        items=[
            OrderItem(id="item_001", name="Wireless Headphones", quantity=1, price=Decimal("99.99"))
        ],
        total_amount=Decimal("99.99"),
        currency="USD",
        status=OrderStatus.DELIVERED,
        created_at=datetime(2024, 1, 15, 10, 0, 0, tzinfo=timezone.utc),
        updated_at=datetime(2024, 1, 20, 15, 30, 0, tzinfo=timezone.utc),
        shipping_address="123 Main St, New York, NY 10001",
        notes="Customer requested express delivery"
    ),
    Order(
        id="ord_002",
        customer_id="cust_002",
        items=[
            OrderItem(id="item_002", name="Cotton T-Shirt", quantity=2, price=Decimal("29.99")),
            OrderItem(id="item_003", name="Jeans", quantity=1, price=Decimal("89.52"))
        ],
        total_amount=Decimal("149.50"),
        currency="USD",
        status=OrderStatus.PROCESSING,
        created_at=datetime(2024, 1, 16, 14, 0, 0, tzinfo=timezone.utc),
        updated_at=datetime(2024, 1, 16, 16, 0, 0, tzinfo=timezone.utc),
        shipping_address="456 Oak Ave, Los Angeles, CA 90210",
        notes="Gift wrapping requested"
    ),
    Order(
        id="ord_003",
        customer_id="cust_003",
        items=[
            OrderItem(id="item_004", name="Programming Book", quantity=3, price=Decimal("25.08"))
        ],
        total_amount=Decimal("75.25"),
        currency="EUR",
        status=OrderStatus.SHIPPED,
        created_at=datetime(2024, 1, 17, 9, 0, 0, tzinfo=timezone.utc),
        updated_at=datetime(2024, 1, 18, 10, 0, 0, tzinfo=timezone.utc),
        shipping_address="789 Pine Rd, London, UK SW1A 1AA",
        notes="Educational discount applied"
    ),
    Order(
        id="ord_004",
        customer_id="cust_004",
        items=[
            OrderItem(id="item_005", name="Office Chair", quantity=1, price=Decimal("299.99"))
        ],
        total_amount=Decimal("299.99"),
        currency="USD",
        status=OrderStatus.CANCELLED,
        created_at=datetime(2024, 1, 18, 16, 0, 0, tzinfo=timezone.utc),
        updated_at=datetime(2024, 1, 18, 17, 0, 0, tzinfo=timezone.utc),
        shipping_address="321 Elm St, Chicago, IL 60601",
        notes="Customer cancelled due to payment failure"
    ),
    Order(
        id="ord_005",
        customer_id="cust_005",
        items=[
            OrderItem(id="item_006", name="Phone Case", quantity=1, price=Decimal("15.00")),
            OrderItem(id="item_007", name="Screen Protector", quantity=2, price=Decimal("15.00"))
        ],
        total_amount=Decimal("45.00"),
        currency="USD",
        status=OrderStatus.DELIVERED,
        created_at=datetime(2024, 1, 19, 10, 30, 0, tzinfo=timezone.utc),
        updated_at=datetime(2024, 1, 21, 14, 0, 0, tzinfo=timezone.utc),
        shipping_address="654 Maple Dr, Miami, FL 33101",
        notes="Standard delivery"
    )
]