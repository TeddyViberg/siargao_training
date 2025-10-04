# Siargao Python Training

Hej hej! Welcome to the Siargao Python Training project! This is a comprehensive Python learning resource designed for beginners to intermediate learners.

## 🏝️ About This Project

This project provides a structured approach to learning Python programming with hands-on exercises, Jupyter notebooks, and practical challenges. Perfect for anyone starting their Python journey or looking to strengthen their fundamentals.

## 📁 Project Structure

```
siargao-training/
├── README.md                 # This file
├── requirements.txt          # Python package dependencies
├── .gitignore              # Git ignore file
├── 00_welcome.ipynb         # Python basics notebook
├── 01_basics.ipynb         # Python basics notebook
```


### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Navigate to the project directory**
   ```bash
   cd siargao-training
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv your-choosen-environment-name
   
   source your-choosen-environment-name/bin/activate
   ```

3. **Install packages:**

   ```bash
   pip install -r requirements.txt
   ```


4. **Start Jupyter Notebook**
   ```bash
   jupyter lab
   ```

### Python 3.12 Compatibility

If you're using Python 3.12 and encounter installation issues:

1. **Upgrade pip and setuptools first:**
   ```bash
   python -m pip install --upgrade pip setuptools
   ```

2. **Try the simple requirements:**
   ```bash
   pip install -r requirements-simple.txt
   ```

3. **If still having issues, install packages individually:**
   ```bash
   pip install jupyter numpy pandas matplotlib requests pytest python-dotenv
   ```

## 📚 Learning Path

### 1. Start with the Basics
- Open `01_basics.ipynb` to learn about:
  - Variables and data types
  - Basic operations
  - Input and output
  - Comments and documentation

### 2. Control Structures
- Work through `02_control_structures.ipynb` to understand:
  - If/else statements
  - For loops
  - While loops
  - Break and continue

### 3. Functions
- Explore `03_functions.ipynb` to learn:
  - Function definition and calling
  - Parameters and arguments
  - Return values
  - Default parameters

### 4. Data Structures
- Study `04_data_structures.ipynb` to master:
  - Lists and tuples
  - Dictionaries
  - Sets
  - String methods

### 5. Practice with Challenges
- Run `challenges.py` for structured exercises:
  ```python
   python challenges.py
   ```

## 🎯 Challenge Levels

The `challenges.py` file contains 10 levels of increasing difficulty:

1. **Beginner (1-3)**: Variables, math, conditionals
2. **Intermediate (4-6)**: Loops, functions, data structures
3. **Advanced (7-9)**: File handling, error handling, classes
4. **Projects (10)**: Mini-projects combining multiple concepts

## 🛠️ Available Tools

### Jupyter Notebooks
- Interactive coding environment
- Mix of code, markdown, and output
- Perfect for learning and experimentation

### Main Challenges File
- Structured exercises with clear instructions
- Example solutions and hints
- Progressive difficulty levels

### Required Packages
- **Jupyter**: Interactive notebook environment
- **NumPy**: Numerical computing
- **Pandas**: Data manipulation
- **Matplotlib**: Data visualization
- **Requests**: HTTP library
- **Flask**: Web framework
- **Pytest**: Testing framework

## 💡 Tips for Learning

1. **Start with notebooks**: Work through each notebook in order
2. **Practice regularly**: Code every day, even if just for 30 minutes
3. **Experiment**: Don't just follow examples - try variations
4. **Use challenges**: Complete the exercises in `challenges.py`
5. **Ask questions**: Python has excellent documentation and community

## 🐛 Troubleshooting

### Common Issues

**Jupyter won't start:**
```bash
pip install --upgrade jupyter
```

**Import errors:**
```bash
pip install -r requirements.txt
```

**Virtual environment issues:**
```bash
# Deactivate and recreate
deactivate
python -m venv venv --clear
```

## 📖 Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)
- [Python for Beginners](https://www.python.org/about/gettingstarted/)
- [Real Python Tutorials](https://realpython.com/)

## 🤝 Contributing

Feel free to:
- Add more exercises
- Improve existing content
- Fix bugs or typos
- Suggest new topics

## 📄 License

This project is open source and available under the MIT License.

## 🏝️ About Siargao

Siargao is a beautiful island in the Philippines known for its surfing, natural beauty, and friendly people. This project is inspired by the island's spirit of adventure and learning!

---

**Happy Coding! 🐍✨**

*Start your Python journey today and discover the power of programming!*
