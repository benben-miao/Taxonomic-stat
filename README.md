### 1.Run with conda or python environment
#### 1.1 Create a conda environment
```bash
# Install python & pip for environment
conda create -n taxonomic-stat python=3.9
conda activate taxonomic-stat

# Install modules with pip for reducing execute file
pip install pandas
pip install numpy
pip install openpyxl
pip install xlrd
```
#### 1.2 Runing the `taxonomic-stat.py` python script
```bash
# The input file of `example.xlsx` is neccecary
python taxonomic-stat.py example.xlsx
```
### 2. For users without conda or python environment
#### 2.1 Compile a execution program
```bash
# Don't forget to activate the environment
conda activate taxonomic-stat

# Install pyinstaller module
pip install pyinstaller

# Compile the python script
pyinstaller -F taxonomic-stat.py
```
#### 2.2 Run the executable file
```bash
# Execute the exe file after compiling by yourself or download from the release
./taxonomic-stat.exe example.xlsx

# The result file should be `example_result.xlsx` or `_result.xlsx`
```
### 3. Data prepare
#### 3.1 Input file structure
| Family           | Genus               | Species |
|------------------|---------------------|---------|
| 䱵科 Cirrhitidae | 钝䱵 Amblycirrhitus | 1       |
| 䱵科 Cirrhitidae | 金䱵 Cirrhitichthys | 4       |
| 䱵科 Cirrhitidae | 䱵 Cirrhitus        | 1       |
| 䱵科 Cirrhitidae | 副䱵 Paracirrhites  | 2       |
| 䲟科 Echeneidae  | 䲟 Echeneis         | 1       |
| 䲟科 Echeneidae  | 短䲟 Remora         | 3       |
|
#### 3.2 Output result content
| Family             | Genus                  | Species | Ratios      | LnRatio      | NegMul      |
|--------------------|------------------------|---------|-------------|--------------|-------------|
| 䱵科 Cirrhitidae     | 钝䱵 Amblycirrhitus      | 1       | 0.125       | -2.079441542 | 0.259930193 |
| 䱵科 Cirrhitidae     | 金䱵 Cirrhitichthys      | 4       | 0.5         | -0.693147181 | 0.34657359  |
| 䱵科 Cirrhitidae     | 䱵 Cirrhitus            | 1       | 0.125       | -2.079441542 | 0.259930193 |
| 䱵科 Cirrhitidae     | 副䱵 Paracirrhites       | 2       | 0.25        | -1.386294361 | 0.34657359  |
| 䲟科 Echeneidae      | 䲟 Echeneis             | 1       | 0.25        | -1.386294361 | 0.34657359  |
| 䲟科 Echeneidae      | 短䲟 Remora              | 3       | 0.75        | -0.287682072 | 0.215761554 |
|

