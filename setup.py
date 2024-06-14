from setuptools import find_packages, setup


setup(
    name='yashfield',
    version='0.1.0',
    license='MIT',
    include_package_data=True,
    author='yash shukla',
    author_email='contact@bradjasper.com',
    maintainer='Ryan P Kilby',
    maintainer_email='kilbyr@gmail.com',
    url='https://github.com/rpkilby/jsonfield/',
    description='A custom modified package of jsonfield with additional functionalities',
    long_description=open("README.rst").read(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['Django >= 2.2'],
    python_requires='>=3.6',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
