from confluent_kafka import Producer
from config import bootstrap_servers
import time

# Kafka Producer 설정
producer_config = {
    'bootstrap.servers': bootstrap_servers,
    'message.max.bytes': 104857600
}

producer = Producer(producer_config)

# 전송 완료 콜백 함수
def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def send_messages(topic, num_messages):
    for i in range(num_messages):
        message = f'Message {i}'
        producer.produce(topic, message.encode('utf-8'), callback=delivery_report)
        producer.poll(1)  # 메시지 전송 후 폴링하여 콜백 함수 실행
        time.sleep(1)  # 메시지 전송 간격 (1초)

    producer.flush()  # 모든 메시지가 전송될 때까지 대기

# 토픽명과 메시지 수를 지정하여 메시지 전송
# send_messages('my-topic', 10)