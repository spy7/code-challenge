# Code Challenge package

Code Challenge package

# Installation

- Download the package and run the command below:

```console
python setup.py install
```

# Programming with the package

## Configurate connection

- Create a `Settings` object with connection settings.
- The example below shows default values.

```python
from code_challenge.api.settings import Settings

settings = Settings()
settings.host = "http://localhost:8000"
settings.endpoint = "graphql"
settings.token = "password"
```

## Create a service

```python
from code_challenge.api.graphql_reader import GraphQLReader
from code_challenge.services.company_service import CompanyService

reader = GraphQLReader(settings)
service = CompanyService(reader)
```

## Service methods

### Get companies

```python
companies = service.get_companies(sector, country)
```

- Get a list of companies using the optional `sector` and `country` filters.

### Get prices

```python
prices = service.get_prices(company, start_date, end_date)
```

- Get prices by a company using the optional `start_date` and `end_date` filters.
- The company object is received from the `get_companies` method.
- You can use a `ticker` string instead.

### Get recommendations

```python
recommendations = service.get_recommendations(company, start_date, end_date)
```

- Get recommendations by a company using the optional `start_date` and `end_date` filters.
- The recommendation is shown as a daily average.
- The company object is received from the `get_companies` method.
- You can use a `ticker` string instead.

### Add new companies

```python
from code_challenge.models.company import Company

companies = [Company(...)]
success = service.add_new_companies(companies)
```

- Add a list of new companies.

### Add prices

```python
from code_challenge.models.price import Price

prices = [Price(...)]
success = service.add_prices(company, prices)

# or

success = service.add_single_price(company, date, open, high, low, close, volume)
```

- Add a new price (or a list of prices) to the company.

### Add recommendations

```python
from code_challenge.models.recommendation import Recommendation

recommendations = [Recommendation(...)]
success = service.add_recommendation(company, recommendations)

# or

success = service.add_single_recommendation(company, date, firm, fromDate, toDate)
```

- Add a new recommendation (or a list of recommendations) to the company.

### Update price

```python
success = service.update_price(company, date, open, high, low, close, volume)
```

- Update prices for a company based on date.

# Using from the command line

- In the command line, call the `code_challenge` script followed by the command.

## Configurate connection

```console
code_challenge config --host http://localhost:8000 --endpoint graphql --token password
```

- Save settings to connect during the `get` methods.
- The configuration file is saved in the `~/.config/code_challenge` folder.

## Get companies

```console
code_challenge get_companies --sector "tech" --country "PT"
```

- Get a list of companies using the optional `sector` and `country` filters.

## Get prices

```
code_challenge get_prices "ticker" --start_date "2022-10-01" --end_date "2022-10-05"
```

- Get prices by a company using its ticker and the optional `start_date` and `end_date` filters.

## Get recommendations

```
code_challenge get_recommendations "ticker" --start_date "2022-10-01" --end_date "2022-10-05"
```

- Get recommendations by a company using its ticker and the optional `start_date` and `end_date` filters.
- The recommendation is shown as a daily average.
