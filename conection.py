import psycopg2

sql_insercao_produtos = 'INSERT INTO produtos (descricao, volume, preco, estoque) VALUES (%s, %s, %s, %s)'
sql_busca_todos_produtos = 'SELECT * FROM produtos'

try:
    conn = psycopg2.connect(database="db-estoque",
                            host="localhost",
                            user="postgres",
                            password="123456",
                            port="5432")
    cursor = conn.cursor()

    #argumentos = ('Heineken Long Neck', 750, 12.00, 60)

    #cursor.execute(sql_insercao_produtos, argumentos)
    #conn.commit()

    cursor.execute(sql_busca_todos_produtos)
    lista = cursor.fetchall()

    for i in range(len(lista)):
        print('Código: ', lista[i][0])
        print('Descrição: ', lista[i][1])
        print('Volume (mL): ', lista[i][2])
        print('Preço: ', lista[i][3])
        print('Estoque: ', lista[i][4])
        print('\n')

except Exception as error:
    print("Erro ao conectar ou executar operação no banco de dados:", error)

finally:
    cursor.close()
    conn.close()
