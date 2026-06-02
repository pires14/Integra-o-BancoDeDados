# Import do framework flask
# Import do render_template para ler o HTML
# request para capturar os dados
from flask import Flask, render_template, request

import mysql.connector 

# Cria conexão com o mySQL
bd_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'escola',
    'database': 'cadastro1'
}

# Biblioteca mysql.connector conecta o Python com o MySQL
