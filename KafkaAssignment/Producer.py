from kafka import KafkaProducer
import sys
import json

def producer(topic: str, message: str) -> None:

	producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
	producer.send(topic, message)
	producer.flush()

def main(message: str) -> None:
	topic = 'test'
	producer(topic, message)

if __name__ == '__main__':
	main(sys.argv[1])