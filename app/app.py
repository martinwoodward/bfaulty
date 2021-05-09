#!/bin/python3

import json
import os, sys
import time
import datetime
from azure.storage.blob import BlobServiceClient
from sensors import sensors
from camera import camera
from specimen import specimen
from azuploader import azuploader

if __name__ == "__main__":
    print("Starting growlab-bfaulty")

    config = {}
    try:
        with open("/home/pi/bfaulty/app/config.json") as f:
            config = json.loads(f.read())
    except Exception as e:
        sys.stderr.write("Error: {}".format(e))
        sys.exit(1)

    print("Loaded config, saving images every {} seconds to {}".format( config["images"]["interval_seconds"], config["images"]["output_directory"]))

    sensors = sensors()
    readings = sensors.get_readings()

    print(readings)

    cam = camera(config["images"])
    frame = cam.get_frame()

    ts = time.time()
    pwd = "/home/pi/bfaulty/app" #os.getcwd()
    output_path = pwd + "/html"
    image_path = output_path + "/{}/{}/{}/bfaulty_{}.jpg".format(datetime.datetime.fromtimestamp(ts).strftime('%Y'),datetime.datetime.fromtimestamp(ts).strftime('%m'),datetime.datetime.fromtimestamp(ts).strftime('%d'),datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))
    data_path = output_path + "/{}/{}/bfaulty_{}.csv".format(datetime.datetime.fromtimestamp(ts).strftime('%Y'),datetime.datetime.fromtimestamp(ts).strftime('%m'),datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d'))
    index_image_path = "{}/image.jpg".format(output_path)
    preview_image_path = "{}/preview.jpg".format(output_path)
    index_path = "{}/index.html".format(output_path)

    try:
       os.makedirs(os.path.dirname(image_path), exist_ok=True)
    except:
       pass

    spec = specimen(config["text"], config["images"])
    spec.save_image(image_path, frame, readings)

    try:
        with open(data_path, "a") as myfile:
            myfile.write("{},{:05.2f},{:0.2f},{:05.2f},{:05.2f},{:0.2f},{:0.2f}\n".format(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%dT%H:%M:%SZ'), readings["temperature"], readings["pressure"], readings["humidity"], readings["soil0"], readings["lux"], readings["colourTemp"]))
    except:
       pass

    spec.save_image(index_image_path, frame, readings)
    spec.save_html(index_image_path, output_path, readings)

    uploader = azuploader(config["upload"]["connection_string"], output_path)

    uploader.upload(image_path)
    #uploader.upload(data_path)
    uploader.upload(preview_image_path)
    uploader.upload(index_path)
    uploader.upload(index_image_path)



