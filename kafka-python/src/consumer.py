from confluent_kafka import Consumer, KafkaError
from sqlalchemy.orm import Session
from src.database import SessionLocal
from src.model import StockData
from src.config import settings


# Kafka Consumer 설정
consumer_config = {
    'bootstrap.servers': settings.bootstrap_servers,  # Kafka 클러스터 주소
    'group.id': 'fastapi-stock-reader-group',        # Consumer 그룹 ID
    'auto.offset.reset': 'earliest',        # 처음부터 메시지 읽기 설정; ["earlist", "latest", "none"]
    'enable.auto.commit': False             # 자동 커밋 활성화
    # 'auto.commit.interval.ms': 5000
    # 'fetch.min.bytes': 1                  # 브로커에서 컨슈머로 전달할 수 있는 메시지의 최소 크기
    # 'fetch.max.wait.ms': 500
    # 'heartbeat.interval.ms': 3000         # 컨슈머가 주기적으로 그룹 코디네이터에 살아있다는 신호 보내는 시간간격
    # 'session.timeout.ms':  10000
    # 'max.poll.records': 500
    # 'max.poll.interval.ms': 300000
    # 'isolation.level': "read_committed"
    # 'partition.assignment.strategy': "roundrobin"
    # 'client.id': "uniq-id-fastapi"
}

consumer = Consumer(consumer_config)
consumer.subscribe(['stock_data'])  # Kafka의 'stock_data' 토픽 구독

# 메시지를 DB에 저장하는 함수
def save_to_db(db: Session, message: dict):
    stock_data = StockData(
        symbol=message['symbol'],
        open_price=message['open_price'],
        volume=message['volume'],
        timestamp=message['timestamp']
    )
    db.add(stock_data)
    db.commit()

# Kafka 메시지 소비 및 데이터베이스 저장
def consume_messages():
    db = SessionLocal()  # DB 세션 생성
    try:
        while True:
            msg = consumer.poll(1.0)  # 1초 대기 후 메시지 가져오기
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f"Error: {msg.error()}")
                    break
            
            # 메시지 디코딩 및 DB 저장
            message = msg.value().decode('utf-8')
            print(f"Received message: {message}")
            
            # 메시지를 JSON 형태로 파싱 (Kafka로부터 받은 메시지)
            import json
            parsed_message = json.loads(message)
            
            # DB에 저장
            save_to_db(db, parsed_message)

            # 수동 커밋
            consumer.commit()
    
    except Exception as e:
        print(f"Error consuming messages: {e}")
    
    finally:
        consumer.close()
        db.close()


###TODO: Consumer strategy update


if __name__ == "__main__":
    consume_messages()