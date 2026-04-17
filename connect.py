import psycopg2
from config import load_config

def connect():
    """ PostgreSQL деректер қорына қосылу """
    config = load_config()
    conn = None
    try:
        # PostgreSQL серверіне қосылу
        print('PostgreSQL деректер қорына қосылуда...')
        conn = psycopg2.connect(**config)
        
        # Көрсеткіш (cursor) жасау
        cur = conn.cursor()
        
        # PostgreSQL нұсқасын тексеру (тест ретінде)
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(f'Сәтті қосылды! Деректер қорының нұсқасы: {db_version}')
        
        # Көрсеткішті жабу
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Қосылу кезінде қате шықты: {error}")
    finally:
        if conn is not None:
            conn.close()
            print('Деректер қорымен байланыс үзілді.')

if __name__ == '__main__':
    connect()