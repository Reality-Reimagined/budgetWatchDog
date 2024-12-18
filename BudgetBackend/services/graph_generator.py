import matplotlib.pyplot as plt
import os

# Ensure the reports directory exists
REPORTS_DIR = "reports"
os.makedirs(REPORTS_DIR, exist_ok=True)

def generate_graph(graph_type: str, data: dict, save_dir=REPORTS_DIR):
    """ Generate various financial graphs based on graph_type and data """
    save_path = os.path.join(save_dir, f"{graph_type}.png")

    try:
        plt.figure(figsize=(10, 6))  # Larger figure size for better quality
        plt.style.use('seaborn')  # More professional style

        if graph_type == "net_debt":
            years = data["years"]
            net_debt = data["net_debt"]
            plt.plot(years, net_debt, marker='o', color='#2563eb', linewidth=2)
            plt.title("Net Debt Over Time", pad=20, fontsize=14, fontweight='bold')
            plt.xlabel("Year", labelpad=10)
            plt.ylabel("Net Debt (Billions CAD)", labelpad=10)
            plt.grid(True, alpha=0.3)

        elif graph_type == "gdp_growth":
            years = data["years"]
            gdp_growth = data["gdp_growth"]
            plt.plot(years, gdp_growth, marker='o', color='#059669', linewidth=2)
            plt.title("GDP Growth Rate", pad=20, fontsize=14, fontweight='bold')
            plt.xlabel("Year", labelpad=10)
            plt.ylabel("GDP Growth (%)", labelpad=10)
            plt.grid(True, alpha=0.3)

        elif graph_type == "inflation_rate":
            months = data["months"]
            inflation = data["inflation_rate"]
            plt.plot(months, inflation, marker='o', color='#dc2626', linewidth=2)
            plt.title("Inflation Rate", pad=20, fontsize=14, fontweight='bold')
            plt.xlabel("Month", labelpad=10)
            plt.ylabel("Inflation (%)", labelpad=10)
            plt.grid(True, alpha=0.3)
            plt.xticks(rotation=45)

        elif graph_type == "employment_growth":
            years = data["years"]
            employment = data["employment_growth"]
            plt.bar(years, employment, color='#7c3aed', alpha=0.8)
            plt.title("Employment Growth Rate", pad=20, fontsize=14, fontweight='bold')
            plt.xlabel("Year", labelpad=10)
            plt.ylabel("Employment Growth (%)", labelpad=10)
            plt.grid(True, alpha=0.3, axis='y')

        elif graph_type == "debt_to_gdp":
            years = data["years"]
            debt_to_gdp = data["debt_to_gdp"]
            plt.plot(years, debt_to_gdp, marker='o', color='#0891b2', linewidth=2)
            plt.title("Debt-to-GDP Ratio", pad=20, fontsize=14, fontweight='bold')
            plt.xlabel("Year", labelpad=10)
            plt.ylabel("Debt-to-GDP (%)", labelpad=10)
            plt.grid(True, alpha=0.3)

        elif graph_type == "bond_yields":
            years = data["years"]
            yields = data["yields"]
            plt.plot(years, yields, marker='o', color='#9333ea', linewidth=2)
            plt.title("Government Bond Yields", pad=20, fontsize=14, fontweight='bold')
            plt.xlabel("Year", labelpad=10)
            plt.ylabel("Yield (%)", labelpad=10)
            plt.grid(True, alpha=0.3)

        else:
            raise ValueError(f"Unsupported graph type: {graph_type}")

        # Add some padding and adjust layout
        plt.tight_layout()
        
        # Save with high DPI for better quality
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()

        # Return the relative path for the URL
        return f"/reports/{os.path.basename(save_path)}"

    except Exception as e:
        print(f"Error generating graph {graph_type}: {e}")
        raise Exception(f"Graph generation failed for {graph_type}")


# import matplotlib.pyplot as plt
# import os
# import logging

# # Ensure the reports directory exists
# REPORTS_DIR = "reports"
# os.makedirs(REPORTS_DIR, exist_ok=True)

# def generate_graph(graph_type: str, data: dict, save_dir=REPORTS_DIR):
#     """ Generate various financial graphs based on graph_type and data """
#     save_path = os.path.join(save_dir, f"{graph_type}.png")

#     try:
#         if graph_type == "net_debt":
#             years = data["years"]
#             net_debt = data["net_debt"]
#             plt.figure(figsize=(8, 5))
#             plt.plot(years, net_debt, marker='o', color='blue')
#             plt.title("Net Debt Over Time")
#             plt.xlabel("Year")
#             plt.ylabel("Net Debt (Billions CAD)")
#             plt.grid()
#             plt.savefig(save_path)
#             plt.close()

#         elif graph_type == "gdp_growth":
#             years = data["years"]
#             gdp_growth = data["gdp_growth"]
#             plt.figure(figsize=(8, 5))
#             plt.plot(years, gdp_growth, marker='o', color='green')
#             plt.title("GDP Growth Rate")
#             plt.xlabel("Year")
#             plt.ylabel("GDP Growth (%)")
#             plt.grid()
#             plt.savefig(save_path)
#             plt.close()

#         elif graph_type == "inflation_rate":
#             months = data["months"]
#             inflation = data["inflation_rate"]
#             plt.figure(figsize=(8, 5))
#             plt.plot(months, inflation, marker='o', color='red')
#             plt.title("Inflation Rate")
#             plt.xlabel("Month")
#             plt.ylabel("Inflation (%)")
#             plt.grid()
#             plt.savefig(save_path)
#             plt.close()

