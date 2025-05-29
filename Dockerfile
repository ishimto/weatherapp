FROM python:3.12-slim AS build-req
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install uv
COPY ./web_app/requirements.txt .
RUN uv pip install -r requirements.txt



FROM python:3.12-slim AS run-app
COPY --from=build-req /opt/venv /opt/venv
RUN useradd --create-home nonroot
RUN chown -R nonroot:nonroot /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
USER nonroot
COPY ./web_app /web_app
WORKDIR /web_app
CMD gunicorn -b 0.0.0.0:8000 wsgi:app  --access-logfile - # for k8s pod stdout, remove 
