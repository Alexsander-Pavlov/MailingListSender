import os


def find_env(name_env: str) -> str:
    env = os.environ.get(name_env)
    if env is not None:
        return env
    print(f'Warning env with name {name_env} is return None, '
          'check you .env or envshell')
