import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager
from styles import CSS, JS, EXAMPLES, HEADER_HTML
import os

load_dotenv(override=True)

print("STEP 1: Starting application...")

manager = ResearchManager()

print("STEP 2: ResearchManager created...")


def format_status(msg: str) -> str:
    return f"""<div class="dr-status-box"><div class="dr-status-spinner"></div><div class="dr-status-info"><div class="dr-status-title">{msg}</div><div class="dr-status-sub">Autonomous Investigation Active • Live Output Below</div></div></div>"""


async def handle_investigate(query: str):
    if not query or not query.strip():
        yield (
            gr.update(visible=False),
            "",
            "",
            "Continue Research with Answers",
            gr.update(
                value=format_status("⚠️ Please enter a research question first."),
                visible=True
            ),
        )
        return

    # Instant feedback while checking clarification
    yield (
        gr.update(visible=False),
        "",
        "",
        "Continue Research with Answers",
        gr.update(
            value=format_status("⏳ Analyzing query for clarification..."),
            visible=True
        ),
    )

    clarification = await manager.clarify_query(query)

    if clarification.needs_clarification and clarification.questions:

        questions_fmt = "\n\n".join(
            f"{i}. **{q}**"
            for i, q in enumerate(clarification.questions, 1)
        )

        msg = (
            f"### 💡 Recommended Clarification Questions:\n\n"
            f"{questions_fmt}\n\n"
            f"*Type your answers in the box below to guide the research.*"
        )

        yield (
            gr.update(visible=True),
            msg,
            "",
            "Continue Research with Answers",
            gr.update(value="", visible=False),
        )

    else:

        # If no clarifications needed -> Directly start deep research
        yield (
            gr.update(visible=False),
            "",
            "",
            "Continue Research with Answers",
            gr.update(
                value=format_status("🚀 Starting deep research..."),
                visible=True
            ),
        )

        async for status_update in manager.run(query):

            if status_update.startswith("#"):
                out_val = status_update
            else:
                out_val = format_status(status_update)

            yield (
                gr.update(visible=False),
                "",
                "",
                "Continue Research with Answers",
                gr.update(
                    value=out_val,
                    visible=True
                ),
            )


async def start_research_with_details(query: str, answers: str):

    yield (
        gr.update(visible=False),
        "",
        "",
        "Continue Research with Answers",
        gr.update(
            value=format_status("🚀 Starting deep research..."),
            visible=True
        ),
    )

    if answers and answers.strip():

        final_query = f"""Original research query:
{query}

User specified answers & additional requirements:
{answers}"""

    else:
        final_query = query

    async for status_update in manager.run(final_query):

        if status_update.startswith("#"):
            out_val = status_update
        else:
            out_val = format_status(status_update)

        yield (
            gr.update(visible=False),
            "",
            "",
            "Continue Research with Answers",
            gr.update(
                value=out_val,
                visible=True
            ),
        )


async def start_research_direct(query: str):

    yield (
        gr.update(visible=False),
        "",
        "",
        "Continue Research with Answers",
        gr.update(
            value=format_status("🚀 Starting deep research..."),
            visible=True
        ),
    )

    async for status_update in manager.run(query):

        if status_update.startswith("#"):
            out_val = status_update
        else:
            out_val = format_status(status_update)

        yield (
            gr.update(visible=False),
            "",
            "",
            "Continue Research with Answers",
            gr.update(
                value=out_val,
                visible=True
            ),
        )


with gr.Blocks(title="Deep Research") as ui:

    gr.HTML(HEADER_HTML)

    with gr.Row(elem_classes="dr-query-row"):

        query_textbox = gr.Textbox(
            placeholder="Type a research question...",
            show_label=False,
            container=False,
            autofocus=True,
            elem_id="dr-query",
            scale=5,
        )

        run_button = gr.Button(
            "Investigate",
            variant="primary",
            elem_id="dr-run",
            scale=1,
        )

    gr.HTML('<div class="dr-examples-label">Try one</div>')

    gr.Examples(
        examples=EXAMPLES,
        inputs=query_textbox,
        elem_id="dr-examples",
    )

    # --------------------------------------------------
    # Clarification Box
    # --------------------------------------------------

    with gr.Column(
        visible=False,
        elem_id="dr-clarification-box"
    ) as clarification_box:

        clarification_display = gr.Markdown(
            elem_id="dr-clarification",
        )

        answers_textbox = gr.Textbox(
            label="Your Answers & Additional Requirements",
            placeholder="Type your answers to the questions above or enter additional guidelines...",
            lines=4,
            container=False,
            elem_id="dr-answers",
        )

        with gr.Row():

            continue_button = gr.Button(
                "Continue Research with Answers",
                variant="primary",
                elem_id="dr-continue",
            )

            skip_button = gr.Button(
                "Skip & Start Research",
                variant="secondary",
                elem_id="dr-skip",
            )

    # Final report / research status markdown

    report = gr.Markdown(
        elem_id="dr-report"
    )

    # --------------------------------------------------
    # Event Handlers
    # --------------------------------------------------

    run_button.click(
        handle_investigate,
        inputs=query_textbox,
        outputs=[
            clarification_box,
            clarification_display,
            answers_textbox,
            continue_button,
            report,
        ],
    )

    query_textbox.submit(
        handle_investigate,
        inputs=query_textbox,
        outputs=[
            clarification_box,
            clarification_display,
            answers_textbox,
            continue_button,
            report,
        ],
    )

    continue_button.click(
        start_research_with_details,
        inputs=[
            query_textbox,
            answers_textbox,
        ],
        outputs=[
            clarification_box,
            clarification_display,
            answers_textbox,
            continue_button,
            report,
        ],
    )

    skip_button.click(
        start_research_direct,
        inputs=query_textbox,
        outputs=[
            clarification_box,
            clarification_display,
            answers_textbox,
            continue_button,
            report,
        ],
    )


if __name__ == "__main__":

    print("STEP 3: Entering main...")

    port = int(os.environ.get("PORT", 10000))

    print(f"STEP 4: Starting Gradio on 0.0.0.0:{port}")

    ui.launch(
        server_name="0.0.0.0",
        server_port=port,
        css=CSS,
        js=JS,
        theme=gr.themes.Base(),
    )
