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
##### retreiving the data or code from git repository(any) 
`git clone <giturl>` 

## Mongodb account creation
<a href="https://account.mongodb.com/account/login?n=%2Fv2%2F6383752f26290660e06cd064&nextHash=%23metrics%2FreplicaSet%2F6383756aa00db149ac3c1cf1%2Fexplorer">Mongodb url login
</a><br>
1--> create new project<br>
    i) give new project name<br>
    ii)create project<br>
2--> Click on Build a database <br>
    i)shared database (righter most) <br>
    ii)last section named cluster change name to `sensor-database`<br>
    iii)give username and password<br>
    iv)ip address (Add my current ip address click)<br>
    v)Click on Finish and close<br>
3--->Connect <br>
    i)Connect to vscode<br>

### DUMP DATA TO MONGODB<br>
1-->download the data and store in local system<br>
2-->.env file and wrote all the credentials into it like url,name,dbname,coll name <br>
3-->data_mongo.py<br>
    i)-->we called the .env file and made its abject called EnvironmentVariable<br>
    ii)-->dataframe to json converted and from the we called the pymongo client and <br>
    then we pushed our complete data to mongodb<br>
    iii)--> we got all the data to mongodb-cloud in collections section <br>

### DATA INGESTION PIPELINE <br>
1--> `sensor` folder created <br>
2--> `components` consists of pipelines <br>
3--> `utils.py` it is for utility handling<br>
4-->`config.py` it is for configuration handling<br>
5-->`entity` folder consists of all the entities <br>


### DATA VAIDATION PIPELINE 
1-->drop_missing_values_columns
2-->is_required_columns_exists -> it validates all the data columns by comparing with base dataframe
3-->data_drift--> checking and validating hypothesis testing based on the 2 different dataframe
4-->intialization of the pipeline

### DATA TRANSFORMATION PIPELINE
Refer to notebook 5 experiments so we will take the best experiment value from that initialized notebook
1-->Robust scaler for handling outliers and simple imputer object with strategy contant and combining to Pipeline module
2-->applyng the SmoteTomek for oversampling the data target class
3--> Label encoder for my target 
4-->make npz i)-train.npz
             ii)-test.npz
            iii)-transformer.pkl
            iv)-targetencoder.pkl
Saving the seriallized object into artifacts folder

### DATA TRAINING PIPELINE
1-->transformed data from the `data transformation pipeline`
2-->XGBClassifier TAINING without HP tuning
3-->checking for overfitting for the model
4--> saving the serialized pkl object into artifacts directory

### MODEL EVALUATION PIPELINE
In this pipeline the main aim is to get the latest directory from the artifacts directory 
compare the previous model score with latest model score THATS IT

### MODEL PUSHER PIPELINE
This pipeline is responsible for storing the latest model,latest encoder file into `saved_models/counter/model/model.pkl`

### BATCH PREDICTION PIPELINE
According to the user input we can able to upload the `filename.csv` file in which we can able to predict the class of the batch data and save it as the local file.
