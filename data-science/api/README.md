`unzip data.zip`  
**Запуск**  
`cd webapp/`  
`sudo docker image build -t app_docker .`  
`sudo docker run -p 5050:5000 -d app_docker`  

**Переходим по адресу в браузере**  
http://localhost:5050/





