from application.model.entity.produto import Produto
import json

class ProdutoDAO:
    def __init__(self):
        self._listar_produtos = []

        with open('C:\\Users\\Meu Computador\\Documents\\P2LabProgInt\\products.json') as product_file: product_list = json.load(product_file)
        
        for product in product_list:
            self._listar_produtos.append(Produto(product['id'],product['name'],product['image'],product['oldPrice'],product['price'],product['description'],product['installments']['count'],product['installments']['value']))  
   
    def get_listar_Produtos(self):
        return self._listar_produtos




   