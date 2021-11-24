Djangun PaaS project
====================

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/pydanny/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Github Actions status](https://github.com/binaryeast/djangun.com/actions/workflows/ci.yml/badge.svg)](https://github.com/binaryeast/djangun.com/actions/workflows/ci.yml)

장건 - All-in-one 코딩 플랫폼 프로젝트.

* AWS 기반 PaaS 플랫폼
* 게이미피케이션 유저 프로필 - 레벨 업, 랜덤박스?
* 한글 프리셋 설정된 리눅스 서버 - 한글화 셸?
* 쉬운 버전 관리 - [gitless?](https://github.com/gitless-vcs/gitless)
* 더 편한 프로젝트 관리 - PERT/CPM, 간트차트, 칸반보드, 권한...
* 효율 높고 질 좋은 강의 - 동영상(유튜브), 위키?

장건은 코딩에 입문하고 싶거나 서비스를 만들어보고 싶은 초보자와, 부수입을 창출하고 싶은 개발자들에게 교육, 프로젝트 관리, 정보 공유, 클라우드 서버 대여를 한 곳에서 할 수 있게 제공해주는 웹 플랫폼이다.

우리 제품은 Github, 구름IDE, AWS, 인프런과 달리 한 곳에서 강의, 자료, 클라우드 서버, 수익 연결(광고, 구독, 후원, 출간, 판매), 서비스 런칭을 모두 제공하며, 유저는 게임처럼 레벨을 올리고 무료&할인 보상을 획득하며 성장할 수 있다.


![image](docs/djangun.jpg)

설명
--------

* AWS lightsail(클라우드 서버, VPS)
  + 우분투 20.04
* 파이썬
  + django 웹 앱 프레임워크
  + cookiecutter-django (Docker 옵션)
  + cellery queue
* 도커
  + docker-compose
  + traefik - Reverse proxy (Web server)
  + node front-side build - SASS
  + aws-cli - SES, S3, ...etc
  + Mailhog - 이메일 전송 기능 테스트

Settings
--------

Moved to
[settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

Basic Commands
--------------

### Docker-compose Commands

#### Build the Stack

This can take a while, especially the first time you run this particular
command on your development system:

    $ docker-compose -f local.yml build

Generally, if you want to emulate production environment use
production.yml instead. And this is true for any other actions you might
need to perform: whenever a switch is required, just do it!

#### Run the Stack

This brings up both Django and PostgreSQL. The first time it is run it
might take a while to get started, but subsequent runs will occur
quickly.

Open a terminal at the project root and run the following for local
development:

    $ docker-compose -f local.yml up

You can also set the environment variable COMPOSE\_FILE pointing to
local.yml like this:

    $ export COMPOSE_FILE=local.yml

And then run:

> \$ docker-compose up

To run in a detached (background) mode, just:

    $ docker-compose up -d

Execute Management Commands \~\~\~\~\~\~\~\~\~\~\~\~\~

As with any shell command that we wish to run in our container, this is
done using the docker-compose -f local.yml run \--rm command:

    $ docker-compose -f local.yml run --rm django python manage.py migrate

    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out
    the form. Once you submit it, you\'ll see a \"Verify Your E-mail
    Address\" page. Go to your console to see a simulated email
    verification message. Copy the link into your browser. Now the
    user\'s email should be verified and ready to go.
-   To create an **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and
your superuser logged in on Firefox (or similar), so that you can see
how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy djangun

### Test coverage

To run the tests, check your test coverage, and generate an HTML
coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with py.test

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS
compilation](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html).

### Celery

This app comes with Celery.

To run a celery worker:

``` {.sourceCode .bash}
cd djangun
celery -A config.celery_app worker -l info
```

Please note: For Celery\'s import magic to work, it is important *where*
the celery commands are run. If you are in the same folder with
*manage.py*, you should be right.

### Email Server

In development, it is often nice to be able to see emails that are being
sent from your application. For that reason local SMTP server
[MailHog](https://github.com/mailhog/MailHog) with a web interface is
available as docker container.

Container mailhog will start automatically when you will run all docker
containers. Please check [cookiecutter-django Docker
documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html)
for more details how to start all containers.

With MailHog running, to view messages that are sent by your
application, open your browser and go to `http://127.0.0.1:8025`

### Sentry

Sentry is an error logging aggregator service. You can sign up for a
free account at <https://sentry.io/signup/?code=cookiecutter> or
download and host it yourself. The system is setup with reasonable
defaults, including 404 logging and integration with the WSGI
application.

You must set the DSN url in production.

Deployment
----------

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker
documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
