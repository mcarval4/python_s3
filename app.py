import boto3
import csv

# Criar conexão com o S3
session = boto3.Session(
  aws_access_key_id=''
  aws_secret_access_key=''
  region_name=''
)

s3 = session.resource('s3')

# Obter o bucket que contém as informações necessárias
bucket = s3.Bucket('[NOME DO BUCKET]') # bucket_exemplo 

# Obter os arquivos dentro do bucket (objetos)
obj = bucket.Object(key='') # pasta1/exemplo.csv

# Obter o arquivo
response = obj.get()

# Realizar a leitura do conteúdo dos arquivos
lines = response['Body'].read()

# Salvar o conteúdo do arquivo em um novo arquivo .csv
with open('test.csv', 'wb') as file:
  file.write(lines)