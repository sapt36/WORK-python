# **kwargs =pack all arguments into a dictionary(need position)
#          fast and accept varying amount of keyword arguments

def hello(**kwargs):
    print("Hello " + kwargs['first'] + " " + kwargs['last'])
hello(first="And" , middle="rew" , last="Chen")

def hello2(**train_kwargs): #changable
    print("Hello ")
    for key,value in train_kwargs.items():
        print(value,end="@")
        #,end = " " : replace new line char to something else
hello2(a="a",b="b",c="c",d="d",e="e",f="f")

data_kwargs = {
    "folder": "FOLDER",
    "crypto_list": "CRYPTO_LIST",
    "feature_list": "FEATURE_LIST",
    "train_start_date": "TRAIN_START_DATE",
    "train_end_date": "TRAIN_END_DATE",
    "trade_start_date": "TRADE_START_DATE",
    "trade_end_date": "TRADE_END_DATE"
}

def env(**kwargs):
    print(" ")
    print("Type: ")
    for key,value in kwargs.items():
        print(key,end=" / ")
env(**data_kwargs)