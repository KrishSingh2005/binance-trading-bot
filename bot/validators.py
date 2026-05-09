from bot.logging_config import setup_logger

logger = setup_logger()

VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]

def validate_inputs(symbol, side, order_type, quantity, price):
    
    # Symbol check
    if not symbol or len(symbol) < 3:
        raise ValueError(f"Invalid symbol: '{symbol}'. Example: BTCUSDT")

    # Side check
    if side.upper() not in VALID_SIDES:
        raise ValueError(f"Invalid side: '{side}'. Choose: BUY ya SELL")

    # Order type check
    if order_type.upper() not in VALID_ORDER_TYPES:
        raise ValueError(f"Invalid order type: '{order_type}'. Choose: MARKET ya LIMIT")

    # Quantity check
    if quantity <= 0:
        raise ValueError(f"Quantity must be greater than 0. Tumne diya: {quantity}")

    # Price check (sirf LIMIT ke liye zaroori)
    if order_type.upper() == "LIMIT":
        if price is None or price <= 0:
            raise ValueError("LIMIT order ke liye price dena zaroori hai aur 0 se zyada hona chahiye")

    logger.info(f"Validation passed | {symbol} | {side} | {order_type} | qty: {quantity}")
    return True