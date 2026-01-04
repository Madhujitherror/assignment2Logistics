from fastapi import APIRouter
from services.intent_classifier import classify_intent
from services.order_service import get_order
from services.cancellation_service import cancel_order
from services.response_generator import generate_response
from datetime import datetime

router = APIRouter()

@router.post("/query")
def handle_query(payload: dict):
    message = payload.get("message")
    order_id = payload.get("order_id")

    intent = classify_intent(message)
    order = get_order(order_id)

    action_result = None
    if intent == "CANCEL_ORDER" and order:
        action_result = cancel_order(order)

    response = generate_response(intent, order, action_result)

    # Log for SLA & audit
    with open("logs/interactions.log", "a") as log:
        log.write(f"{datetime.now()} | {intent} | {order_id}\n")

    return {
        "intent": intent,
        "response": response
    }
