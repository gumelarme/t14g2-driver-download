import httpx
import json

def get_file_list(filename: str) -> list[dict[str, any]]:
    with open(filename, 'r') as f:
        return json.loads(f.read())


def main():
    files = get_file_list("driver-list.json")
    for file in files:
        print(file["name"])

if __name__ == "__main__":
    main()

