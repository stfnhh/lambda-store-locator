# AWS Lambda Store Locator

[![GitHub Stars](https://img.shields.io/github/stars/Mullen/store-locator.svg)](https://github.com/Mullen/store-locator/stargazers) [![GitHub Issues](https://img.shields.io/github/issues/Mullen/store-locator.svg)](https://github.com/Mullen/store-locator/issues) [![Current Version](https://img.shields.io/badge/version-0.1.0-green.svg)](https://github.com/Mullen/store-locator)

This is a Python store locator for [AWS Lambda](https://aws.amazon.com/lambda/) powered by [Chalice](https://github.com/aws/chalice/) and [SQLite](https://sqlite.org/).

Brought to you by the developers at [MullenLowe](https://us.mullenlowe.com).


## Setup

```shell
$ yum install sqlite-devel # CentOS, RHEL
$ apt-get install libsqlite3-dev # Debian, Ubuntu
```

## Usage
After you clone this repo, go to its root directory and run `pip install -r requirements.txt` to install its dependencies.

Once the dependencies are installed, you can run  `chalice local` to start the application. You will then be able to access it at localhost:8000/locations/*02201*

To add your own locations edit the *locations* table in `chalicelib/database.db`, the only column required for this to function is postcode.

## Development and contributing

Feel free to send pull requests and raise issues.

## License
>You can check out the full license [here](https://github.com/Mullen/lambda-store-locator/blob/master/LICENSE.md)

This project is licensed under the terms of the **MIT** license.
