import psycopg2
from config import load_config

def search_contacts(pattern):
    """1. Паттерн бойынша іздеу функциясын шақыру"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
                rows = cur.fetchall()
                print(f"\n🔍 Іздеу нәтижесі ('{pattern}'):")
                for row in rows:
                    print(f"ID: {row[0]}, Аты: {row[1]}, Тел: {row[2]}")
    except Exception as error:
        print(f"Қате: {error}")

def upsert_contact(name, phone):
    """2. Қосу немесе жаңарту процедурасын шақыру"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("CALL upsert_contact(%s, %s);", (name, phone))
                conn.commit()
                print(f"✅ Контакт сәтті қосылды/жаңартылды: {name}")
    except Exception as error:
        print(f"Қате: {error}")

def get_paginated(limit, offset):
    """3. Пагинация функциясын шақыру"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
                rows = cur.fetchall()
                print(f"\n📖 Беттегі мәліметтер (Limit: {limit}, Offset: {offset}):")
                for row in rows:
                    print(row)
    except Exception as error:
        print(f"Қате: {error}")

def delete_contact(identifier):
    """4. Өшіру процедурасын шақыру"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("CALL delete_contact(%s);", (identifier,))
                conn.commit()
                print(f"🗑️ Контакт өшірілді: {identifier}")
    except Exception as error:
        print(f"Қате: {error}")

if __name__ == '__main__':
    # ТЕКСЕРУ ҮШІН (Мәліметтерді өзгертіп көрсең болады):
    
    # 1. Жаңа адам қосу
    upsert_contact('Damir', '87015554433')
    
    # 2. Іздеп көру
    search_contacts('Damir')
    
    # 3. Пагинацияны тексеру (мысалы, алғашқы 5 адам)
    get_paginated(5, 0)
    
    # 4. Өшіру (тексергің келсе астындағыны аш)
    # delete_contact('Damir')