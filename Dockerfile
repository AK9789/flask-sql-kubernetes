FROM python:3.8 
ARG USERNAME=princess
ARG USER_UID=1000
ARG USER_GID=$USER_UID
WORKDIR /app
# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME
RUN python -m pip install --upgrade pip
RUN pip install flask
RUN python -m pip install mysql-connector-python
COPY . /app
USER $USERNAME
EXPOSE 5000
CMD ["python","-m","flask","run","--host=0.0.0.0"]