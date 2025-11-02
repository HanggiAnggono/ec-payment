from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CustomerDTO(BaseModel):
    first_name: str = Field(..., description="Customer first name")
    last_name: str = Field(..., description="Customer last name")
    email: str = Field(..., description="Customer email address")
    phone: str = Field(..., description="Customer phone number")


class CreatePaymentRequestDTO(BaseModel):
    order_id: str = Field(..., description="Unique order identifier")
    amount: int = Field(..., description="Payment amount in smallest currency unit (e.g., cents)")
    customer: CustomerDTO = Field(..., description="Customer details")
    description: Optional[str] = Field(None, description="Payment description")


class CreatePaymentResponseDTO(BaseModel):
    success: bool = Field(..., description="Whether the payment creation was successful")
    transaction_token: Optional[str] = Field(None, description="Midtrans transaction token")
    redirect_url: Optional[str] = Field(None, description="Payment redirect URL")
    order_id: str = Field(..., description="Order identifier")
    message: Optional[str] = Field(None, description="Response message")
    error: Optional[str] = Field(None, description="Error message if any")

class PaymentWebhookRequestDTO(BaseModel):
    order_id: str = Field(..., description="Order identifier")