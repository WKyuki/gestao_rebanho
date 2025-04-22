import json
import uuid
import datetime
import cx_Oracle

# ======================== Banco de Dados =============================

def conectar_oracle():
    try:
        dsn = cx_Oracle.makedsn("localhost", 1521, service_name="xe")
        conn = cx_Oracle.connect(user="usuario", password="senha", dsn=dsn)
        return conn
    except Exception as e:
        print(f"Erro ao conectar no Oracle: {e}")
        return None

def criar_tabela(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE rebanho (
            id VARCHAR2(50) PRIMARY KEY,
            identificador VARCHAR2(50),
            raca VARCHAR2(50),
            data_nascimento DATE,
            sexo VARCHAR2(1),
            status VARCHAR2(20)
        )
        """)
        conn.commit()
    except cx_Oracle.DatabaseError as e:
        pass

def inserir_banco(conn, animal):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO rebanho VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5, :6)",
                       [animal['id'], animal['identificador'], animal['raca'],
                        animal['data_nascimento'], animal['sexo'], animal['status']])
        conn.commit()
    except Exception as e:
        print(f"Erro ao inserir: {e}")

# ======================== Funções principais =============================

rebanho = []

def registrar_animal():
    identificador = input("Identificador único: ")
    raca = input("Raça: ")
    data_nasc = input("Data de nascimento (YYYY-MM-DD): ")
    sexo = input("Sexo (M/F): ")
    animal = {
        "id": str(uuid.uuid4()),
        "identificador": identificador,
        "raca": raca,
        "data_nascimento": data_nasc,
        "sexo": sexo.upper(),
        "status": "Ativo",
        "historico": []
    }
    rebanho.append(animal)
    conn = conectar_oracle()
    if conn:
        inserir_banco(conn, animal)
        conn.close()

def listar_animais():
    for animal in rebanho:
        print(f"ID: {animal['id']} | Identificador: {animal['identificador']} | Raça: {animal['raca']}")

def registrar_evento():
    ident = input("Identificador do animal: ")
    evento = input("Descrição do evento: ")
    data = input("Data do evento (YYYY-MM-DD): ")
    for animal in rebanho:
        if animal['identificador'] == ident:
            animal['historico'].append({"evento": evento, "data": data})
            print("Evento registrado.")
            return
    print("Animal não encontrado.")

def exportar_json():
    with open("rebanho.json", "w") as f:
        json.dump(rebanho, f, indent=4)
    print("Exportado para rebanho.json")

def menu():
    while True:
        print("\n--- Gestão de Rebanho ---")
        print("1. Registrar novo animal")
        print("2. Listar animais")
        print("3. Registrar evento")
        print("4. Exportar para JSON")
        print("5. Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            registrar_animal()
        elif opcao == "2":
            listar_animais()
        elif opcao == "3":
            registrar_evento()
        elif opcao == "4":
            exportar_json()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    conn = conectar_oracle()
    if conn:
        criar_tabela(conn)
        conn.close()
    menu()