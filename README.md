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
