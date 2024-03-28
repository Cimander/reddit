from decouple import config

print(config('SECRET_KEY'))
print(config('DEBUG'))
print(config('POSTGRES_DB'))
print(config('POSTGRES_USER'))
print(config('POSTGRES_PASSWORD'))
print(config('POSTGRES_HOST'))
print(config('POSTGRES_PORT'))
print(config('USE_S3'))
