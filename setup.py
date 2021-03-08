from setuptools import setup
def readme():
    with open('README.md') as f:
        README = f.read()
    return README
setup(
  name = 'TOPSIS_ANUJ_101803638',         # How you named your package folder (MyLib)
  packages = ['TOPSIS_ANUJ_101803638'],   # Chose the same as "name"
  version = '0.5',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'THIS PACKAGE IS TO IMPLEMENT TOPSIS',   # Give a short description about your library
  long_description=readme(),
  long_description_content_type="text/markdown",
  author = 'ANUJ SINGLA',                   # Type in your name
  author_email = 'artistanujsingla123@gmail.com',      # Type in your E-Mail
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)