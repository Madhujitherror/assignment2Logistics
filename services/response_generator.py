def generate_response(intent, order, action_result=None):
    if not order:
        return "❌ Order not found. Please verify your Order ID."

    if intent == "ORDER_STATUS":
        return (
            f"📦 Order {order['order_id']} is currently "
            f"{order['status']} via {order['courier']}."
        )

    if intent == "CANCEL_ORDER":
        return action_result["message"]

    return "⚠️ Sorry, I couldn't understand your request."
