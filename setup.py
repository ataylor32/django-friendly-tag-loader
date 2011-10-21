import codecs
from os.path import join, dirname
from setuptools import setup


version = '1.0'
read = lambda *rnames: unicode(codecs.open(join(dirname(__file__), *rnames),
                                           encoding='utf-8').read()
                              ).strip()

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
      'Programming Language :: Python',
    ],
    install_requires=[],
    tests_require=['Django>=1.2',],
    test_suite='tests.runtests.runtests',
    zip_safe=False,
)
