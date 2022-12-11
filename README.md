craetion of virtual environment

1--> pip install virtualenv
2--> creattion of virtualenv by assigning unique name 
`virtualenv envname`
        or
`python -m venv env`
3--> activation of virtualenv
`.\env\Scripts\activate.bat`
4--> building app upon the virtualenv i have made

2--> install all the packages and dependencies
`make requirements.txt file and enter all the packages and deps`
`pip install -r .\requirements.txt`


3-->github setup 
just put all my files will be uploaded to github
`git init`--> initialize and to start tracking our local code we are using this cd
`git add .`--> it will will add all our local code into a history of git 
`git commit -m "commit-name"` it will used for commiting the changes we have made into our code into github
`git branch -M branch-name`
`git remote origin <git_url>`
`git push origin branch-name`