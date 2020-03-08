import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-polls",  # Replace with your own username
    version="0.0.1",
    author="Thomas Erhel",
    author_email="thomas.erhel@gmail.com",
    description="A Django app to conduct Web-based polls.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThomasErhel/django-polls",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7.5",
        "License :: OSI Approved :: GNU General Public License version 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.5',
)
