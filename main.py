import tweepy

# Adicione as suas credenciais de desenvolvedor do Twitter aqui
consumer_key = 'SUA_CONSUMER_KEY'
consumer_secret = 'SUA_CONSUMER_SECRET'
access_token = 'SEU_ACCESS_TOKEN'
access_token_secret = 'SEU_ACCESS_TOKEN_SECRET'

# Configure a autenticação e criar uma instância da API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Buscar tweets com a palavra-chave "programação"
tweets = api.search(q='programação', count=100)

# Imprima os textos dos tweets encontrados
for tweet in tweets:
    print(tweet.text)
