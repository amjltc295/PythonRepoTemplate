# Python Repository Template

Python repository template with Travis CI, Conda environment, .gitigone, Flake8 and PR template

## Installation

1. Install miniconda/anaconda, a package for  package/environment management
```
wget repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

2. Build conda environment from file
```
conda env create -f environment.yaml
```

3. Activate the environment
```
source activate <environemnt name>
```

## Repository Structure
```
├── .gitignore              Filenames in this file would be ignored by Git
├── .flake8                 Syntax and style settings for Flake8
├── .travis.yml             For Travis CI configuration
├── environment.yaml        For Conda environment
├── README.md
├── LICENSE                 LICENSE file (MIT license here)
├── tests/                  For tests
├── lib/                    For third-party libraries
└── src/                    For source code

```
## License

MIT 

## Authors

Ya-Liang Chang (Allen) [amjltc295](https://github.com/amjltc295/)


