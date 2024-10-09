from confluent_kafka import Producer, TopicPartition, KafkaError
from src.config import settings
import json

# Kafka Producer 설정
producer_config = {
    'bootstrap.servers': settings.bootstrap_servers,
    'message.max.bytes': 104857600,
    # 'compression.type': 'gzip'  # 압축 유형 설정 (gzip, snappy, lz4, zstd)
    # 'partitioner': 'sticky'  # 스티키 파티셔너를 활성화
    # 'acks': 'all'  # 중복 없는 메시지 전송을 위해 'acks=all' 설정
    # 'enable.idempotence': True  # Idempotent Producer 활성화
    # 'retries': 5  # 메시지 전송 실패 시 재시도 횟수
    # 'transactional.id': 'my-transactional-id'  # 트랜잭셔널 프로듀서 활성화
}

producer = Producer(producer_config)

# 전송 완료 콜백 함수
def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def produce_message(topic: str, message: dict):
    """
    Kafka로 메시지 전송 함수
    :param topic: Kafka 토픽 이름
    :param message: 전송할 메시지 (딕셔너리 형태)
    """
    try:
        # Kafka로 메시지 전송
        ###TODO: JSON serializer update
        # https://github.com/confluentinc/confluent-kafka-python/blob/master/examples/json_producer.py
        serialized_message = json.dumps(message).encode('utf-8')
        producer.produce(topic, value=serialized_message, callback=delivery_report)
        producer.flush()  # 전송 대기 중인 메시지를 처리

    except Exception as e:
        print(f"Error producing message to Kafka: {e}")


###TODO: produce message only once
def produce_message_only_once(topic: str, message: dict):
    pass


###TODO: produce message with different partitioning
def produce_message_with_key(topic: str, message: dict, key: str):
    pass


###TODO: produce message with transaction
def produce_message_transaction(topic: str, message: dict):
    pass


###TODO: asyncio producer
# https://github.com/confluentinc/confluent-kafka-python/blob/master/examples/asyncio_example.py