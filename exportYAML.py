#Kevin Doyon
#Python/SQL Assignment

import yaml

#Saves data to yaml
def runyaml(data,filename):
    with open(filename,"wt") as file:
        yaml_data = yaml.dump(data,sort_keys=False)
        file.write(yaml_data)

if __name__ == "__main__":
    print("This is exportYAML")