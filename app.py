import hvac 
import sys
import os

if __name__ == "__main__":
	print("############## INICIANDO VAULT ##############")
	client = hvac.Client(url=os.environ['VAULT_ADDR'], token='contra')
	regis = client.is_authenticated()
	if regis:
		print("############## USUARIO INICIADO CORRECTAMENTE ##############")
	else:
		print("############## USUARIO NO ENCONTRADO ##############")
	key = "este"
	secreto = "secretoPrueba"
	hvac_secret = {
		key: secreto,
	}
	print("############## GUARDANDO SECRETO ##############")
	client.secrets.kv.v2.create_or_update_secret(
	    path='hvac',
	    secret=dict(hvac_secret),
	)
	print("############## LEYENDO SECRETO ##############")
	read_response = client.secrets.kv.read_secret_version(path='hvac')
	print(read_response['data']['data'][key])
	exit
