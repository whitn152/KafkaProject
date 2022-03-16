from kafka import KafkaConsumer

def consumer(topic: str) -> None:
	consumer = KafkaConsumer(topic)
	for message in consumer:
		print(message)

def main() -> None:
	topic = 'test'
	consumer(topic)

if __name__ == '__main__':
	main()