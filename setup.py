import codecs
from os.path import join, dirname
from setuptools import setup


version = '1.2'
read = lambda *names: codecs.open(join(dirname(__file__), *names),
                                  encoding='utf-8').read().strip()

setup(
    name='django-friendly-tag-loader',
    version=version,
    description='Want to optionally use a template tag library? Use this!',
    long_description='\n\n'.join((read('README'), read('CHANGES'),)),
    author='Jaap Roes (Eight Media)',
    author_email='jaap@eight.nl',
    url='https://bitbucket.org/jaap3/django-friendly-tag-loader/',
    package_dir={'': 'src'},
    packages=['friendlytagloader', 'friendlytagloader.templatetags'],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=[],
    zip_safe=False,
)
