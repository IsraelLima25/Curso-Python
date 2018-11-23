#coding: utf-8

import os

from flask import Flask, render_template, request, redirect

import model

DIR_BASE = os.path.join(os.path.dirname(__file__), 'view')
app = Flask(__name__, template_folder=DIR_BASE)

# ------------------------------------------- 

@app.route('/')
@app.route('/inicial/')
def inicial():
    print(DIR_BASE.format('inicial.html'))
    return render_template('inicial.html')

# ------------------------------------------- 

@app.route('/categorias/')
def lista_categorias(retorno=''):    
    cats = model.Categoria().recuperar_todas()
    deps = model.Categoria().contar_coisas_dependentes()
    return render_template('lista_categorias.html', qtd=len(cats), categorias=cats, dependentes=deps)
    
@app.route('/categoria/', methods=['GET', 'POST'])
@app.route('/categoria/<id>', methods=['GET', 'POST'])
def categoria(id=''):
    cat = model.Categoria()
    if request.method == 'GET':
        if id != '':
            cat.recuperar(id)
        return render_template('categoria.html', categoria=cat)
    else: # method == POST
        if request.form['descricao'].strip() != '':            
            if id != '':
                cat.id = id
                cat.descricao = request.form['descricao'].strip()
                cat.atualizar()
            else:
                cat.descricao = request.form['descricao'].strip()
                cat.criar()                
        return redirect('/categorias/')

@app.route('/categoria_excluir/<id>', methods=['GET'])
def categoria_excluir(id=''):
    if id != '':
        cat = model.Categoria()
        cat.id = id
        cat.excluir()
    return redirect('/categorias/')

# ------------------------------------------- 

@app.route('/coisas/')
def lista_coisas():
    cois = model.recuperar_todas_coisas()     
    return render_template('lista_coisas.html', qtd=len(cois), coisas=cois)

@app.route('/coisa/', methods=['GET', 'POST'])
@app.route('/coisa/<id>', methods=['GET', 'POST'])
def coisa(id=''):
    if request.method == 'GET':
        cats = model.Categoria().recuperar_todas() 
        if id != '':
            coi = model.recuperar_coisa(id)
        else:
            coi = {'id':'', 'nome':'', 'utilidade':'', 'valor':'', 'categoria':''}
        return render_template('coisa.html', coisa=coi, categorias=cats)
    else: # method == POST
        nome = request.form['nome'].strip()
        utilidade = request.form['utilidade'].strip()
        valor = request.form['valor'].strip()
        if valor != '':
            valor = float(valor)
        else:
            valor = 0.0
        categoria = request.form['categoria']
        if nome != '' and categoria != '':
            if id != '':
                model.atualizar_coisa(id, nome, utilidade, valor, categoria)
            else:
                model.criar_coisa(nome, utilidade, valor, categoria)
        return redirect('/coisas/')    

@app.route('/coisa_excluir/<id>', methods=['GET'])
def coisa_excluir(id=''):
    if id != '':
        model.excluir_coisa(id)
    return redirect('/coisas/')

# ------------------------------------------- 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
