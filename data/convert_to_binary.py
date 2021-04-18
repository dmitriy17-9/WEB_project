def convert_to_binary(filename: str) -> bytes:
    """
    Любой файл кодирует в байты
    :param filename: str
    :return: bytes
    """
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


def write_to_file(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)