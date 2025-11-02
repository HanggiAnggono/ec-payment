from fastapi import FastAPI

from ec_payment.config import Settings
from ec_payment.dto.payment_dto import CreatePaymentRequestDTO, PaymentWebhookRequestDTO
from ec_payment.services.payment_service import PaymentService


app = FastAPI(
    title="EC Payment API",
    description="A simple payment and order management API",
    version="0.1.0",
)

payment_svc = PaymentService()


@app.get("/")
async def hello_world():
    """Simple hello world endpoint"""
    return {"message": "Ok"}


@app.post("/create-payment")
async def create_transaction(payment_request: CreatePaymentRequestDTO):
    """Create Transaction"""
    resp = payment_svc.create_payment(payment_request)
    return resp

@app.post("/handle-webhook")
async def handle_webhook(webhook_request: PaymentWebhookRequestDTO):
  """Handle Webhook"""
  payment_svc.handle_webhook(webhook_request)