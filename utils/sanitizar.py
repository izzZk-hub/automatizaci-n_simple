import unicodedata

def sanitizar(texto):

    texto = texto.lower().strip()

    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')

    texto = texto.replace("ñ", "n")

    return texto