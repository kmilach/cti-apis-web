import re

def validateIpAddress(ip: str) -> bool:
    '''
    Validates if the IP address is in the correct format
    :param ip: the IP address string
    :return: a boolean indicating if ip was valid or not
    '''
    ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    return bool(re.match(ip_pattern, ip))

def validateDomain(domain: str) -> bool:
    '''
    Validates if the domain name is valid
    :param domain: the domain string
    :return: a boolean indicating if domain was valid or not
    '''
    domain_pattern = r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(domain_pattern, domain))

def validateHash(hash_value: str) -> bool:
    '''
    Validates if the hash value is a valid MD5 or SHA256 hash
    :param hash_value: the hash string
    :return: a boolean indicating if hash_value was valid or not
    '''
    md5_pattern = r'^[a-fA-F0-9]{32}$'
    sha256_pattern = r'^[a-fA-F0-9]{64}$'
    return bool((re.match(md5_pattern, hash_value) or re.match(sha256_pattern, hash_value)))

def validateKey(key: str) -> bool:
    '''
    Validates if the key contains only lowercase letters and numbers
    :param key: the API key string
    :return: a boolean indicating if key was valid or not
    '''
    key_pattern = r'^[A-Za-z0-9]+$'
    return bool(re.match(key_pattern, key))