from setuptools import setup
import os
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def load_requirements(fname):
    reqs = parse_requirements(fname, session=False)
    try:
        req = [str(ir.requirement) for ir in reqs]
    except:
        req = [str(ir.req) for ir in reqs]
    return reqs

setup(
    name='fedo-ruw-api',
    version=os.getenv('RUW_VERSION'),
    include_package_data=True,
    packages=['users', 'users.migrations', 'eventmgmt', 'static'],
    url='http://localhost:8000',
    license='',
    author='Nadeem',
    author_email='nadeem.p.j@gmail.com',
    description='Event Management API',
    scripts=['manage.py'],
    python_requires="==3.6.9",
    install_requires=load_requirements("requirements.txt")
)
