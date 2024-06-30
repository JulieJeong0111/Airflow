import cx_Oracle
import logging

# 설정된 DB 연결 정보
DB_Connection = {
    'host': 'localhost',
    'port': '1521',
    'user': 'system',
    'password': 'pass',
    'database': 'xe'
}

# 로그 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

def get_connection():
    dsn = cx_Oracle.makedsn(
        DB_Connection['host'],
        DB_Connection['port'],
        sid=DB_Connection['database']
    )
    try:
        connection = cx_Oracle.connect(
            user=DB_Connection['user'],
            password=DB_Connection['password'],
            dsn=dsn
        )
        logger.info('Oracle DB 연결 성공')
        return connection
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        logger.error(f'Oracle DB 연결 실패: {error.message}')
        raise

# 연결 함수 호출
try:
    connection = get_connection()
    # 여기서부터 원하는 작업 수행
    # 예시: connection.cursor()를 사용하여 쿼리 실행 등
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM EMPLOYEES ')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
except Exception as e:
    logger.error(f'작업 중 오류 발생: {str(e)}')