# kafka_study

## kafka 실행

- `.env.example`과 동일하게 `.env` 생성
- `docker network create kafka-network`
- `docker compose up`
- grafana/prometheus 파일 접근 문제의 경우, `init.sh` 참고

## 실행방법 (python)

### 1. pyenv & poetry install

#### Ubuntu

- zsh를 쓰시면 `~/.bashrc` 대신 `~/.zshrc`를 사용하세요!

```(bash)
// pyenv
sudo apt update
sudo apt-get install build-essential python-tk python3-tk tk-dev  zlib1g-dev libffi-dev libssl-dev libbz2-dev libreadline-dev libsqlite3-dev liblzma-dev libncurses-dev
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc 
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc 
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc

pyenv install 3.12
(pyenv global 3.12.7) // optional, 로컬로 사용하려면 pyenv local (버전명)

//poetry
curl -sSL https://install.python-poetry.org | python -
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

#### Mac (brew)

- for bashrc user check: https://github.com/pyenv/pyenv?tab=readme-ov-file#set-up-your-shell-environment-for-pyenv

```(bash)
brew update & brew install pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc

pyenv install 3.12
(pyenv global 3.12.7) // optional, 로컬로 사용하려면 pyenv local (버전명)

curl -sSL https://install.python-poetry.org | python -
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### 2. 패키지 설치하기

```(bash)
cd kafka-python & poetry install
poetry shell
```

- to check venv path: `poetry env info -p`

### 3. fastapi 실행

- `.env` 파일 생성
  
    ```(shell)
    OPEN_OASIS_KEY=
    ALPHA_VANTAGE_KEY=
    ```

- /kafka-python 폴더내 (src와 동일 레벨) /log 폴더 생성
- `./entrypoint.sh` or `sh entrypoint.sh`
- application을 시작하면 scheduler 동작함
