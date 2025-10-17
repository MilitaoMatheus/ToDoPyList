import mysql.connector

conexao = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password= "12345678",
        database = "pylistdatabase"
    )