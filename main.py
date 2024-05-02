import os
import httpx
import json
import logging

from pathlib import Path

DOWNLOAD_DIR = "downloads"

log = logging.getLogger(__name__)
console = logging.StreamHandler()
c_format = logging.Formatter('[%(levelname)s:%(name)s] - %(message)s')
console.setFormatter(c_format)

log.setLevel(logging.INFO)
log.addHandler(console)


def get_file_list(filename: str) -> list[dict[str, any]]:
    with open(filename, 'r') as f:
        return json.loads(f.read())


def humane_size(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

def get_download_size(link: str) -> str:
    resp = httpx.head(link)
    return int(resp.headers["content-length"])

def is_file_downloaded(filename: str, expected_size: int) -> bool:
    try:
        return expected_size == os.path.getsize(filename)
    except FileNotFoundError:
        return False


def main():
    Path(DOWNLOAD_DIR).mkdir(parents=True, exist_ok=True)

    files = get_file_list("driver-list.json")
    for file in files:
        filename = os.path.join(DOWNLOAD_DIR, file["name"])
        link = file['link']
        file_size = get_download_size(link)
        if is_file_downloaded(filename, file_size):
            log.info(f"{filename} - EXIST")
            continue

        log.info(f"Downloading {filename} ({humane_size(file_size)})")
        try:
            download_file(filename, link)
        except httpx.HTTPError:
            log.error(f"Failed downloading {filename}")
            continue

        log.info(f"{filename} - DONE")


def download_file(filename: str, link: str):
    with httpx.stream("GET", link) as r:
        r.raise_for_status()

        with open(filename, 'wb') as f:
            for chunk in r.iter_bytes(chunk_size=2 ** 13):
                f.write(chunk)

if __name__ == "__main__":
    main()

