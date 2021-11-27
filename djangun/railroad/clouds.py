import logging  # noqa
import os

AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

# boto 연결해서 생성해주는 거 하면 되는데... 일단 저쪽(AWS)에서 해줘야 할 일이 많음

"""
1. 이미지 만들기 - [x]
2. IAM 생성 - []
3. 권한 설정 및 과금설정 - []
4. 연결 - []
5. ssh 키 생성 후 다운로드 - key파일 모델에서 관리 - []
6. 테스트 - []
"""
