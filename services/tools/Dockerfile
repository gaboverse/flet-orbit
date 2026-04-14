FROM python:3.11.5-slim-bookworm AS base

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN pip install --upgrade pip

RUN apt update &&\
    apt install -y git

RUN adduser flet

USER flet

WORKDIR /app

RUN pip install --upgrade pip

# target icons-browser
# https://github.com/flet-dev/flet/blob/main/sdk/python/examples/apps/icons_browser/main.py

# target controls-gallery
# https://github.com/flet-dev/gallery
