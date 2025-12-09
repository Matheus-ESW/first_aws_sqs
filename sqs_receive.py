import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Lendo a URL da fila
QUEUE_URL = os.getenv('QUEUE_URL')

# Criando o cliente SQS
sqs = boto3.client('sqs')

print("Iniciando leitura da fila...")

while True:
    response = sqs.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=10,  # máximo permitido por chamada
        WaitTimeSeconds=10      # long polling
    )

    # Se não houver mensagens, encerra o loop
    if 'Messages' not in response:
        print("Fila vazia. Todas as mensagens foram lidas.")
        break

    for message in response['Messages']:
        print(f"Mensagem recebida: {message['Body']}")

        # Excluindo a mensagem da fila após o processamento
        sqs.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=message['ReceiptHandle']
        )

        print(f"Mensagem excluída: ID {message['MessageId']}")