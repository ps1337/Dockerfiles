SHELL := /bin/bash
VERSION ?= latest

# The directory of this file
DIR := $(shell echo $(shell cd "$(shell  dirname "${BASH_SOURCE[0]}" )" && pwd ))

IMAGE_NAME ?= bananafett/hopper
CONTAINER_NAME ?= hopper

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
	xhost +local:root && \ # Allow X forwarding
	sudo docker run \
	-d \
	--name $(CONTAINER_NAME) \
	-e DISPLAY=$DISPLAY \
	--cap-add=SYS_PTRACE \
	-v /tmp/.X11-unix:/tmp/.X11-unix:ro \
	-v $(DIR)/sharedFolder:/var/sharedFolder \
	--entrypoint /opt/hopper-v4/bin/Hopper \
	$(IMAGE_NAME):$(VERSION)

run-cracked: ## Run container with modified clock
	docker pull $(IMAGE_NAME):$(VERSION) && \
	xhost +local:root && \ # Allow X forwarding
	sudo docker run \
	-d \
	--name $(CONTAINER_NAME) \
	-e DISPLAY=$DISPLAY \
	--cap-add=SYS_PTRACE \
	-v /tmp/.X11-unix:/tmp/.X11-unix:ro \
	-v $(DIR)/sharedFolder:/var/sharedFolder \
	$(IMAGE_NAME):$(VERSION)

stop: ## Stop a running container
	docker stop $(CONTAINER_NAME)

remove: ## Remove a (running) container
	docker rm -f $(CONTAINER_NAME)

remove-image-force: ## Remove the latest image (forced)
	docker rmi -f $(IMAGE_NAME):$(VERSION)

