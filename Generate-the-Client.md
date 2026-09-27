# Generate the Client

- Get the generator, check releases here https://github.com/OpenAPITools/openapi-generator/releases:
  ```shell
  export GENERATOR_VERSION=7.25.0
  wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/$GENERATOR_VERSION/openapi-generator-cli-$GENERATOR_VERSION.jar
  ```

- Copy the OpenAPI definition file from a [release](https://github.com/tkhamez/neucore/releases) from
  `web/application-api-3.yml` to `application-api-3.yml`, or fetch it from a running application, e.g.:
  ```shell
  wget https://account.bravecollective.com/application-api-3.yml
  ```

- Delete the `neucore_api` files and the `docs` directory:
  ```shell
  rm -R neucore_api docs
  ```

- Generate the client:
  ```shell
  java -jar openapi-generator-cli-$GENERATOR_VERSION.jar generate -i application-api-3.yml -g python -c openapi-config.json
  ```

- Add the directories `neucore_api` and `docs`:
  ```shell
  git add neucore_api docs
  ```

- Revert changes in `.gitignore`:
  ```shell
  git checkout .gitignore
  ```

- In `.openapi-generator/FILES`, delete any new lines that starts with `test/`.

- In `README.md`, undo all changes above `This Python package is automatically generated`.

- Commit everything:
  ```shell
  git add .
  git commit -a -m "Update client"
  ```
