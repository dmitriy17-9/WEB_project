def convert_to_binary(filename):
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data