import click
from bot.client import get_client
from bot.validators import validate_inputs
from bot.orders import place_order
from bot.logging_config import setup_logger

logger = setup_logger()

@click.command()
@click.option("--symbol",     required=True, help="Trading pair, e.g. BTCUSDT")
@click.option("--side",       required=True, help="BUY ya SELL")
@click.option("--order-type", required=True, help="MARKET ya LIMIT")
@click.option("--quantity",   required=True, type=float, help="Quantity")
@click.option("--price",      default=None,  type=float, help="Sirf LIMIT ke liye")
def main(symbol, side, order_type, quantity, price):
    """Binance Futures Testnet Trading Bot"""
    try:
        validate_inputs(symbol, side, order_type, quantity, price)
        client = get_client()
        place_order(client, symbol, side, order_type, quantity, price)
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        print(f"\n⚠️  INPUT ERROR: {e}\n")
    except Exception as e:
        logger.error(f"Bot error: {e}")
        print(f"\n❌ ERROR: {e}\n")

if __name__ == "__main__":
    main()