#         elif graph_type == "employment_growth":
#             years = data["years"]
#             employment = data["employment_growth"]
#             plt.figure(figsize=(8, 5))
#             plt.bar(years, employment, color='purple')
#             plt.title("Employment Growth Rate")
#             plt.xlabel("Year")
#             plt.ylabel("Employment Growth (%)")
#             plt.grid(axis='y')
#             plt.savefig(save_path)
#             plt.close()

#         elif graph_type == "interest_payments":
#             years = data["years"]
#             interest = data["interest"]
#             plt.figure(figsize=(8, 5))
#             plt.bar(years, interest, color='orange')
#             plt.title("Interest Payments Over Time")
#             plt.xlabel("Year")
#             plt.ylabel("Interest (Billions CAD)")
#             plt.grid(axis='y')
#             plt.savefig(save_path)
#             plt.close()

#         elif graph_type == "debt_to_gdp":
#             years = data["years"]
#             debt_to_gdp = data["debt_to_gdp"]
#             plt.figure(figsize=(8, 5))
#             plt.plot(years, debt_to_gdp, marker='o', color='cyan')
#             plt.title("Debt-to-GDP Ratio")
#             plt.xlabel("Year")
#             plt.ylabel("Debt-to-GDP (%)")
#             plt.grid()
#             plt.savefig(save_path)
#             plt.close()

#         elif graph_type == "program_spending":
#             sectors = data["sectors"]
#             spending = data["spending"]
#             plt.figure(figsize=(8, 5))
#             plt.bar(sectors, spending, color='lightblue')
#             plt.title("Program-Specific Spending")
#             plt.xlabel("Sector")
#             plt.ylabel("Spending (Billions CAD)")
#             plt.grid(axis='y')
#             plt.savefig(save_path)
#             plt.close()

#         else:
#             logging.error(f"Unsupported graph type: {graph_type}")
#             raise ValueError(f"Unsupported graph type: {graph_type}")

#         logging.info(f"Generated graph: {save_path}")
#         return save_path

#     except Exception as e:
#         logging.error(f"Error generating graph {graph_type}: {str(e)}")
#         raise Exception(f"Graph generation failed for {graph_type}")



# import matplotlib.pyplot as plt
# import os

# # Ensure the reports directory exists
# REPORTS_DIR = "reports"
# os.makedirs(REPORTS_DIR, exist_ok=True)

# def generate_graph(graph_type: str, data: dict, save_dir=REPORTS_DIR):
#     """ Generate various financial graphs based on graph_type and data """
#     save_path = os.path.join(save_dir, f"{graph_type}.png")

#     try:
#         if graph_type == "net_debt":
#             years = data["years"]
#             net_debt = data["net_debt"]
#             plt.figure(figsize=(8, 5))
#             plt.plot(years, net_debt, marker='o', color='blue')
#             plt.title("Net Debt Over Time")
#             plt.xlabel("Year")
#             plt.ylabel("Net Debt (Billions CAD)")
#             plt.grid()
#             plt.savefig(save_path)
#             plt.close()

#         elif graph_type == "gdp_growth":
#             years = data["years"]
#             gdp_growth = data["gdp_growth"]
#             plt.figure(figsize=(8, 5))
#             plt.plot(years, gdp_growth, marker='o', color='green')
#             plt.title("GDP Growth Rate")
#             plt.xlabel("Year")
#             plt.ylabel("GDP Growth (%)")
#             plt.grid()
#             plt.savefig(save_path)
#             plt.close()

#         elif graph_type == "inflation_rate":
#             months = data["months"]
#             inflation = data["inflation_rate"]
#             plt.figure(figsize=(8, 5))
#             plt.plot(months, inflation, marker='o', color='red')
#             plt.title("Inflation Rate")
#             plt.xlabel("Month")
#             plt.ylabel("Inflation (%)")
#             plt.grid()
#             plt.savefig(save_path)
#             plt.close()

#         elif graph_type == "employment_growth":
#             years = data["years"]
#             employment = data["employment_growth"]
#             plt.figure(figsize=(8, 5))
#             plt.bar(years, employment, color='purple')
#             plt.title("Employment Growth Rate")
#             plt.xlabel("Year")
#             plt.ylabel("Employment Growth (%)")
#             plt.grid(axis='y')
#             plt.savefig(save_path)
#             plt.close()

#         elif graph_type == "interest_payments":
#             years = data["years"]
#             interest = data["interest"]
#             plt.figure(figsize=(8, 5))
#             plt.bar(years, interest, color='orange')
#             plt.title("Interest Payments Over Time")
#             plt.xlabel("Year")
#             plt.ylabel("Interest (Billions CAD)")
#             plt.grid(axis='y')
#             plt.savefig(save_path)
#             plt.close()

#         elif graph_type == "debt_to_gdp":
#             years = data["years"]
#             debt_to_gdp = data["debt_to_gdp"]
#             plt.figure(figsize=(8, 5))
#             plt.plot(years, debt_to_gdp, marker='o', color='cyan')
#             plt.title("Debt-to-GDP Ratio")
#             plt.xlabel("Year")
#             plt.ylabel("Debt-to-GDP (%)")
#             plt.grid()
#             plt.savefig(save_path)
#             plt.close()

#         elif graph_type == "program_spending":
#             sectors = data["sectors"]
#             spending = data["spending"]
#             plt.figure(figsize=(8, 5))
#             plt.bar(sectors, spending, color='lightblue')
#             plt.title("Program-Specific Spending")
#             plt.xlabel("Sector")
#             plt.ylabel("Spending (Billions CAD)")
#             plt.grid(axis='y')
#             plt.savefig(save_path)
#             plt.close()

#         else:
#             raise ValueError(f"Unsupported graph type: {graph_type}")

#         print(f"Generated graph: {save_path}")
#         return save_path

#     except Exception as e:
#         print(f"Error generating graph {graph_type}: {e}")
#         raise Exception(f"Graph generation failed for {graph_type}")
