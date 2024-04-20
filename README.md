# kpk ![last commit](https://img.shields.io/github/last-commit/zobweyt/kpk) ![license](https://img.shields.io/github/license/zobweyt/kpk)

kpk is a movie database web service. It is an open-source project, allowing all of the community's members to contribute and see their code live in action. 

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#key-features">Key Features</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#contribution">Contribution</a></li>
  </ol>
</details>



## Key Features
* Manage movies and reviews.
* Leave reviews for movies.
* Configure admins via the control panel.



## Getting started

Clone the repository:
```sh
git clone https://github.com/zobweyt/kpk.git
```

Install common project dependencies locally:
```sh
pip install -r requirements/common.txt
```

Create an `.env` file in the root directory and configure the environment variables:
```dotenv
SECRET_KEY="SECRET_KEY"
SQLALCHEMY_DATABASE_URI="sqlite:///db.sqlite3"
```

Create a superuser:
```sh
flask create-superuser <username> <password> <email>
```

Finally, run the website:
```sh
flask --debug run
```

## Contribution

Feel free to open an issue, contribute or suggest new ideas to improve this repository!

Install project dependencies required for development locally:
```sh
pip install -r requirements/dev.txt
```

Before committing, run static analysis tools in the project root directory:
```sh
black .
```