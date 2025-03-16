import json
import boto3
import uuid
from datetime import datetime

# Criar clientes da AWS
comprehend = boto3.client('comprehend')
s3 = boto3.client('s3')

# Nome do bucket S3
BUCKET_NAME = "sentiment-analysis-logs"

def lambda_handler(event, context):
    try:
        # Printar o evento recebido para depuração
        print("Evento recebido:", json.dumps(event, indent=2))

        # Verificar se o evento já está no formato JSON correto
        if isinstance(event, dict) and "text" in event:
            body = event  # Evento já está no formato esperado
        elif "body" in event:
            body = json.loads(event['body'])  # Evento veio via API Gateway
        else:
            return {"statusCode": 400, "body": json.dumps({"error": "'body' não encontrado no evento."})}

        # Verificar se o texto foi fornecido
        text = body.get("text", "")
        if not text:
            return {"statusCode": 400, "body": json.dumps({"error": "Texto não fornecido."})}

        # Detectar idioma
        lang_response = comprehend.detect_dominant_language(Text=text)
        language = lang_response['Languages'][0]['LanguageCode']
        print(f"Idioma detectado: {language}")

        # Verificar se o idioma é suportado
        supported_languages = ['en', 'es', 'fr', 'de', 'it', 'pt', 'ja', 'ko']
        if language not in supported_languages:
            return {"statusCode": 400, "body": json.dumps({"error": "Idioma não suportado."})}

        # Análise de sentimento
        sentiment_response = comprehend.detect_sentiment(Text=text, LanguageCode=language)
        print(f"Resposta do Comprehend: {sentiment_response}")

        # Preparar o resultado
        sentiment = sentiment_response["Sentiment"]
        sentiment_score = sentiment_response["SentimentScore"]

        result = {
            "text": text,
            "language": language,
            "sentiment": sentiment,
            "confidence": sentiment_score,
            "timestamp": datetime.utcnow().isoformat()
        }

        # Salvar no S3
        file_name = f"sentiment_logs/{uuid.uuid4()}.json"
        s3.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=json.dumps(result))
        print(f"Resultado salvo no S3: {file_name}")

        # Retornar a resposta com o resultado da análise
        return {"statusCode": 200, "body": json.dumps(result)}

    except Exception as e:
        print(f"Erro: {str(e)}")
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
