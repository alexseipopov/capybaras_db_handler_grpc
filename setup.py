from setuptools import setup, find_packages

setup(
    name='db_service_grpc',
    version='0.0.10',
    packages=find_packages(),
    install_requires=[
        "grpcio",
        "grpcio-tools"
    ],
)