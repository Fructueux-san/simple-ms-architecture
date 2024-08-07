import pika, json


def upload(f, fs, channel, access):
    try:
        fid = fs.put(f)
    except:
        return "Internal server error", 500

    message = {
            "video": str(fid),
            "mp3_fid": None,
            "username": access["username"],
    }

    try:
        channel.basic_publish(
                exchange="",
                routing_key="video",
                body=json.dumps(message),
                property=pika.BasicProperties(
                    delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                ),
        )
    except:
        fs.delete(fid)
        return "internal server error", 500


