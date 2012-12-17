from distutils.core import setup

setup(
    name='RoadRunner',
    version='0.0dev',
    packages=['roadrunnerlib'],
    license='Apache License 2.0',
    long_description=open('README.rst').read(),
    package_data={'roadrunnerlib' : ['data/*']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Topic :: Scientific/Engineering'
        ]
    )
