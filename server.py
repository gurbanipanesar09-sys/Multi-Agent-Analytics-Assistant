try:
    from mcp.server.fastmcp import FastMCP
except Exception:
    FastMCP = None

from .tools.csv_profile_tools import mcp_profile_csv
from .tools.data_quality_tools import mcp_detect_data_quality_issues
from .tools.kpi_tools import mcp_generate_kpi_catalog
from .tools.ml_tools import (
    mcp_recommend_ml_use_cases,
    mcp_feature_engineering_suggestions
)
from .tools.report_tools import mcp_generate_report_markdown
from mcp_server.tools.data_quality_tools import mcp_detect_data_quality_issues
from mcp_server.tools.kpi_tools import mcp_generate_kpi_catalog
from mcp_server.tools.ml_tools import (
    mcp_recommend_ml_use_cases,
    mcp_feature_engineering_suggestions,
)
from mcp_server.tools.report_tools import mcp_generate_report_markdown


if FastMCP is not None:
    mcp = FastMCP("analytics_mcp_server")

    mcp.tool()(mcp_profile_csv)
    mcp.tool()(mcp_detect_data_quality_issues)
    mcp.tool()(mcp_generate_kpi_catalog)
    mcp.tool()(mcp_recommend_ml_use_cases)
    mcp.tool()(mcp_feature_engineering_suggestions)
    mcp.tool()(mcp_generate_report_markdown)


if __name__ == "__main__":
    if FastMCP is None:
        print("MCP package not available, but tools are importable.")
    else:
        print("analytics_mcp_server running...")
        mcp.run()