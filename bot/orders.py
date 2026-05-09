import hmac
import hashlib
import requests
from bot.logging_config import setup_logger

logger = setup_logger()
TESTNET_BASE_URL = "https://testnet.binancefuture.com"

def get_server_time():
    r = requests.get(f"{TESTNET_BASE_URL}/fapi/v1/time")
    return r.json()["serverTime"]

def place_order(client, symbol, side, order_type, quantity, price=None):
    api_key = client["api_key"]
    api_secret = client["api_secret"]

    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()

    print("\n" + "="*50)
    print("ORDER REQUEST SUMMARY")
    print("="*50)
    print(f"  Symbol     : {symbol}")
    print(f"  Side       : {side}")
    print(f"  Order Type : {order_type}")
    print(f"  Quantity   : {quantity}")
    if price:
        print(f"  Price      : {price}")
    print("="*50 + "\n")

    logger.info(f"Order place ho raha hai | {symbol} | {side} | {order_type} | qty={quantity} | price={price}")

    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
        "timestamp": get_server_time()
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    query_string = "&".join([f"{k}={v}" for k, v in params.items()])
    
    signature = hmac.new(
        api_secret.encode("utf-8"),
        query_string.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()

    params["signature"] = signature
    headers = {"X-MBX-APIKEY": api_key}

    response = requests.post(
        f"{TESTNET_BASE_URL}/fapi/v1/order",
        headers=headers,
        params=params,
        timeout=10
    )

    data = response.json()
    logger.info(f"API Response: {data}")

    if "code" in data and data["code"] != 200:
        error_msg = data.get("msg", "Unknown error")
        logger.error(f"API error: {error_msg}")
        print(f"\n❌ API ERROR: {error_msg}\n")
        raise Exception(error_msg)

    print("✅ ORDER SUCCESSFULLY PLACED!")
    print("="*50)
    print(f"  Order ID     : {data.get('orderId')}")
    print(f"  Status       : {data.get('status')}")
    print(f"  Executed Qty : {data.get('executedQty')}")
    print(f"  Avg Price    : {data.get('avgPrice', 'N/A')}")
    print("="*50 + "\n")

    logger.info(f"Order success | ID: {data.get('orderId')} | Status: {data.get('status')}")
    return data