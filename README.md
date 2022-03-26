# 가상 환경 만들기 (venv)

### 1. venv로 가상환경 생성
- `$ python3 -m venv <venv>`
```bash
# ex
$ python3 -m venv venv
```

### 2. 가상환경 활성화
- `$ source <venv>/bin/activate`
``` bash
# ex
$ source venv/bin/activate
```

### 가상환경 비활성화
- `deactivate`

<br>

# pip 기본 사용법
- `$ pip --version` : 설치된 pip 버전 확인
- `$ pip install pip --upgrade` : pip 업그레이드
- `$ pip install 패키지이름` : 패키지 설치
- `$ pip install "패키지이름~=3.0.0` : 3.0.0 버전의 패키지 설치
- `$ pip freeze` : 설치된 패키지 확인
- `$ pip freeze > requirements.txt` : requirements.txt 파일에 설치된 패키지 기록
- `$ pip install -r requirements.txt` : requirements.txt 파일에 기록된 패키지 설치