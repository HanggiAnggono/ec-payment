from ec_payment.provider.midtrans_provider import Customer, MidtransProvider
from ec_payment.dto.payment_dto import CreatePaymentRequestDTO, CreatePaymentResponseDTO, CustomerDTO, PaymentWebhookRequestDTO
from typing import Dict, Any
import logging

# Set up logging
logger = logging.getLogger(__name__)


class PaymentService:
    def __init__(self):
        """Initialize PaymentService with MidtransProvider"""
        self.payment_provider = MidtransProvider()

    def create_payment(self, create_payment_request: CreatePaymentRequestDTO) -> CreatePaymentResponseDTO:

        """
        Create a payment transaction using the configured payment provider

        Args:
            create_payment_request: Payment request DTO containing order details

        Returns:
            CreatePaymentResponseDTO: Response containing transaction details
        """
        try:
            logger.info(f"Processing payment creation for order_id: {create_payment_request.order_id}")

            # Convert CustomerDTO to dictionary for Midtrans
            customer_dict = create_payment_request.customer.model_dump()

            # Create payment using Midtrans provider
            transaction_response = self.payment_provider.create_payment(
                order_id=create_payment_request.order_id,
                amount=create_payment_request.amount,
                customer=customer_dict
            )

            # Extract relevant information from Midtrans response
            transaction_token = transaction_response.get('token')
            redirect_url = transaction_response.get('redirect_url')

            logger.info(f"Payment created successfully for order_id: {create_payment_request.order_id}")

            return CreatePaymentResponseDTO(
                success=True,
                transaction_token=transaction_token,
                redirect_url=redirect_url,
                order_id=create_payment_request.order_id,
                message="Payment transaction created successfully",
                error=None
            )

        except Exception as e:
            logger.error(f"Failed to create payment for order_id: {create_payment_request.order_id}, error: {str(e)}")

            return CreatePaymentResponseDTO(
                success=False,
                transaction_token=None,
                redirect_url=None,
                order_id=create_payment_request.order_id,
                message="Failed to create payment transaction",
                error=str(e)
            )

    def handle_webhook(self, handle_webhook_request: PaymentWebhookRequestDTO):
        # create payment with ORM here
        # publish a payment created event
        None