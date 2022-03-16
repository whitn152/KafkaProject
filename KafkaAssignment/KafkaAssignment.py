from kafka import KafkaConsumer, KafkaProducer

def consumer(topic: str) -> None:
	consumer = KafkaConsumer(topic)
	for message in consumer:
		print(message)

def producer(topic: str, message: str) -> None:
	KAFKA_SERVER = 'localhost:9092'

	producer = KafkaProducer(boostrap_servers=KAFKA_SERVER)

	#binary_message = map(bin,bytearray(message))
	producer.send(topic, message)
	producer.flush()