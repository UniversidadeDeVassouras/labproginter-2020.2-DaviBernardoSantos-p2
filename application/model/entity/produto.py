class Produto:
    def __init__(self, id, nome, imagem, preço_antigo, preço, descriçao, parcela,var_parcela):
        self._id = id
        self._nome = nome
        self._imagem = imagem
        self._preço_antigo = preço_antigo
        self._preço = preço
        self._descriçao = descriçao
        self._parcela = parcela
        self._var_parcela = var_parcela


    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome  

    def get_imagem(self):
        return self._imagem

    def get_preço_antigo(self):
        return self._preço_antigo

    def get_preço(self):
        return self._preço

    def get_descriçao(self):
        return self._descriçao

    def get_parcela(self):
        return self._parcela

    def get_var_parcela(self):
        return self._var_parcela