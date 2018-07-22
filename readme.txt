1. Ensure docker and docker-compose are present on the machine

2. copy the contents in the .env.deploy file in an .env file, and fit in the required fileds

3. (optional) for development, change the port mapping in the docker-compose.yml file under the nginx service to "8000:8000", and set DEBUG=True WebPlumbing/settings.py

4. docker-compose build && docker-compose up (sudo may be required to run the commands)

