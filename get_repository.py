from flask import Flask, request, jsonify
import git
import os

app = Flask(__name__)


def clone_repo_from_github(clone_url):
    print(f'Cloning: {clone_url}')
    git.Git('/var/www').clone(clone_url)


def pull_repo_from_github(repo_path):
    print(f'Pulling: {repo_path}')
    g = git.cmd.Git(repo_path)
    g.pull()


@app.route('/', methods=['POST', 'GET'])
def received_data_from_github():
    data = request.json
    repo = data.get('repository', {})
    clone_url = repo.get('clone_url', None)
    name = repo.get('name', '')


