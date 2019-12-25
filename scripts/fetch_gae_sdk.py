language: python
sudo: required
dist: xenial
python: "3.7"

before_install:
  - openssl aes-256-cbc -K $encrypted_XXX_key -iv $encrypted_XXX_iv -in credentials.tar.gz.enc -out credentials.tar.gz -d
  - tar -xzf credentials.tar.gz
  - mkdir -p lib

install:
  - pip install -r requirements.txt
  - pip install -r requirements-for-testing.txt

script:


deploy:
  provider: gae
  skip_cleanup: true # Skip cleanup so api_key.py and vendored dependencies are still there
  keyfile: client-secret.json
  project: project-name
  default: true  # default project app version
