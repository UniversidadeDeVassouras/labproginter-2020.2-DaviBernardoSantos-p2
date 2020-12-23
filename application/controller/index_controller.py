from flask import render_template, request
from application import app 
from application.model.entity.produto import Produto
from application.model.dao.produto_dao import ProdutoDAO




@app.route("/")
def index():
    listaProdutos = ProdutoDAO().get_listar_Produtos()
    return render_template("index.html", listaProdutos = listaProdutos)