# Numerical and Machine Learning Methods for Corneal Curvature Modeling

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

A comprehensive comparative study implementing three different approaches to solve the nonlinear corneal curvature boundary value problem: traditional numerical methods and physics-informed neural networks.

## 🔬 Project Overview

This project focuses on mathematical modeling of corneal curvature using a boundary value ordinary differential equation (BVODE) model. The cornea is modeled as a thin membrane under static force balance, incorporating biomechanical principles through tension forces, elastic constants, and applied pressure.

### Mathematical Model

The dimensionless governing equation:
-d²h/dx² / √(1 + (dh/dx)²) + ah = b / √(1 + (dh/dx)²)


**Boundary Conditions:**
- `h'(0) = 0` (zero slope at center due to symmetry)
- `h(1) = 0` (zero height at corneal periphery)

**Parameters:**
- `a = R²k/T`: ratio of elastic to tension forces
- `b = RP/T`: ratio of pressure to tension forces

## 🎯 Objectives

1. **Numerical Methods**: Implement and compare multiple numerical solution schemes  
2. **Machine Learning**: Develop Physics-Informed Neural Network (PINN) approach  
3. **Performance Analysis**: Evaluate methods based on accuracy, computational efficiency, and stability

## 🔧 Methods Implemented

### 1. Reference Method: Method of Lines (MOL)
- Transforms steady-state BVP into time-dependent problem
- Uses LSODA solver with high-order finite differences  
- **Accuracy**: Benchmark solution  
- **Time**: 0.9 seconds

### 2. Shooting Method + Runge-Kutta (RK4)
- Converts BVP to IVP using shooting technique  
- Fourth-order Runge-Kutta integration  
- Secant method for root finding  
- **Accuracy**: Max error < 0.35%  
- **Time**: 0.0114 seconds

### 3. Finite Difference + Damped Newton-Raphson
- Spatial discretization with central differences  
- Damped Newton-Raphson for nonlinear system  
- **Accuracy**: Max error < 5.67%  
- **Time**: 0.086 seconds

### 4. Physics-Informed Neural Network (PINN)
- 3 hidden layers with 50 neurons each  
- Multi-component loss function (data + physics + boundary)  
- Automatic differentiation for gradient computation  
- **Accuracy**: Max error 4.38%  
- **Time**: 148 microseconds

## 📊 Results Summary

| Method             | Max Absolute Error | Max Relative Error | Execution Time | Convergence        |
|--------------------|-------------------|---------------------|----------------|---------------------|
| Shooting + RK4     | < 0.001227         | < 0.35%             | 0.0114 s       | 10⁻¹⁰               |
| Finite Difference  | < 0.019418         | < 5.67%             | 0.086 s        | 10⁻⁸                |
| PINN               | 0.0127             | 4.38%               | 148×10⁻⁶ s     | MSE: 4.73×10⁻⁵      |

## 🚀 Getting Started

### Prerequisites

```bash
python >= 3.8
numpy >= 1.21.0
scipy >= 1.7.0
matplotlib >= 3.4.0
torch >= 1.9.0
pandas >= 1.3.0
```
### Installation

### 1. Clone the repository
```bash
git clone https://github.com/3bdullah-Gamil/corneal-curvature-modeling.git
cd corneal-curvature-modeling
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 📁 Project Structure
```bash
├── README.md
├── requirements.txt
├── main.py                 # Main execution script
├── config.py              # Configuration parameters
├── src/
│   ├── reference_mol.py    # Method of Lines (Reference)
│   ├── shooting_method.py  # Shooting + RK4 implementation
│   ├── finite_difference.py # Finite Difference + Newton-Raphson
│   ├── pinn_method.py     # Physics-Informed Neural Network
├── data/
│   └── reference_solution.csv  # MOL reference data
├── results/
│   ├── plots             # Generated figures
├── docs/
    ├── report.pdf         # IEEE conference paper
    └── Reference Book 

```


## 📈 Usage Examples
```bash
from src.shooting_method import ShootingMethod
from src.finite_difference import FiniteDifferenceMethod
from src.pinn_method import PINNMethod
corneal-curvature-modeling/

```

### Set parameters
a, b = 2.0, 1.0  # Dimensionless parameters

### Shooting Method
shooter = ShootingMethod(a=a, b=b)
x_shoot, h_shoot = shooter.solve()

### Finite Difference Method
fd_solver = FiniteDifferenceMethod(a=a, b=b, n_points=21)
x_fd, h_fd = fd_solver.solve()

### PINN Method
pinn = PINNMethod(a=a, b=b)
pinn.train(epochs=2000)
x_pinn, h_pinn = pinn.predict()

## 🔬 Scientific Context

This work addresses the mathematical modeling of corneal biomechanics, which is crucial for:

- **Clinical Applications**: Corneal surgery planning and outcome prediction  
- **Biomedical Engineering**: Understanding corneal deformation under various loading conditions  
- **Computational Methods**: Comparing traditional numerical methods with modern ML approaches

## 📊 Performance Metrics

### Accuracy Metrics
- Mean Squared Error (MSE)  
- Mean Absolute Error (MAE)  
- Maximum Absolute Error  
- Maximum Relative Error  

### Computational Metrics  
- Execution Time  
- Convergence Rate  
- Memory Usage  
- Stability Analysis

## 🤝 Contributing
1. Fork the repository  
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)  
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)  
4. Push to the branch (`git push origin feature/AmazingFeature`)  
5. Open a Pull Request  

## 📚 References

1. W. E. Schiesser, *"Differential Equation Analysis in Biomedical Science and Engineering: Ordinary Differential Equation Applications with R,"* John Wiley & Sons, 2014.  
2. W. Okrasifski and L. Plociniczak, *"A nonlinear mathematical model of the corneal shape,"* Nonlinear Analysis: Real World Applications, vol. 13, no. 3, pp. 1498-1505, 2012.  
3. [Physics-Based Deep Learning](https://physicsbaseddeeplearning.org/)  

## 📜 License

This project is licensed under the [MIT License](LICENSE) - see the **LICENSE** file for details.

## 👥 Team Members

**Team 3-SBE28**

- Abdulrahman hassan     
- Abdulrahman Yasser
- Moustafa Ali
- Mostafa Hazem
- Ganna Ahmed
- Shaimaa Abdelziz
- Sohaila Emad
- Shahd Mabrouk
- Mariam Mohamed
- Mariam Hosny


## Course Information

- **Course:** SBEG108 - Numerical Methods in Biomedical Engineering  
- **Instructor:** Dr. Muhammad Rushdi  
- **Institution:** Cairo University, Faculty of Engineering  
- **Academic Year:** 2024/2025  
- **Semester:** Spring 2025  

## Contact

For questions or collaborations, please contact:

- **Email:** [abdullahgamil285@gmail.com]  
- **Project Repository:** [Corneal Curvature Modeling](https://github.com/3bdullah-Gamil/corneal-curvature-modeling)  

---

### ❖ If you found this project helpful, please consider giving it a ⭐ on GitHub!
