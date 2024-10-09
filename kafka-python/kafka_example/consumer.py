from confluent_kafka import Consumer, KafkaException
from config import bootstrap_servers

consumer_config = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'test-group',  # Consumer 그룹 ID
    'auto.offset.reset': 'earliest',  # 가장 오래된 메시지부터 읽기
}

consumer = Consumer(consumer_config)

# 토픽 구독
consumer.subscribe(['my-topic'])

def consume_messages():
    try:
        while True:
            msg = consumer.poll(1.0)  # 메시지 폴링 (1초 대기)
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            else:
                print(f"Received message: {msg.value().decode('utf-8')} from topic: {msg.topic()}")

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()  # 종료 시 컨슈머 닫기

consume_messages()