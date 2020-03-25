# Corona Tracker

This Project pulls daily Cornoavirus data from this api and uploads it to a google sheets file. From the google sheets file, I use the data for multiple Tableau Visulizations. You can see my tableau project here.
I call my python function every day from an EC2 instance using cloud watch triggers.

## Getting Started

**To setup your own tableau server for corona virus tracking, you will need to:**

- Obtain OAuth2 credentials from Google Developers Console
- Create Google Sheet
- Create AWS EC2 Instance
- Pull repo
- Setup a virtual enviroment
- Setup AWS Lambda Function to Start/Stop EC2 Instance
- Install Tableau
- Link Tableau Data Source to Google Sheet

### Setup

1. [Obtain OAuth2 credentials from Google Developers Console](https://gspread.readthedocs.io/en/latest/oauth2.html)
2. [Create Google Sheet](https://www.google.com/sheets/about/) (I recomend scrolling to the bottom of the page and increasing the number of rows. My First data set was more than 100 rows, which is the default option)
3. [Create AWS EC2 Instance](https://medium.com/employbl/how-to-launch-an-ec2-instance-de568295205d)
4. [Pull this repo](https://medium.com/@sriteja95/login-to-aws-ec2-instance-and-clone-your-code-from-git-hub-repo-using-ubuntu-36fbf8bdc41b)
5. [Transfer OAuth2 JSON](https://github.com/juanfrans/notes/wiki/Copying-Files-Between-Local-Computer-and-Instance-(AWS))
6. Setup a virtual enviroment
```
python3 -m venv env
source env/bin/activate
```
7. Install Packages
```
pip install COVID19PY
pip install datetime
pip install gspread
pip install time
```
8. [Setup AWS Lambda Function to Start/Stop EC2 Instance](https://aws.amazon.com/premiumsupport/knowledge-center/start-stop-lambda-cloudwatch/)
9. [Install Tableau](https://public.tableau.com/en-us/s/)
10. [Link Tableau Data Source to Google Sheet](resources) (Video number 3)

## Built With

* [COVID19Py](https://github.com/Kamaropoulos/COVID19Py) - @Kamaropoulos Coronavirus python API wrappet
* [gspread](https://github.com/burnash/gspread) -@burnash Python package for editing Google Sheets

## Authors

* **Chase Austin** - [GitHub](https://github.com/ChaseAustin/)

## Acknowledgments

* **jhu** - https://github.com/CSSEGISandData/COVID-19 - Worldwide Data repository operated by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE). 

* **csbs** - https://www.csbs.org/information-covid-19-coronavirus - U.S. County data that comes from the Conference of State Bank Supervisors.
