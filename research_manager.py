from agents import Runner, trace, gen_trace_id
from search_agent import search_agent
from planner_agent import planner_agent, WebSearchItem, WebSearchPlan
from writer_agent import writer_agent, ReportData
from clarification_agent import clarification_agent, ClarificationResult
import asyncio


class ResearchManager:

    async def clarify_query(self, query: str) -> ClarificationResult:
        """Check whether the research query needs clarification."""

        result = await Runner.run(
            clarification_agent,
            f"Query: {query}"
        )

        return result.final_output

    async def run(self, query: str):
        """Run the deep research process."""

        trace_id = gen_trace_id()

        with trace("Research trace", trace_id=trace_id):

            yield f"Starting research. Trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"

            yield "Planning searches..."

            search_plan = await self.plan_searches(query)

            yield f"Searches planned, starting {len(search_plan.searches)} searches..."

            search_results = await self.perform_searches(search_plan)

            yield "Searches complete, writing report..."

            report = await self.write_report(query, search_results)

            yield "Report written, research complete."

            yield report.markdown_report

    async def plan_searches(self, query: str) -> WebSearchPlan:
        """Plan the searches to perform for the query."""

        result = await Runner.run(
            planner_agent,
            f"Query: {query}"
        )

        return result.final_output

    async def perform_searches(
        self,
        search_plan: WebSearchPlan
    ) -> list[str]:
        """Perform all planned searches in parallel."""

        tasks = [
            self.search(item)
            for item in search_plan.searches
        ]

        return await asyncio.gather(*tasks)

    async def search(self, item: WebSearchItem) -> str | None:
        """Perform a single web search."""

        input_message = (
            f"Search term: {item.query}\n"
            f"Reason for searching: {item.reason}"
        )

        result = await Runner.run(
            search_agent,
            input_message
        )

        return result.final_output

    async def write_report(
        self,
        query: str,
        search_results: list[str]
    ) -> ReportData:
        """Write the final research report."""

        input_message = (
            f"Original query: {query}\n"
            f"Summarized search results: {search_results}"
        )

        result = await Runner.run(
            writer_agent,
            input_message
        )

        return result.final_output