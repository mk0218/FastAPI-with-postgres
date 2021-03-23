# expert-potato
## 실행 방법
본 프로젝트는 docker compose를 이용해 세팅되었습니다.  
아래와 같이 api 서버와 db 서버를 한 번에 실행할 수 있습니다.
```
$ docker-compose up
```

## api 서버 접속
docker-compose.yml 파일에서 api 서버의 port는 12321로 세팅되어 있습니다.  
위와 같이 서버 실행 후, http://127.0.0.1:12321 로 접속하시면 됩니다.