import os
import boto3
from face_recognition_code import face_recognition_function

def handler(event, context):
    obj_k = event['Records'][0]['s3']['object']['key']
    s3 = boto3.client('s3')
    s3.download_file('1225466047-stage-1', obj_k, f"/tmp/{os.path.basename(obj_k)}.jpg")
    txtresult = face_recognition_function(f"/tmp/{os.path.basename(obj_k)}.jpg")
    s3.put_object(Key=f"{obj_k.split('.')[0]}.txt", Body=bytes(txtresult.encode('utf-8')), Bucket='1225466047-output')
    return "Success"
