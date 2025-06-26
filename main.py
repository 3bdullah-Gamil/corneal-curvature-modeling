"""
Main execution script for corneal curvature modeling comparison.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.reference_mol import ReferenceMOL
from src.shooting_method import ShootingMethod
from src.finite_difference import FiniteDifferenceMethod
from src.pinn_method import PINNMethod
from src.analysis import PerformanceAnalyzer
from config import MODEL_PARAMS
import time

def main():
    """Main function to run all methods and perform comparison."""
    
    print("🔬 Corneal Curvature Modeling - Comparative Study")
    print("=" * 50)
    
    # Parameters
    a, b = MODEL_PARAMS['a'], MODEL_PARAMS['b']
    
    # Initialize methods
    methods = {}
    results = {}
    
    print("\n1️⃣ Running Reference Method (MOL)...")
    start_time = time.time()
    mol = ReferenceMOL(a=a, b=b)
    x_ref, h_ref = mol.solve()
    results['MOL'] = {
        'x': x_ref, 
        'h': h_ref, 
        'time': time.time() - start_time
    }
    print(f"   ✅ Completed in {results['MOL']['time']:.4f} seconds")
    
    print("\n2️⃣ Running Shooting Method + RK4...")
    start_time = time.time()
    shooter = ShootingMethod(a=a, b=b)
    x_shoot, h_shoot = shooter.solve()
    results['Shooting'] = {
        'x': x_shoot, 
        'h': h_shoot, 
        'time': time.time() - start_time
    }
    print(f"   ✅ Completed in {results['Shooting']['time']:.4f} seconds")
    
    print("\n3️⃣ Running Finite Difference + Newton-Raphson...")
    start_time = time.time()
    fd_solver = FiniteDifferenceMethod(a=a, b=b)
    x_fd, h_fd = fd_solver.solve()
    results['FiniteDiff'] = {
        'x': x_fd, 
        'h': h_fd, 
        'time': time.time() - start_time
    }
    print(f"   ✅ Completed in {results['FiniteDiff']['time']:.4f} seconds")
    
    print("\n4️⃣ Running Physics-Informed Neural Network...")
    start_time = time.time()
    pinn = PINNMethod(a=a, b=b)
    pinn.train()
    x_pinn, h_pinn = pinn.predict()
    results['PINN'] = {
        'x': x_pinn, 
        'h': h_pinn, 
        'time': time.time() - start_time
    }
    print(f"   ✅ Completed in {results['PINN']['time']:.4f} seconds")
    
    print("\n📊 Performing Analysis and Generating Reports...")
    analyzer = PerformanceAnalyzer(results)
    analyzer.compare_all_methods()
    analyzer.generate_plots()
    analyzer.save_results()
    
    print("\n🎉 Analysis Complete! Check the results/ directory for outputs.")
    print("📁 Generated files:")
    print("   - results/comparison_results.csv")
    print("   - results/plots/method_comparison.png")
    print("   - results/plots/error_analysis.png")
    print("   - results/performance_metrics.json")

if __name__ == "__main__":
    main()
