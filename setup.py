from setuptools import setup
from pspdfkit import __version__


setup(
    name="pspdfkit",
    version=__version__,
    url="https://github.com/tizz98/py-pspdfkit",
    download_url="https://github.com/tizz98/py-pspdfkit/tarball/{version}".format(
        version=__version__,
    ),
    author="Elijah Wilson",
    author_email="elijah@elijahwilson.me",
    description="A simple API wrapper for PSPDFKit",
    long_description=open('README.md').read(),
    license="MIT",
    keywords="pspdfkit pdf",
    install_requires=[
        "python-magic==0.4.15",
        "requests==2.18.4",
    ],
    packages=[
        "pspdfkit",
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    zip_safe=True,
)
