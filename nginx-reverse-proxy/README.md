# docker-nginx-reverse-proxy (Deprecated)
A simple nginx reverse proxy using the official nginx docker image with custom port support, so you don't need subdomains.

## Why?
Because you can. It simplifies the process of hosting multiple webapps contained in docker containers on one centralized nginx instance.

## How?

*  Clone this repo <:
*  Edit the file ``default.conf`` to fit your domain name (domain.tld).
*  Copy the file ``default.conf`` to create a new virtual host (let's say ``webapp.conf``). Edit the file to fit your needs. Settings that should be changed are marked in ``<`` and ``>``.
*  Edit the file ``nginx.conf`` to fit your needs.
*  Put your SSL/TLS files into the ``ssl`` folder
*  Edit the start script ``start.sh``:
    * Add your desired ports: Add ``-p <externalPort>:<internalPort> \``
    * Add the config to the container: ``-v $PWD/webapp.conf:/etc/nginx/conf.d/webapp.conf \``
    * Link the webapp container to nignx: ``--link webapp:webapp \``

## Notes
SSL/TLS is enabled by default and preconfigured for using letsencrypt. You can refer to the *.conf files to check the settings.
