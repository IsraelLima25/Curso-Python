#coding: utf-8

import sqlite3

DATABASE = 'dados.sqlite'

def abrir_conexao(banco):
    con = sqlite3.connect(banco)
    return con, con.cursor()

# ------------------------------------------- 

class CategoriaDAO(object):

    def __init__(self):
        self.conexao = sqlite3.connect(DATABASE)
        self.cursor = self.conexao.cursor()        

    def criar_categoria(self, categoria):
        stmt = 'INSERT INTO categorias (descricao) VALUES (?)'        
        self.cursor.execute(stmt, (categoria.descricao,))
        self.conexao.commit()       
        categoria.id = self.cursor.lastrowid
        
    def carregar_categoria(self, categoria):
        stmt = 'SELECT id, descricao FROM categorias WHERE id = ?'
        self.cursor.execute(stmt, (categoria.id,))
        reg = self.cursor.fetchone()        
        if reg:
            categoria.descricao = reg[1]
        else:
            categoria.descricao = ''       

    def atualizar_categoria(self, categoria):
        stmt = 'UPDATE categorias SET descricao = ?  WHERE id = ?'       
        self.cursor.execute(stmt, (categoria.descricao, categoria.id))
        self.conexao.commit()   
        
    def excluir_categoria(self, categoria):
        stmt = 'DELETE FROM categorias WHERE id = ?'
        self.cursor.execute(stmt, (categoria.id,))
        self.conexao.commit()          
        
    def recuperar_todas_categorias(self):
        todas = []
        stmt = 'SELECT id, descricao FROM categorias ORDER BY descricao COLLATE NOCASE'
        con, cur = abrir_conexao(DATABASE)
        cur.execute(stmt)
        regs = cur.fetchall()
        for reg in regs:
            cat = Categoria()
            cat.id = reg[0]
            cat.descricao = reg[1]
            todas.append(cat)
        return todas
        
    def contar_coisas_dependentes(self):
        dependentes = {}
        stmt = 'SELECT categoria, count(*) FROM coisas GROUP BY categoria'
        con, cur = abrir_conexao(DATABASE)
        cur.execute(stmt)
        regs = cur.fetchall()
        for reg in regs:
            cat = reg[0]
            qtd = reg[1]
            dependentes[cat] = qtd
        return dependentes        
            
# ------------------------------------------- 

class Categoria(object):

    def __int__(self, id='', descricao=''):
        self.id = id
        self.descricao = descricao

    def criar(self):
        dao = CategoriaDAO()
        dao.criar_categoria(self)     
        
    def recuperar(self, id=''):
        if id != '':
            self.id = id
        dao = CategoriaDAO()
        dao.carregar_categoria(self)
        
    def atualizar(self):
        dao = CategoriaDAO()
        dao.atualizar_categoria(self)

    def excluir(self, id=''):
        if id != '':
            self.id = id
        dao = CategoriaDAO()
        dao.excluir_categoria(self)        
        self.id = ''
        self.descricao = ''
        
    def recuperar_todas(self):
        dao = CategoriaDAO()
        return dao.recuperar_todas_categorias()
        
    def contar_coisas_dependentes(self):
        dao = CategoriaDAO()
        return dao.contar_coisas_dependentes()
        
# ------------------------------------------- 

def recuperar_todas_coisas():
    todas = []
    stmt = 'SELECT coi.id, coi.nome, coi.utilidade, coi.valor, coi.categoria, cat.descricao'
    stmt += ' FROM coisas AS coi INNER JOIN categorias AS cat ON coi.categoria = cat.id'
    stmt += ' ORDER BY coi.nome COLLATE NOCASE'
    con, cur = abrir_conexao(DATABASE)
    cur.execute(stmt)
    regs = cur.fetchall()
    for reg in regs:
        coi = {'id':reg[0], 'nome':reg[1], 'utilidade':reg[2], 'valor':reg[3], 
            'categoria':reg[4], 'categoria_descricao':reg[5]}
        todas.append(coi)
    return todas   
    
def criar_coisa(nome, utilidade, valor, categoria):
    stmt = 'INSERT INTO coisas (nome, utilidade, valor, categoria) VALUES (?, ?, ?, ?)'
    con, cur = abrir_conexao(DATABASE)
    cur.execute(stmt, (nome, utilidade, valor, categoria))    
    con.commit()     
    novo_id = cur.lastrowid   
    return novo_id

def recuperar_coisa(id):   
    stmt = 'SELECT id, nome, utilidade, valor, categoria FROM coisas WHERE id = ?'
    con, cur = abrir_conexao(DATABASE)
    cur.execute(stmt, (id,))
    reg = cur.fetchone()        
    if reg:
        coi = {'id':reg[0], 'nome':reg[1], 'utilidade':reg[2], 'valor':reg[3], 'categoria':reg[4]}
    else:
        coi = {'id':'', 'nome':'', 'utilidade':'', 'valor':'', 'categoria':''}
    return coi
    
def atualizar_coisa(id, nome, utilidade, valor, categoria):
    stmt = 'UPDATE coisas SET nome = ?, utilidade = ?, valor = ?, categoria = ? WHERE id = ?'
    con, cur = abrir_conexao(DATABASE)
    cur.execute(stmt, (nome, utilidade, valor, categoria, id))
    con.commit()
    
def excluir_coisa(id):
    stmt = 'DELETE FROM coisas WHERE id = ?'
    con, cur = abrir_conexao(DATABASE)
    cur.execute(stmt, (id, ))
    con.commit()  

