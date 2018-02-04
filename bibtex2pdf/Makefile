SHELL := /bin/bash

# The directory of this file
DIR := $(shell echo $(shell cd "$(shell  dirname "${BASH_SOURCE[0]}" )" && pwd ))

# The users UID
UID_ := $(shell id -u)

VERSION ?= latest
IMAGE_NAME ?= bananafett/bibtex2pdf
CONTAINER_NAME ?= bibtex2pdf

# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help

help: ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help


# DOCKER TASKS
# Build the container
build: ## Build the container
	docker build --rm -t $(IMAGE_NAME) .

build-nc: ## Build the container without caching
	docker build --rm --no-cache -t $(IMAGE_NAME) .

run: ## Run container
	sudo docker run \
    -it \
    --rm \
    --name=$(CONTAINER_NAME) \
    --env UID_=$(UID_) \
    -v $(DIR)/bib.bibtex:/tmp/bib.bibtex \
    -v $(DIR)/data:/home/chrome/bibtex-downloads \
    $(IMAGE_NAME):$(VERSION) \
    bash -c "usermod -u $(UID_) chrome && su -c 'python /home/chrome/bibtex2pdf.py /tmp/bib.bibtex /home/chrome/bibtex-downloads' chrome"

stop: ## Stop a running container
	docker stop $(CONTAINER_NAME)

remove: ## Remove a (running) container
	docker rm -f $(CONTAINER_NAME)

remove-image-force: ## Remove the latest image (forced)
	docker rmi -f $(IMAGE_NAME):$(VERSION)

