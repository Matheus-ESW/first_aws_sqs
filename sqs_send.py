import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Lendo URL da fila
QUEUE_URL = os.getenv('QUEUE_URL')

# Criando o cliente SQS
sqs = boto3.client('sqs')

# Enviando 49 mensagens
for i in range(1, 50):
    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=f'Mensagem número {i} para minha-fila-standard'
    )

    print(f"Mensagem {i} enviada com sucesso! ID: {response['MessageId']}")