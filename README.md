# Corona Tracker

![Tableau Project](http://recordit.co/EjVb6fLw6u.gif)

This Project pulls daily Cornoavirus data from [this api](https://github.com/ExpDev07/coronavirus-tracker-api) and uploads it to a google sheets file. From the google sheets file, I use the data for multiple Tableau Visulizations. You can see my Tableau project [here](https://public.tableau.com/profile/chase.austin#!/vizhome/CoronavirusCOVID-19USCases/USMap). You can view my google sheet where I store my data [here.](https://docs.google.com/spreadsheets/d/1R1JiUvjdLMXHnt1S9tkUTFoYdy37tJVD1b-apvu711k/edit?usp=sharing) I call my python function every day from an EC2 instance using cloud watch triggers.

## Getting Started

**To setup your own tableau server for corona virus tracking, you will need to:**

- Obtain OAuth2 credentials from Google Developers Console
- Create Google Sheet
- Create AWS EC2 Instance
- Pull Repo on EC2
- Transfer OAuth2 Json Credentials
- Setup Install Packages
- Setup a Cron Job for EC2
- Setup AWS Lambda Function to Start/Stop EC2 Instance
- Install Tableau
- Link Tableau Data Source to Google Sheet

### Setup

1. [Obtain OAuth2 credentials from Google Developers Console](https://gspread.readthedocs.io/en/latest/oauth2.html)
2. [Create Google Sheet](https://www.google.com/sheets/about/) (I recomend scrolling to the bottom of the page and increasing the number of rows. My First data set was more than 100 rows, which is the default option)
3. [Create AWS EC2 Instance](https://medium.com/employbl/how-to-launch-an-ec2-instance-de568295205d)
4. [Pull Repo on EC2](https://medium.com/@sriteja95/login-to-aws-ec2-instance-and-clone-your-code-from-git-hub-repo-using-ubuntu-36fbf8bdc41b)
5. [Transfer OAuth2 JSON](https://github.com/juanfrans/notes/wiki/Copying-Files-Between-Local-Computer-and-Instance-(AWS))


6. Install Packages
```
sudo apt-get update
sudo apt-get upgrade python3 -y
sudo apt-install python3-pip -y
sudo apt-get install python3-venv -y
```

Setup Virutal Enviroment and install pip packages
```
python3 -m venv env
source env/bin/activate

pip3 install requests
pip3 install COVID19PY
pip3 install gspread
pip3 install --upgrade oauth2client
```
7. [Setup AWS Lambda Function to Start/Stop EC2 Instance](https://aws.amazon.com/premiumsupport/knowledge-center/start-stop-lambda-cloudwatch/)

8. Setup a Cron Job for EC2 (Run Script on instance start)

   - Stop instance
   - Select instance, then Actions, Instance Settings, View/Change User Data
   - Copy contents of userDataScript.txt into window
   - Select plain text and save

#### You should now pull data to your google sheets at the intervals you selected with AWS Cloud Watch

9. [Install Tableau](https://public.tableau.com/en-us/s/)
10. [Link Tableau Data Source to Google Sheet](https://public.tableau.com/en-us/s/resources) (Video number 3)

## Built With

* [COVID19Py](https://github.com/Kamaropoulos/COVID19Py) - @Kamaropoulos Coronavirus python API wrappet
* [gspread](https://github.com/burnash/gspread) -@burnash Python package for editing Google Sheets

## Authors

* **Chase Austin** - [GitHub](https://github.com/ChaseAustin/)

## Acknowledgments

* **jhu** - https://github.com/CSSEGISandData/COVID-19 - Worldwide Data repository operated by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE). 

* **csbs** - https://www.csbs.org/information-covid-19-coronavirus - U.S. County data that comes from the Conference of State Bank Supervisors.
