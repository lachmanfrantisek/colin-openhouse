![PyPI](https://img.shields.io/pypi/v/colin-openhouse.svg)
![PyPI - License](https://img.shields.io/pypi/l/colin-openhouse.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/colin-openhouse.svg)
![PyPI - Status](https://img.shields.io/pypi/status/colin-openhouse.svg)

# Colin OpenHouse checks

Additional checks for colin -- the cintainer linter.



# Create your image with apache (htttpd) and check it with the colin:

```
$ pip3 install https://github.com/user-cont/colin
$ pip3 install colin-openhouse
```

```
$ sudo /usr/local/bin/colin -r openhouse my-image
OPENHOUSE:
ok :passed:fedora_base
nok:failed:fedora_parent
   -> Use fedora:27 as a parent image
   -> Use `FROM image:tag` to specify base image. (Needs to be first instruction.) Použij `FROM obraz:tag` pro určení obrazu, na kterém budeme stavět. (Je třeba zadat jako první instrukci).
   -> https://fedoraproject.org/wiki/Container:Guidelines#env
nok:failed:maintainer_label_required
   -> Label 'maintainer' has to be specified.
   -> Use `LABEL labelname=labelvalue` for specifying label. Pro vytvoření labelu (=štítku) použij `LABEL klic=hodnota`.
   -> https://fedoraproject.org/wiki/Container:Guidelines#LABELS
nok:failed:env_var_password
   -> Environment variable 'password' has to be specified and should be set to `secret`.
   -> Use `ENV labelname=labelvalue` for specifying label. Pro vytvoření labelu (=štítku) použij `LABEL klic=hodnota`.
   -> https://fedoraproject.org/wiki/Container:Guidelines#env
nok:failed:httpd_installed
   -> Package httpd has to be isntalled (dnf install -y httpd).
   -> Use RUN for running a command inside an image. Použij RUN pro spuštění příkazu v obraze.
   -> https://docs.docker.com/engine/reference/builder/#copy
nok:failed:workdir
   -> Working directory has to be set to /var/www/html
   -> Use `WORKDIR /my/path` for specifying working directory. Pro zadání pracovního adresáře použij `WORKDIR /moje/cesta`.
   -> https://fedoraproject.org/wiki/Container:Guidelines#workdir
nok:failed:file_copy
   -> Package httpd has to be isntalled.
   -> To copy a file into image, use `COPY source destination`. Pro vkládání souborů do kontejnerového obrazu použij příkaz`COPY zdroj cíl`
   -> https://docs.docker.com/engine/reference/builder/#copy
nok:failed:cmd_entrypoint
   -> You should set /usr/sbin/httpd as an ENTRYPOINT and set CMD to ["-D", "FOREGROUND"] to run in it in the foreground.
   -> Use `ENTRYPOINT` for startup command and CMD for specifying its parameters.Použij ENTRYPOINT pro zadání příkazu spouštěného při startu kontejneru a CMD pro zadání jeho parametrů.
   -> https://fedoraproject.org/wiki/Container:Guidelines#workdir
nok:failed:port80
   -> Expose the port 80.
   -> Use EXPOSE 12345 to inform docker about port of your service.Použij EXPOSE 12345 pro informování dockeru o portu služby.
   -> https://fedoraproject.org/wiki/Container:Guidelines#expose
```
