Для запуска приложения необходимо установить и включить Docker Desktop последней версии 
Находясь в директории с Dockerfile запустить следующие команды: 
docker build -t myimage .
docker run -d --name mycontainer -p 8000:8000 myimage

Приложение принимает POST запросы по адресу localhost:8000/analyze/{text}
Документация доступная по localhost:8000/docs
