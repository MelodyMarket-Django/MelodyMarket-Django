import os
from pathlib import Path
import environ
from rest_framework import serializers
from .models import ReviewLike


env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent

env.read_env(os.path.join(BASE_DIR, '.env'))

<<<<<<< HEAD
# # SECRET_KEY 설정 변경
# SECRET_KEY = env("SECRET_KEY")

# # DATABASES 설정 변경
# DATABASES = {
#     "default": env.db(),
# }
=======
SECRET_KEY = env('SECRET_KEY')
DATABASES = {
    'default': env.db(),
}
>>>>>>> 7fbf496 (노래, 리뷰, 장르, 좋아요 모델 추가)


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "account",
    "playlist",
    "subscription",
    "review",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ko-kr"
TIME_ZONE = "Asia/Seoul"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

<<<<<<< HEAD
AUTH_USER_MODEL = "account.User"
=======
# ReviewLike 모델의 Serializer를 정의

class ReviewLikeSerializer(serializers.ModelSerializer):
    # 리뷰에 해당하는 노래의 평균 평점을 나타내는 필드
    song_average_rating = serializers.SerializerMethodField()

    class Meta:
        # ReviewLike 모델을 기반으로 Serializer를 정의
        model = ReviewLike
        # Serializer에 필드들을 정의
        fields = ['id', 'user', 'review', 'song_average_rating']

    # 리뷰에 해당하는 노래의 평균 평점을 가져오는 메서드
    def get_song_average_rating(self, obj):
        # 리뷰에 해당하는 노래
        song = obj.review.song
        # 노래가 존재하는 경우 노래의 평균 평점을 반환, 존재하지 않는 경우 None
        return song.average_rating() if song else None
>>>>>>> 7fbf496 (노래, 리뷰, 장르, 좋아요 모델 추가)
