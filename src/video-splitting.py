import os
import time
import boto3
import subprocess


def video_splitting_cmdline(video_filename):
    filename = os.path.basename(video_filename)
    out_file = os.path.splitext(filename)[0] + ".jpg"
    out_dest = os.path.join("/tmp", out_file)

    split_cmd = f'/opt/ffmpeg -i "{video_filename}" -vframes 1 {out_dest}'

    try:
        subprocess.check_call(split_cmd, shell=True)
    except subprocess.CalledProcessError as e:
        print(e.returncode)
        print(e.output)

    return out_dest


def lambda_handler(event, context):
    object_key = event['Records'][0]['s3']['object']['key']
    s3 = boto3.client('s3')
    s3.download_file('1225319303-input', object_key, f"/tmp/{object_key}")
    out_dest = video_splitting_cmdline(f"/tmp/{object_key}")
    s3.upload_file(out_dest, '1225319303-stage-1', os.path.basename(out_dest))
