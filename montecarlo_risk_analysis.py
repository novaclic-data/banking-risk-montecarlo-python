import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. CORE SIMULATION FUNCTION
def run_risk_simulation(filename, prob_def, volt, rate, color, title):
    """
    Executes a Monte Carlo simulation for banking credit risk.
    Calculates VaR (Value at Risk) and Net Profit/Loss scenarios.
    """
    n_sim = 10000
    loan_amount = 1000000
    income = loan_amount * rate
    
    # Generate Default Scenarios (Normal Distribution)
    scenarios = np.random.normal(prob_def, volt, n_sim)
    scenarios = np.clip(scenarios, 0, 1) # Logical limit 0-100%
    
    # Calculate Net Result (Income - Losses)
    net_result = income - (loan_amount * scenarios)
    
    # Key Metrics: VaR at 95% confidence level
    var_95 = np.percentile(net_result, 5)
    prob_loss = (net_result < 0).mean() * 100

    # Data Visualization
    plt.figure(figsize=(10, 6))
    sns.histplot(net_result, kde=True, color=color)
    plt.axvline(0, color='black', linestyle='--', label='Break-even Point')
    plt.axvline(var_95, color='orange', label=f'VaR 95% ({var_95:,.0f} USD)')
    plt.title(title, fontsize=14)
    plt.xlabel('Net Profit / Loss (USD)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.savefig(filename)
    plt.close()
    
    print(f"✅ Scenario '{title}' completed. Probability of Loss: {prob_loss:.2f}%")

# 2. EXECUTIVE RISK TRILOGY EXECUTION
if __name__ == "__main__":
    print("🚀 Initializing Financial Simulation Engine...")
    
    # Scenario 1: Normal Operations
    run_risk_simulation("1_riesgo_normal.png", 0.02, 0.01, 0.05, "forestgreen", "Normal Market: Stable Operations")

    # Scenario 2: Stress Test (Crisis)
    run_risk_simulation("2_riesgo_crisis.png", 0.15, 0.05, 0.05, "crimson", "Stress Test: Market Crisis")

    # Scenario 3: Strategic Rescue (Optimization)
    run_risk_simulation("3_riesgo_rescate.png", 0.15, 0.05, 0.20, "gold", "Recovery Strategy: Rate Optimization")
    
    print("\n📊 All visual assets generated successfully for the Risk Report.")