import json

def read_variables():
    with open('/var/lib/jenkins/workspace/MT25010-Uday/Task-21-05-2025/task-5-json-reader/Task-21-04-2025/task-5/variables.json', 'r') as f:
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
