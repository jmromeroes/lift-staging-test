import os

def create_Dockerfiles():
    for i in range(50):
        newpath = "../place{}/".format(i)
        print(newpath)
        
        if not os.path.exists(newpath):
            print("Path already exists")
            os.makedirs(newpath)
        else:
            continue
        
        with open("{}/{}".format(newpath, "Dockerfile"), 'w') as f:
            f.write("""
FROM ubuntu

USER root

RUN apt install -y \
    curl \
    jq \
    less

WORKDIR /app/

USER root

COPY file.txt .

CMD [ "jq" ]
""")


create_Dockerfiles()
