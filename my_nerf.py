import requests
from pathlib import Path

def main():
    if not Path("./data/tiny_nerf_data.npz").exists():
        url = "http://cseweb.ucsd.edu/~viscomp/projects/LF/papers/ECCV20/nerf/tiny_nerf_data.npz"
        filename = "tiny_nerf_data.npz"
        url_data = requests.get(url).content
        with open(filename, mode="wb") as f:
            f.write(url_data)

if __name__ == '__main__':
    main()