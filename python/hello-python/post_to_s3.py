import json
import boto3
import uuid

def lambda_handler(event, context):
    # TODO implement
    #message = event["body"]
    message = "body hier ist die ergebnis"
    
    s3 = boto3.client('s3')
    bucket_name = 'hello-s3-20231025'
    file_name = str(uuid.uuid4()) + '.txt'
    file_content = message
    
    response = s3.put_object(
    Body=file_content,
    Bucket=bucket_name,
    Key=file_name,
    )
    
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('https://zz604sldm9.execute-api.eu-central-1.amazonaws.com/'+file_name)
    # }

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }



# import json
# import boto3
# import uuid

# def lambda_handler(event, context):
#     # Die JSON-Nachricht aus dem Event extrahieren
#     message = event["body"]
    
#     # Eine Verbindung zu Amazon S3 herstellen
#     s3 = boto3.client('s3')
    
#     # Bucket-Namen
#     bucket_name = 'hello-s3-20231025'
    
#     # Einen eindeutigen Dateinamen erstellen
#     file_name = str(uuid.uuid4()) + '.txt'
    
#     # Den Dateiinhalt festlegen
#     file_content = message
    
#     # Die Datei in Amazon S3 hochladen
#     response = s3.put_object(
#         Body=file_content,
#         Bucket=bucket_name,
#         Key=file_name,
#     )
    
#     # Die URL zur gerade hochgeladenen Datei erstellen
#     file_url = f'https://zz604sldm9.execute-api.eu-central-1.amazonaws.com/{file_name}'
    
#     # Das Response-Objekt zurückgeben
#     return {
#         'statusCode': 200,
#         'body': json.dumps({'url': file_url})
#     }






























# import json
# import boto3
# import uuid

# def lambda_handler(event, context):
#  
#     message = event["body"]
    
#     s3 = boto3.client('s3')
#     #bucket_name = 'hello-s3-20231025'
#     bucket_name = 'hello-s3-20231025'
#     file_name = str(uuid.uuid4()) + '.txt'
#     file_content = message
    
#     response = s3.put_object(
#     Body=file_content,
#     Bucket=bucket_name,
#     Key=file_name,
#     )
    
#     # return {
#     #     'statusCode': 200,
#     #     'body': json.dumps('https://zz604sldm9.execute-api.eu-central-1.amazonaws.com/'+file_name)
#     # }


#     return {
#         'statusCode': 200,
#         'body': json.dumps(message)
#     }