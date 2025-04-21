import requests
import logging
import configparser
import os

# Configure logging for PCI-DSS Requirement 10
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/payment_api.log'),
        logging.StreamHandler()
    ]
)

def load_encryption_config(config_path='configs/encryption.conf'):
    """Load encryption settings from config file."""
    config = configparser.ConfigParser()
    if not os.path.exists(config_path):
        logging.error(f"Encryption config file not found: {config_path}")
        raise FileNotFoundError(f"Config file {config_path} not found")
    config.read(config_path)
    return config['encryption']

def process_payment(api_key, amount, currency="USD", config=None):
    """
    Process a payment using PaySafe's Hosted Payments API.
    Args:
        api_key (str): API key for authentication.
        amount (float): Payment amount in cents (e.g., 1000 = $10.00).
        currency (str): Currency code (default: USD).
        config (dict): Encryption configuration from encryption.conf.
    Returns:
        dict: API response or None if failed.
    """
    if config is None:
        config = load_encryption_config()

    # API endpoint (fictional)
    url = "https://api.paysafe.com/v1/payments"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "amount": amount,
        "currency": currency,
        "merchantRefNum": "TXN-" + str(int(os.urandom(4).hex(), 16)),
        "settleWithAuth": True
    }

    # Ensure TLS settings from config
    try:
        session = requests.Session()
        session.verify = True  # Enforce TLS verification
        logging.info(f"Initiating payment of {amount/100:.2f} {currency} with TLS {config['protocol']}")

        response = session.post(url, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        logging.info(f"Payment processed successfully: {result.get('id', 'N/A')}")
        return result
    except requests.RequestException as e:
        logging.error(f"Payment processing failed: {str(e)}")
        return None

if __name__ == "__main__":
    # Example usage with a fictional API key
    api_key = "fake-paysafe-api-key-123"
    amount = 1000  # $10.00
    result = process_payment(api_key, amount)
    if result:
        print(f"Payment successful: {result}")
    else:
        print("Payment failed")
