def convert_to_binary(filename: str) -> bytes:
    """
    Любой файл кодирует в байты
    :param filename: str
    :return: bytes
    """
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data