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


### DATA VAIDATION PIPELINE <br>
1-->drop_missing_values_columns<br>
2-->is_required_columns_exists -> it validates all the data columns by comparing with base dataframe<br>
3-->data_drift--> checking and validating hypothesis testing based on the 2 different dataframe<br>
4-->intialization of the pipeline<br>

### DATA TRANSFORMATION PIPELINE<br>
Refer to notebook 5 experiments so we will take the best experiment value from that initialized notebook<br>
1-->Robust scaler for handling outliers and simple imputer object with strategy contant and combining to Pipeline module<br>
2-->applyng the SmoteTomek for oversampling the data target class<br>
3--> Label encoder for my target <br>
4-->make npz i)-train.npz<br>
             ii)-test.npz<br>
            iii)-transformer.pkl<br>
            iv)-targetencoder.pkl<br>
Saving the seriallized object into artifacts folder<br>

### DATA TRAINING PIPELINE<br>
1-->transformed data from the `data transformation pipeline`<br>
2-->XGBClassifier TAINING without HP tuning<br>
3-->checking for overfitting for the model<br>
4--> saving the serialized pkl object into artifacts directory<br>

### MODEL EVALUATION PIPELINE<br>
In this pipeline the main aim is to get the latest directory from the artifacts directory <br>
compare the previous model score with latest model score THATS IT<br>

### MODEL PUSHER PIPELINE<br>
This pipeline is responsible for storing the latest model,latest encoder file into `saved_models/counter/model/model.pkl`<br>

### BATCH PREDICTION PIPELINE<br>
According to the user input we can able to upload the `filename.csv` file in which we can able to predict the class of the batch data and save it as the local file.





data ingestion

1.collect from db to local gather 
2.data validation-->dropping the m.v,outlier detectioon,missmatch 
3.data transformation-->
data bricks--> spark
azure ml studio
sagemaker 
gcp deeplearning studio

1--->simple impute +robust scaler +smote analysis

for eve
ry pieplien we have i/p and o/p 

di->output -->complete data
dv--> i/p -> complete data o/p-->valdiated data
dt-> i/p-->validated data o/p->transformed data
dm-> i/p->transformed o/p-->model score and test and train score


for every particular training we will keep track of model.pkl

1-train-->99%-->model.pkl
2-train--95% -->model.pkl
3-train-->94% -->model.pkl
4-train-->99.5%-->modedl

1 train acc <2nd accuracy --> 1accuracy

train acc-0.9 test acc 0.8 diff 0.1 ---> rejecting the model which is overfitted
train accc 0.9 test acc 0.95 -> 0.05 --> false --> continue the pipeline 

loaded numpy array of train and test which was generated from data tranformation
sopliited the data as dep adn independent
fit the data on xgb
y_hat=model.pred(x_test)
f1_score(y_train,y_test)


-->training we got pickle file,f1_score train va,f1score test value

model.pkl


model resolver method

<!-- artifacts---> datatime--> data ingestion
           datatime-->  data validation -->


            datatime-->data trans  --> tranformed object ,pipeline object ,label encoder obj.pkl
           datatime-->  data training  --> output model.pkl

model resolver to evaluate our pipeline

1stime time training
we need to take the latest training artifacts and then store that artifacts traiend one inside the new directors saved_models dir

2nd time training
i will compare with the latest model directory of artifact and compare the models with saved_model-dir the delete the previous model and then or copy the atifacts generated model and then paste to saved_model_dir

artifacts/datetime/all the outputs

datetime --- .
    first list all the directories of artifacts

20230101
20230202
20230303

get the maximum value of the data director
convert the sting to int and then get th e maximum no of that

get_latest_model_path

saved_model/0/all the pickle files
saved_model/1/all the pickle files
saved_model/2/all the pickle files


it will just take all the particular model from artifacts that too latest one and then save that model to my saved_model directory in terms of counterwise

artifcats/latest_dir/models --> latest_model

saved_models/0 -> previous model
saved_model/1 ---> previous models

saved_model/2--> new_model



software:v1 
ci.cd 


software  --> push to github --> ftrom github git action will trigger and the steps will take place and will deploy the complete app to the target saved

        ,v2,v3





sync--->collect data --> preprocessing->transformation->model building --> model saving --> success message --->email 

echo "success"
Email opera

pythonoperator and bash operator

wanted to send local data to cloud s3 bucket 

aws s3 sync local_dir to s3_bucket 
aws s3 s3://data/data to data/

iam roles in aws
aws data center
mumbai s1 s2 s3 s4-->ap-south-1
kolkatta
osaka 
usa 
ohio
identity and  access management  global ser 
access key
secret access key 



1--> data/artifacts --->local sytem root dir

local data dir to s3 bucket--> problem statement 

configuration
iam roles 
access key
secret access key
region name

configure 

configured 



ec2--->vm setup
ecr repository-->elastic container
ecs-->

ecr-->ecs---ec2
s3--> 
github actions-->

application  manual deployment

ci.cd pipeline

.github/workflows/cicd.yaml
application local --- push github ---->cloud deployments

github runners

connection between github to ec2 machine
artifacts
saved_models

link-->open 

iam  --> 5 members in your team 
lead developer

3 devops engineer 2 fs dev

ec2 and s3 

iam 


ecr and ecs

iam -->user1 user2 user3  -->group --> policies for access to ecr and ecs --->access key and secret access key

ecr repository



aws login--->build the docker image-->deploy this docker image to ecr(elastic container registry) repository---->ecs repositorty---->connecting a ec2 machine and run the docker file over ec2 machine-->exposed host and port keys---> i need to change the configure the credential of ec2 machine and make the host as to all traffic and i can abble to open the link and access the apache airflow on cloud

apache airflow open a link---> 2 dags   
                            i) sensor from feature store to saved_models
                            ii) own data to saved_models
i) dag if i run 1st dag saved_model and artifacts get generated from this i directly deploy this 2 directories to s3 bucket

ii)i need to have already the new data on my s3 bucket--->we fetch the data from s3 bucket and from s3 bucket-->start running a pipeline for a new data --> prediction.csv file will be generated 
171 columns --> extra columns prediction column --> 172 columns --> deploy this predictions.csv data to same s3 bucket with dir name as prediction