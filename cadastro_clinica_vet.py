# importanto bibliotecas
import tkinter as tk
from tkinter import Entry
from tkinter import ttk
import datetime as dt
import sqlite3
import pandas as pd

#criando listas
lista_tipos=["Cachorro","Cobra","Coelho","Gato","Hamster","Pássaro","Tartaruga"]

#criando conexão 
conexao = sqlite3.connect('cadastro_clientes.db')
c = conexao.cursor()
c.execute("""CREATE TABLE  clientes (
     nometutor text,
     endereco text,
     numero text,
     bairro text,
     cidade text,
     telefone text,
     pet text,
     raca text,
     especie text,
     idade text,
     peso text,
     castrado text
     )""")

conexao.commit()
conexao.close()

#definindo funções 
def cadastrar_cliente():
    conexao = sqlite3.connect('cadastro_clientes.db')
    c = conexao.cursor()
    
    c.execute("INSERT INTO clientes VALUES (:nometutor,:endereco,:numero,:bairro,:cidade,:telefone,:pet,:raca,:especie,:idade,:peso,:castrado)",
            {
                'nometutor': entry_nome.get(),
                'endereco': entry_rua.get(),
                'numero': entry_numero.get(),
                'bairro': entry_bairro.get(),
                'cidade': entry_cidade.get(),
                'telefone': entry_telefone.get(),
                'pet':entry_pet.get(),
                'raca': entry_raca.get(),
                'especie': entry_especie.get(),
                'idade' : entry_idade.get(),
                'peso': entry_peso.get(),
                'castrado': entry_castrado.get()
            })

    conexao.commit()
    conexao.close()

    #Apagar textos anteriores
    entry_nome.delete(0,"end")
    entry_rua.delete(0,"end")
    entry_numero.delete(0,"end")
    entry_bairro.delete(0,"end")
    entry_cidade.delete(0,"end")
    entry_telefone.delete(0,"end")
    entry_pet.delete(0,"end")
    entry_raca.delete(0,"end")
    entry_especie.delete(0,"end")
    entry_idade.delete(0,"end")
    entry_peso.delete(0,"end")
    entry_castrado.delete(0,"end")
    
def exportar_cliente():
    conexao = sqlite3.connect('cadastro_clientes.db')
    c = conexao.cursor()

    # Inserir dados na tabela:
    c.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados = c.fetchall()
    print(clientes_cadastrados)
    clientes_cadastrados=pd.DataFrame(clientes_cadastrados,columns=['nometutor','rua','numero','bairro','cidade','telefone','pet','raca','especie','idade','peso','castrado','id_banco'])
    clientes_cadastrados.to_excel("banco_clientess.xlsx")

    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

# criando interface gráfica
janela = tk.Tk()
janela.title("CADASTRO DE PACIENTES")

#Rotulo Entradas: 
label_descricao = tk.Label(text="CADASTRO")
label_descricao.grid(row=1,column=5,padx = 10, pady = 10, sticky="nswe",columnspan = 4)

label_nome = tk.Label(text="Nome do tutor")
label_nome.grid(row=2,column=0,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

label_endereco= tk.Label(text="Endereço - Rua")
label_endereco.grid(row=2,column=5,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

label_numero = tk.Label(text="Número")
label_numero.grid(row=2,column=9,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

label_bairro = tk.Label(text="Bairro")
label_bairro.grid(row=3,column=0,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

label_cidade= tk.Label(text="Cidade")
label_cidade.grid(row=3,column=5,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

label_telefone = tk.Label(text="Telefone")
label_telefone .grid(row=3,column=9,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

label_pet = tk.Label(text="Nome do animal")
label_pet.grid(row=4,column=0,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

label_raca = tk.Label(text="Raça")
label_raca.grid(row=4,column=5,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

label_especie = tk.Label(text="Especie")
label_especie.grid(row=4,column=9,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

label_idade = tk.Label(text="Idade")
label_idade.grid(row=5,column=0,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

label_peso = tk.Label(text="Peso")
label_peso.grid(row=5,column=5,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

label_castrado = tk.Label(text="Castrado")
label_castrado.grid(row=5,column=9,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

#Caixa Entrada

entry_nome= tk.Entry()
entry_nome.grid(row=2,column=3,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

entry_rua = tk.Entry()
entry_rua.grid(row=2,column=7,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

entry_numero = tk.Entry()
entry_numero.grid(row=2,column=11,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

entry_bairro = tk.Entry()
entry_bairro.grid(row=3,column=3,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

entry_cidade = tk.Entry()
entry_cidade.grid(row=3,column=7,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

entry_telefone  = tk.Entry()
entry_telefone .grid(row=3,column=11,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

entry_pet = tk.Entry()
entry_pet.grid(row=4,column=3,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

entry_raca = ttk.Combobox(values=lista_tipos)
entry_raca.grid(row=4,column=7,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

entry_especie = tk.Entry()
entry_especie.grid(row=4,column=11,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

entry_idade = tk.Entry()
entry_idade.grid(row=5,column=3,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

entry_peso =tk.Entry()
entry_peso.grid(row=5,column=7,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

entry_castrado = tk.Entry()
entry_castrado.grid(row=5,column=11,padx = 10, pady = 10, sticky="nswe",columnspan = 2)


#BOTAO CADASTRAR 
botao_cadastrar = tk.Button(text="CADASTRAR", command = cadastrar_cliente)
botao_cadastrar.grid(row=6,column=4,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

#BOTAO EXPORTAR
botao_exportar = tk.Button(text="EXPORTAR", command = exportar_cliente)
botao_exportar.grid(row=6,column=8,padx = 10, pady = 10, sticky="nswe",columnspan = 2)

janela.mainloop()