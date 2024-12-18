from fastapi import FastAPI, HTTPException
from models.inputs import ReportRequest
from models.outputs import ReportOutput
from services.data_fetcher import DataFetcher
from services.graph_generator import generate_graph
from services.report_builder import generate_markdown_report
from services.cache_manager import CacheManager
import openai
import os

# Initialize FastAPI
app = FastAPI(title="Canadian Financial Watchdog API")

# Initialize Redis Cache on startup
@app.on_event("startup")
async def startup():
    CacheManager.initialize_cache()

@app.post("/generate-report", response_model=ReportOutput)
async def generate_financial_report(request: ReportRequest):

    # Validate inputs
    if request.government_level not in ["Province", "Federal"]:
        raise HTTPException(status_code=400, detail="Invalid government level")

    try:
        # Fetch financial data and metrics
        budget_data = DataFetcher.get_budget_data(request.government_level, request.province)
        gdp_data = DataFetcher.fetch_economic_data("gdp_growth")
        inflation_data = DataFetcher.fetch_economic_data("inflation_rate")
        employment_data = DataFetcher.fetch_economic_data("employment_growth")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Generate graphs using fetched data
    graphs = [
        generate_graph("net_debt", {"years": budget_data["years"], "net_debt": budget_data["net_debt"]}),
        generate_graph("gdp_growth", {"years": gdp_data["years"], "gdp_growth": gdp_data["values"]}),
        generate_graph("inflation_rate", {"months": inflation_data["months"], "inflation_rate": inflation_data["values"]}),
        generate_graph("employment_growth", {"years": employment_data["years"], "employment_growth": employment_data["values"]}),
    ]

    # Generate tables based on fetched data
    tables = [
        {
            "Fiscal Year": year,
            "Revenue": f"{budget_data['revenue'][i]}B",
            "Expenses": f"{budget_data['expenses'][i]}B",
            "Surplus/Deficit": f"{budget_data['deficit'][i]}B"
        } for i, year in enumerate(budget_data["years"])
    ]

    # Generate Markdown report
    report_file = generate_markdown_report(
        {
            "report_title": f"Financial Report: {request.government_level} - {request.province or 'Canada'}",
            "report_content": "Generated using real-time government and economic data.",
            "user_name": request.user_name,
            "company_email": request.company_email,
        },
        graphs, tables
    )

    return ReportOutput(
        file_path=report_file,
        graphs=graphs,
        tables=tables
    )
