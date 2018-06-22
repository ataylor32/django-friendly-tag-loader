import codecs
from os.path import join, dirname
from setuptools import setup


version = '1.3'
read = lambda *names: codecs.open(join(dirname(__file__), *names),
                                  encoding='utf-8').read().strip()

setup(
    name='django-friendly-tag-loader',
    version=version,
    description='Want to optionally use a template tag library? Use this!',
    long_description='\n\n'.join((read('README'), read('CHANGES'),)),
    author='Jaap Roes',
    author_email='jaap.roes@gmail.com',
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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[],
    zip_safe=False,
)
