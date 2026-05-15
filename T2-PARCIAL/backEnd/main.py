from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)


class produto(BaseModel):
    nome_produto: str
    valor_produto: float
    unidade_produto: str
    quantidade_produto: float

class apagar_Item(BaseModel):
    apagar_item: str

def usar_banco(comando,valor=None):
    try:
        config = {
            'host':'127.0.0.1',
            'user':'root',
            'password':'93g@Fvk7fdc',
            'database':'banco_produto'
        }

        conexao = mysql.connector.connect(**config)
        cursor = conexao.cursor()

        if valor != None:
            cursor.execute(comando,valor)
            conexao.commit()
            print('Adicionado com sucesso!')
        
        elif valor == None:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(comando)
            lista_produto = cursor.fetchall()
            return lista_produto[::-1]
            
            

    except mysql.connector.Error as erro:
        print(f'Erro ao conectar: {erro}')

    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()
            print(" Conexão encerrada.")


@app.post("/salvar-produto")
def test(dados: produto):
    print('teste')
    valores = (dados.nome_produto, dados.valor_produto, dados.unidade_produto, dados.quantidade_produto)
    print(valores)
    comando = 'INSERT INTO produto(nome,valor,unidade,quantidade) VALUES(%s,%s,%s,%s);'
    usar_banco(comando, valores)

@app.get('/listar')
async def listar_produtos():
    comando = 'SELECT * FROM produto;'
    dados = usar_banco(comando)
    return dados

@app.post('/apagar')
def apagarItem(dados: apagar_Item):


    print('apagar')
    lista = usar_banco('SELECT * FROM produto')

    produto_existente = next((linha for linha in lista if linha['nome'] == dados.apagar_item), None)

    
    if produto_existente:
        comando = 'delete from produto where id = %s;'
        usar_banco(comando,(produto_existente['id'],))
        


    