from mastodon import Mastodon

mastodon = Mastodon(
	access_token = '',
	api_base_url = 'masto.es'
)

# Mensajes
mensaje = "¡Hola! Soy Roberto, el administrador de este servidor de Mastodon :mastodon: (https://masto.es)\n\nSi es tu primera vez en Mastodon, he preparado una guía para ayudarte a empezar 🙂 https://masto.es/@rober/109412552189056438 \n\nPuedes preguntarme lo que quieras si necesitas más ayuda. Sígueme para estar al tanto de las novedades sobre Mastodon y este servidor."

# Retomamos el id de la última notificación leída
try:
	file = open('last_id', 'r')
except FileNotFoundError:
	last_id = ""
else:
	last_id = file.read().rstrip("\n")
	file.close()

# Obtenemos las notificaciones
notifications = mastodon.notifications(since_id=last_id)
#notifications = mastodon.notifications(limit=1)
for n in notifications:
	# Ignoramos todo lo que no sea un registro
	if n['type'] == "admin.sign_up":
		user = "@" + n['account']['acct']
		mastodon.status_post(user + " " + mensaje, visibility="direct")
# Guardamos la notificación más reciente
file = open('last_id', 'w')
try:
	file.write(str(notifications[0]['id']))
except IndexError:
	file.write(last_id)
file.close()
