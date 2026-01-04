def cancel_order(order: dict) -> dict:
    if not order["cancellable"]:
        return {
            "success": False,
            "message": "❌ Order cannot be cancelled. Shipment already in progress."
        }

    order["status"] = "Cancelled"
    order["cancellable"] = False

    return {
        "success": True,
        "message": "✅ Your order has been successfully cancelled."
    }
