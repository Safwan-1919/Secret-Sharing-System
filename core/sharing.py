
from secretsharing import PlaintextToHexSecretSharer

def split_secret(secret_string, num_shares, threshold):
    """
    Splits a secret string into a number of shares.

    Args:
        secret_string (str): The secret to split.
        num_shares (int): The total number of shares to create.
        threshold (int): The number of shares required to reconstruct the secret.

    Returns:
        list: A list of shares.
    """
    if not all(isinstance(arg, int) and arg > 0 for arg in [num_shares, threshold]):
        raise ValueError("Number of shares and threshold must be positive integers.")
    if threshold > num_shares:
        raise ValueError("Threshold cannot be greater than the number of shares.")
    if not secret_string:
        raise ValueError("Secret string cannot be empty.")
        
    return PlaintextToHexSecretSharer.split_secret(secret_string, threshold, num_shares)

def combine_shares(shares):
    """
    Recovers a secret from a list of shares.

    Args:
        shares (list): A list of shares.

    Returns:
        str: The recovered secret.
    """
    if not shares or not isinstance(shares, list) or not all(isinstance(s, str) for s in shares):
        raise ValueError("Shares must be a non-empty list of strings.")

    return PlaintextToHexSecretSharer.recover_secret(shares)

