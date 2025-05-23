import json

def read_variables():
    with open('variables.json', 'r') as f:
        data = json.load(f)
    
    print("Project Configuration:")
    print(f"Project Name : {data['project_name']}")
    print(f"Maintainer   : {data['maintainer']}")
    print(f"Version      : {data['version']}")
    print(f"Environment  : {data['environment']}")
    print(f"Deploy Time  : {data['deploy_time']}")
    print(f"Region       : {data['region']}")
    print("\nServices Info:")
    for service in data['services']:
        print(f" - {service['name']} (Port: {service['port']}, Status: {service['status']})")

if __name__ == "__main__":
    read_variables()
