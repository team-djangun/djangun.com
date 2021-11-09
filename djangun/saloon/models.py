from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel

User = get_user_model()


# 게시판 - 스레드 | 갤러리 / 언어별, 프레임워크별, 구인, 프로젝트 홍보, 후기, 잡담.
# 위키 - 노션 | django-wiki
# 문서 - 포스트 | gitbook
# 템플릿 - 강좌 | 사용기?


