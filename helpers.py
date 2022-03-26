def get_id(url) -> int:
    """write a function that returns the id of a pokemon"""
    return int(url.split('/')[-2])
