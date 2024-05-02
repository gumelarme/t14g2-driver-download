import os
import httpx
import json
import logging

from pathlib import Path

DOWNLOAD_DIR = "downloads"

def get_file_list(filename: str) -> list[dict[str, any]]:
    with open(filename, 'r') as f:
        return json.loads(f.read())


def main():
    Path(DOWNLOAD_DIR).mkdir(parents=True, exist_ok=True)

    files = get_file_list("driver-list.json")
    for file in files:
        filename = os.path.join(DOWNLOAD_DIR, file["name"])
        logging.info(f"Downloading {file['link']}")
        try:
            download_file(filename, file["link"])
        except httpx.HTTPError:
            logging.error(f"Failed downloading {filename}")
            continue


def download_file(filename: str, link: str):
    with httpx.stream("GET", link) as r:
        r.raise_for_status()

        with open(filename, 'wb') as f:
            for chunk in r.iter_bytes(chunk_size=2 ** 13):
                f.write(chunk)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()

