# 프로젝트 셋업 및 실행 가이드
## 1. 실행 방법
본 프로젝트는 docker compose를 이용해 세팅되었습니다.  
아래의 명령어로 api와 db 컨테이너를 한 번에 실행할 수 있습니다.
```
docker-compose up
```
처음 실행시 Dockerfile을 빌드하며 requirements.txt에 등록된 패키지들을 api 컨테이너에 설치합니다.  
만약 requirements.txt의 의존성 목록이 변경되었다면,
```
docker-compose up --build
```
--build 플래그를 붙여 다시 빌드해주어야 합니다.
  
## 2. API 서버
docker-compose.yml 파일에서 API 서버의 port는 8000번으로 세팅되어 있습니다.  
http://127.0.0.1:8000 에서 API 서버의 응답을 확인할 수 있습니다.

### 2.1. API documentation
FastAPI에서는 두 가지의 자동 API documentation을 제공합니다.  
* Interactive API docs - http://127.0.0.1:8000/docs
* Alternative API docs - http://127.0.0.1:8000/redoc
  
## 3. Database 세팅
데이터베이스 파일이 저장되는 디렉토리는 .gitignore에 등록되어 있습니다.  
따라서 새로 테이블을 생성하고 데이터를 불러와야 합니다.

### 3.1. Migration
만들어져 있는 SQLAlchemy Model로부터 DB table을 생성합니다.  
alembic이라는 migration tool을 이용했습니다.  
우선 Revision을 생성합니다.
```
docker-compose exec api alembic revision -m "initial" --autogenerate
```
api/migrations/versions 디렉토리에 5763893ccd26_initial.py 같은 이름의 파일이 생성됩니다.  
Revision이 오류 없이 잘 이루어졌으면 migration을 할 수 있습니다.
```
docker-compose exec api alembic upgrade head
```

### 3.2. Table 불러오기
지정된 이름의 파일로부터 데이터를 가져옵니다.  
(현재 여기부터 미구현입니다.)