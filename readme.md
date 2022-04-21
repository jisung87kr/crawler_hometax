1. 이미지 빌드
```
docker build -t test-python .
```

2. 스크립트 실행
```
docker run -v "$PWD":/usr/src/app  test-python python3 hometax.py
```