instalacion para el backend
 pip install -r requirements.txt
  sudo apt install redis-server
Luego de instalar verifica que está activo con: sudo systemctl status redis 
debe decirte: Active: active (running)

abrir otra ventana en la terminal y escribir lo siguiente:

paso1 (levantar Celery): celery worker -A app.celery --loglevel=info


en otra ventana debes exportar la variable:
echo "export FLASK_APP=idsapp.py" >> ~/.profile
Debes cerrar sesión y volver a iniciarla para que tome los cambios.
para verificar:  echo $FLASK_APP 

luego puedes levantar el paso 1 y paso dos

Paso 1: levantar Celery
Paso 2: Levantar flask usando: flask run








Repeticion:

primero escribir estos dos comandos: python3 -m venv venv

luego: source venv/bin/activate eso para levantar el entorno virtual, en tu consola aparecera adelante (venv)

instalacion para el backend pip install -r requirements.txt sudo apt install redis-server Luego de instalar verifica que está activo con: sudo systemctl status redis debe decirte: Active: active (running)

ahora debemos exportar la variable "idsapp"

echo "export FLASK_APP=idsapp.py" >> ~/.profile

Debes cerrar sesión y volver a iniciarla para que tome los cambios. para verificar: echo $FLASK_APP

luego puedes levantar el paso 1 y paso dos

Paso 1: celery worker -A app.celery --loglevel=info

Paso 2(en otra ventana): Levantar flask usando: flask run
