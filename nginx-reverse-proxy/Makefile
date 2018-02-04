SHELL := /bin/bash

# The directory of this file
DIR := $(shell echo $(shell cd "$(shell  dirname "${BASH_SOURCE[0]}" )" && pwd ))

# The users UID
UID_ := $(shell id -u)

VERSION ?= latest
IMAGE_NAME ?= bananafett/nginx-reverse-proxy
CONTAINER_NAME ?= nginx-reverse-proxy

# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help

help: ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

run: ## Run container
	sudo docker run \
	--name $(CONTAINER_NAME) \
	-p 80:80 \
	-v $(PWD)/nginx.conf:/etc/nginx/nginx.conf \
	-v $(PWD)/default.conf:/etc/nginx/conf.d/default.conf \
	-v $(PWD)/nginx-root:/usr/share/nginx \
	-v $(PWD)/nginx-root/html:/etc/nginx/html \
	-v $(PWD)/ssl:/etc/nginx/ssl \
	-d \
	nginx:$(VERSION)


stop: ## Stop a running container
	docker stop $(CONTAINER_NAME)

remove: ## Remove a (running) container
	docker rm -f $(CONTAINER_NAME)

remove-image-force: ## Remove the latest image (forced)
	docker rmi -f $(IMAGE_NAME):$(VERSION)

