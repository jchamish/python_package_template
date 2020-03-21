"""Installation setup script"""

import setuptools

setuptools.setup(
    name="python_package_name",
    version="0.0.1",
    author="Your Name",
    author_email="your_email@gmail.com",
    description="What my python package does is...",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",  # Works with Python 3.6 (Remove if not true)
        "Programming Language :: Python :: 3.7",  # Works with Python 3.7 (Remove if not true)
        "Programming Language :: Python :: 3.8",  # Works with Python 3.8 (Remove if not true)
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
)
