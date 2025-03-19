import subprocess
import multiprocessing
from typing import List

def install_package(package: str):
    """安装单个包"""
    try:
        subprocess.check_call(["pip", "install", package])
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package}: {e}")

def install_packages_concurrently(packages: List[str], max_workers: int = 4):
    """并发安装多个包"""
    with multiprocessing.Pool(processes=max_workers) as pool:
        pool.map(install_package, packages)

if __name__ == "__main__":
    # 假设从 requirements.txt 读取依赖
    with open("requirements.txt", "r") as f:
        packages = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    install_packages_concurrently(packages, max_workers=16)