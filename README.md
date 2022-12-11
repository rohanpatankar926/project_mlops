### CREATION OF VIRTUALENV<br>

1--> pip install virtualenv<br>
2--> creattion of virtualenv by assigning unique name <br>
`virtualenv envname`<br>
        or
`python -m venv env`<br>
3--> activation of virtualenv<br>
`.\env\Scripts\activate.bat`<br>
4--> building app upon the virtualenv i have made<br>

2--> install all the packages and dependencies<br>
`make requirements.txt file and enter all the packages and deps`<br>
`pip install -r .\requirements.txt`<br>


## GITHUB SETUP <br>

just put all my files will be uploaded to github and also for pushing local code to github<br>
`git init`--> initialize and to start tracking our local code we are using this cd<br>
`git add .`--> it will will add all our local code into a history of git <br>
`git commit -m "commit-name"` it will used for commiting the changes we have made into <br>
our code into github<br>
`git branch -M branch-name`<br>
`git remote origin <git_url>`<br>
`git push origin branch-name`<br>


retreiving the data or code from git repository(any) 
`git clone <giturl>` 


### DUMP DATA TO MONGODB<br>
1-->download the data and store in local system<br>
2-->.env file and wrote all the credentials into it like url,name,dbname,coll name <br>
3-->data_mongo.py<br>
    i)-->we called the .env file and made its abject called EnvironmentVariable<br>
    ii)-->dataframe to json converted and from the we called the pymongo client and <br>
    then we pushed our complete data to mongodb<br>
    iii)--> we got all the data to mongodb-cloud in collections section <br>