# Skincare Timer App

## Getting started
1. Clone this repository (only this branch)

   ```bash
   git clone https://github.com/c-rose-g/SkincareTimerApp.git
   ```

2. Install dependencies

      ```bash
      pipenv install -r requirements.txt
      ```

3. Create a **.env** file based on the example with proper settings for your
   development environment
4. Make sure the SQLite3 database connection URL is in the **.env** file

5. Get into your pipenv, migrate your database, seed your database, and run your Flask app

   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   flask run
   ```



## Tech Stack

## Database

## Highlights
## Future Implementation Goals
- [ ] Routines
- [ ] Steps
- [ ] Premium account
- [ ] Connection to 3rd party devices
