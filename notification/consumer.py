
import pika, sys, os, time
from send import email


def main():
    #rabbitmq connection
    rabbit_credentials = pika.PlainCredentials('local', 'thelocaluserpassword')
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq", 5672, '/', credentials=rabbit_credentials))
    channel = connection.channel()

    def callback(ch, method, properties, body):
        err = email.notification(body)
        if err:
            ch.basic_nack(delivery_tag=method.delivery_tag)
        else:
            ch.basic_ack(delivery_tag=method.delivery_tag)
    channel.basic_consume(
            queue=os.environ.get("MP3_QUEUE"),
            on_message_callback=callback
        )
    print("Waiting for messages. Press ctrl + C to exit")
    channel.start_consuming()

if __name__ == "__main__":
    try:
        print("Notification consumer start")
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
