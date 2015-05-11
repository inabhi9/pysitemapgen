'''
pytz setup script
'''

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

me = 'Abhinav Kotak'
memail = 'in.abhi9@gmail.com'

packages = ['pysitemapgen']

setup(
    name='pysitemapgen',
    version='0.0.1',
    zip_safe=True,
    description='Simple sitemap and sitemap index generator',
    author=me,
    author_email=memail,
    maintainer=me,
    maintainer_email=memail,
    install_requires=['lxml'],
    url='https://github.com/inabhi9/pytimeframe',
    license=open('LICENSE', 'r').read(),
    keywords=['sitemap', 'google', 'sitemap generator', 'sitemap index'],
    packages=packages,
    platforms=['Independant'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
