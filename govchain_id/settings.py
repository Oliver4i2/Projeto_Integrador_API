DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'govchain_db',
        'USER': 'govchain_user',
        'PASSWORD': 'securepassword',
        'HOST': 'db',   # nome do serviço no docker-compose
        'PORT': '5432',
    }
}
