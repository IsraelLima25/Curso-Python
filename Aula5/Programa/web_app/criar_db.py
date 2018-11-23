#coding: utf-8

import sqlite3

stmt_categorias = '''
    CREATE TABLE categorias (
        id INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE ,
        descricao VARCHAR NOT NULL
    )
'''

stmt_coisas = '''
    CREATE TABLE coisas (
        id INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE ,
        nome VARCHAR NOT NULL,
        utilidade VARCHAR,
        valor FLOAT,
        categoria INTEGER
    )
'''

connection = sqlite3.connect('dados.sqlite')
cursor = connection.cursor()
cursor.execute(stmt_categorias)
cursor.execute(stmt_coisas)
