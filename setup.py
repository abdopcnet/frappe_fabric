from setuptools import setup, find_packages

setup(
    name="frappe_fabric",
    version="1.0.0",
    description="Fabric and Roll Management for ERPNext",
    author="Your Company",
    author_email="info@yourcompany.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["frappe", "erpnext"],
    python_requires=">=3.10",
)
