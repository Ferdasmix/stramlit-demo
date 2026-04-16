"""
Streamlit Feature Explorer
--------------------------
A live reference demo for every major Streamlit element.
Each feature is shown in action with a code snippet.

Run:
    pip install -r requirements.txt
    streamlit run app.py
"""

import time
from datetime import date, time as dtime

import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Streamlit Feature Explorer",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Shared sample data ────────────────────────────────────────────────────────
np.random.seed(42)
SAMPLE_DF = pd.DataFrame(
    {
        "Name": ["Alice", "Bob", "Carol", "Dave", "Eve"],
        "Score": np.random.randint(60, 100, 5),
        "Revenue ($)": np.random.uniform(1000, 9000, 5).round(2),
        "Active": np.random.choice([True, False], 5),
    }
)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("🧪 Feature Explorer")
    st.info(
        "A live demo + code snippet for every major Streamlit element.\n\n"
        "Click through the tabs above to explore each category."
    )
    st.divider()
    st.subheader("Tabs in this demo")
    st.markdown(
        """
1. 📝 **Text** — titles, markdown, LaTeX, code blocks
2. 📊 **Data Display** — dataframe, table, metric, JSON
3. 📈 **Charts** — line, bar, scatter, Plotly, Altair, map
4. 🎛️ **Widgets** — every input element
5. 🗂️ **Layout** — columns, expanders, containers, popovers
6. 🔔 **Status** — alerts, progress, spinner, balloons
7. 📋 **Forms** — batched submit, form_submit_button
8. 🧠 **State & Cache** — session_state, cache_data, cache_resource
9. 💬 **Chat** — chat_message, chat_input, write_stream
"""
    )
    st.divider()
    st.caption("All data is generated in-memory — no external files needed.")

# ── Tabs ──────────────────────────────────────────────────────────────────────
tabs = st.tabs(
    [
        "📝 Text",
        "📊 Data Display",
        "📈 Charts",
        "🎛️ Widgets",
        "🗂️ Layout",
        "🔔 Status",
        "📋 Forms",
        "🧠 State & Cache",
        "💬 Chat",
    ]
)

# ─────────────────────────────────────────────────────────────────────────────
# TAB 1 — TEXT & TYPOGRAPHY
# ─────────────────────────────────────────────────────────────────────────────
with tabs[0]:
    st.header("Text & Typography", divider="rainbow")
    st.markdown(
        "These elements let you write textual content — from page titles and "
        "section headers to rich Markdown, math equations, and syntax-highlighted code."
    )

    # ── st.title ──
    st.subheader("`st.title()`")
    st.caption(
        "Displays a large page-level title. Typically used **once** at the very top "
        "of an app to identify it."
    )
    st.title("I am a st.title()")
    st.code("st.title('I am a st.title()')", language="python")
    st.divider()

    # ── st.header ──
    st.subheader("`st.header()`")
    st.caption(
        "Section-level heading. Supports the `divider` parameter for a colored "
        "horizontal rule (`'blue'`, `'rainbow'`, `'orange'`, …)."
    )
    st.header("I am a st.header()", divider="blue")
    st.code("st.header('I am a st.header()', divider='blue')", language="python")
    st.divider()

    # ── st.subheader ──
    st.subheader("`st.subheader()`")
    st.caption("Sub-section heading — smaller than `st.header`, larger than body text.")
    st.subheader("I am a st.subheader()")
    st.code("st.subheader('I am a st.subheader()')", language="python")
    st.divider()

    # ── st.text ──
    st.subheader("`st.text()`")
    st.caption(
        "Fixed-width monospace text. No Markdown rendering. "
        "Good for pre-formatted output, logs, or simple labels."
    )
    st.text("Fixed-width. No **markdown**. Just plain text.")
    st.code("st.text('Fixed-width. No **markdown**. Just plain text.')", language="python")
    st.divider()

    # ── st.markdown ──
    st.subheader("`st.markdown()`")
    st.caption(
        "Renders GitHub-flavored Markdown: bold, italic, links, tables, lists, "
        "inline code, and even raw HTML (with `unsafe_allow_html=True`)."
    )
    st.markdown(
        "**Bold**, *italic*, `inline code`, [a link](https://streamlit.io)\n\n"
        "| Column A | Column B |\n|---|---|\n| 1 | alpha |\n| 2 | beta |"
    )
    st.code(
        'st.markdown("**Bold**, *italic*, `code`, [link](https://streamlit.io)\\n\\n'
        '| A | B |\\n|---|---|\\n| 1 | alpha |")',
        language="python",
    )
    st.divider()

    # ── st.caption ──
    st.subheader("`st.caption()`")
    st.caption(
        "Small muted text. Perfect for footnotes, hints, image captions, or "
        "supplementary information that shouldn't compete visually with main content."
    )
    st.caption("← This line itself is rendered with st.caption().")
    st.code("st.caption('Small muted helper text.')", language="python")
    st.divider()

    # ── st.code ──
    st.subheader("`st.code()`")
    st.caption(
        "Syntax-highlighted code block with a copy button. "
        "Supports Python, SQL, JSON, Bash, and dozens of other languages."
    )
    st.code(
        "def greet(name: str) -> str:\n    return f'Hello, {name}!'\n\nprint(greet('World'))",
        language="python",
    )
    st.code(
        "st.code(\"def greet(name):\\n    return f'Hello, {name}!'\", language='python')",
        language="python",
    )
    st.divider()

    # ── st.latex ──
    st.subheader("`st.latex()`")
    st.caption(
        "Renders LaTeX math using KaTeX. Great for scientific, statistical, "
        "or academic apps that need proper equation formatting."
    )
    st.latex(
        r"E = mc^2 \qquad \text{and} \qquad "
        r"\int_0^\infty e^{-x^2}\,dx = \frac{\sqrt{\pi}}{2}"
    )
    st.code(
        r"st.latex(r'E = mc^2 \qquad \int_0^\infty e^{-x^2}\,dx = \frac{\sqrt{\pi}}{2}')",
        language="python",
    )
    st.divider()

    # ── st.divider ──
    st.subheader("`st.divider()`")
    st.caption(
        "Draws a horizontal rule to visually separate sections. "
        "Equivalent to `st.markdown('---')`."
    )
    st.divider()
    st.code("st.divider()", language="python")


# ─────────────────────────────────────────────────────────────────────────────
# TAB 2 — DATA DISPLAY
# ─────────────────────────────────────────────────────────────────────────────
with tabs[1]:
    st.header("Data Display", divider="rainbow")
    st.markdown(
        "Show tabular data, key performance metrics, and structured JSON — "
        "from fully interactive tables to simple static grids."
    )

    # ── st.dataframe ──
    st.subheader("`st.dataframe()`")
    st.caption(
        "Interactive table with sorting, column resizing, full-text search, and a "
        "built-in CSV download button. Supports rich `column_config` options "
        "(progress bars, image URLs, number formats, checkboxes, etc.)."
    )
    st.dataframe(
        SAMPLE_DF,
        use_container_width=True,
        column_config={
            "Score": st.column_config.ProgressColumn(
                "Score", min_value=0, max_value=100, format="%d pts"
            ),
            "Revenue ($)": st.column_config.NumberColumn(
                "Revenue ($)", format="$%.2f"
            ),
            "Active": st.column_config.CheckboxColumn("Active?"),
        },
    )
    st.code(
        """st.dataframe(
    df,
    use_container_width=True,
    column_config={
        "Score":      st.column_config.ProgressColumn("Score", min_value=0, max_value=100),
        "Revenue ($)": st.column_config.NumberColumn("Revenue ($)", format="$%.2f"),
        "Active":     st.column_config.CheckboxColumn("Active?"),
    },
)""",
        language="python",
    )
    st.divider()

    # ── st.table ──
    st.subheader("`st.table()`")
    st.caption(
        "Static, non-interactive table. No sorting or resizing — renders exactly as-is. "
        "Good when you just need to display a small DataFrame without any UI chrome."
    )
    st.table(SAMPLE_DF.head(3))
    st.code("st.table(df.head(3))", language="python")
    st.divider()

    # ── st.metric ──
    st.subheader("`st.metric()`")
    st.caption(
        "KPI card widget. Shows a **label**, a large **value**, and an optional "
        "**delta** with an up/down arrow and green/red coloring. "
        "Pass `delta_color='inverse'` to flip the color logic (useful for costs)."
    )
    mc1, mc2, mc3 = st.columns(3)
    mc1.metric("Total Users", "1,234", delta="+12%")
    mc2.metric("Monthly Cost", "$8,420", delta="+3.2%", delta_color="inverse")
    mc3.metric("Uptime", "99.97%", delta="0.01%")
    st.code(
        """col1, col2, col3 = st.columns(3)
col1.metric("Total Users",  "1,234",  delta="+12%")
col2.metric("Monthly Cost", "$8,420", delta="+3.2%", delta_color="inverse")
col3.metric("Uptime",       "99.97%", delta="0.01%")""",
        language="python",
    )
    st.divider()

    # ── st.json ──
    st.subheader("`st.json()`")
    st.caption(
        "Renders a collapsible, syntax-highlighted JSON tree viewer. "
        "Accepts dicts, lists, or raw JSON strings. "
        "Use `expanded=False` to start collapsed."
    )
    sample_json = {
        "model": "streamlit",
        "version": "1.35",
        "features": ["tabs", "widgets", "charts", "chat"],
        "meta": {"author": "You", "year": 2024},
    }
    st.json(sample_json)
    st.code(
        'st.json({"model": "streamlit", "features": ["tabs", "widgets"], "meta": {...}})',
        language="python",
    )


# ─────────────────────────────────────────────────────────────────────────────
# TAB 3 — CHARTS
# ─────────────────────────────────────────────────────────────────────────────
with tabs[2]:
    st.header("Charts", divider="rainbow")
    st.markdown(
        "Native one-liner chart helpers plus full integrations with "
        "Matplotlib, Plotly, and Altair. All data is generated in-memory."
    )

    # Shared time series data
    np.random.seed(7)
    dates = pd.date_range("2024-01-01", periods=30)
    ts_df = pd.DataFrame(
        {
            "Series A": np.cumsum(np.random.randn(30)) + 50,
            "Series B": np.cumsum(np.random.randn(30)) + 40,
            "Series C": np.cumsum(np.random.randn(30)) + 45,
        },
        index=dates,
    )

    # ── st.line_chart ──
    st.subheader("`st.line_chart()`")
    st.caption(
        "Quickest way to draw a line chart from a DataFrame or dict. "
        "Auto-detects columns as separate series. Interactive zoom and pan built in."
    )
    st.line_chart(ts_df)
    st.code("st.line_chart(df)  # index = x-axis, columns = series", language="python")
    st.divider()

    # ── st.area_chart ──
    st.subheader("`st.area_chart()`")
    st.caption(
        "Filled area chart. Good for showing volume, cumulative sums, "
        "or stacked totals over time."
    )
    st.area_chart(ts_df)
    st.code("st.area_chart(df)", language="python")
    st.divider()

    # ── st.bar_chart ──
    st.subheader("`st.bar_chart()`")
    st.caption(
        "Vertical bar chart. Best for categorical comparisons or small time series. "
        "Pass `horizontal=True` for horizontal bars."
    )
    bar_df = pd.DataFrame(
        {"Sales": [120, 95, 140, 80, 160, 110]},
        index=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
    )
    st.bar_chart(bar_df)
    st.code(
        "bar_df = pd.DataFrame({'Sales': [120, 95, 140, 80, 160]},\n"
        "                       index=['Mon','Tue','Wed','Thu','Fri'])\n"
        "st.bar_chart(bar_df)",
        language="python",
    )
    st.divider()

    # ── st.scatter_chart ──
    st.subheader("`st.scatter_chart()`")
    st.caption(
        "Scatter plot with optional `size` and `color` columns. "
        "Useful for exploring correlations or cluster distributions."
    )
    sc_df = pd.DataFrame(
        {
            "x": np.random.randn(60),
            "y": np.random.randn(60),
            "size": np.random.randint(20, 120, 60),
        }
    )
    st.scatter_chart(sc_df, x="x", y="y", size="size")
    st.code(
        "st.scatter_chart(df, x='x', y='y', size='size')", language="python"
    )
    st.divider()

    # ── st.pyplot ──
    st.subheader("`st.pyplot()`")
    st.caption(
        "Renders any Matplotlib `Figure`. Full Matplotlib API access — "
        "histograms, subplots, custom styles, annotations."
    )
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.hist(np.random.randn(1000), bins=35, color="steelblue", edgecolor="white", alpha=0.85)
    ax.set_title("Matplotlib Histogram (st.pyplot)")
    ax.set_xlabel("Value")
    ax.set_ylabel("Count")
    st.pyplot(fig)
    plt.close(fig)
    st.code(
        "fig, ax = plt.subplots()\nax.hist(data, bins=35)\nst.pyplot(fig)",
        language="python",
    )
    st.divider()

    # ── st.plotly_chart ──
    st.subheader("`st.plotly_chart()`")
    st.caption(
        "Interactive Plotly chart with zoom, pan, hover tooltips, "
        "legend toggle, and PNG/SVG download. "
        "Supports all Plotly Express and Graph Objects figures."
    )
    p_df = pd.DataFrame(
        {
            "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            "Sales": [120, 95, 140, 80, 160, 130],
            "Returns": [10, 8, 15, 6, 20, 11],
        }
    )
    fig2 = px.line(
        p_df, x="Month", y=["Sales", "Returns"],
        title="Sales vs Returns — Plotly Interactive", markers=True,
    )
    st.plotly_chart(fig2, use_container_width=True)
    st.code(
        "import plotly.express as px\n"
        "fig = px.line(df, x='Month', y=['Sales','Returns'], markers=True)\n"
        "st.plotly_chart(fig, use_container_width=True)",
        language="python",
    )
    st.divider()

    # ── st.altair_chart ──
    st.subheader("`st.altair_chart()`")
    st.caption(
        "Vega-Lite charts via the Altair library. Declarative grammar — "
        "great for linked/brushed interactive views and composable specs."
    )
    alt_df = pd.DataFrame(
        {"x": range(25), "y": np.random.randn(25).cumsum()}
    )
    altair_c = (
        alt.Chart(alt_df)
        .mark_line(point=True)
        .encode(x="x:Q", y="y:Q", tooltip=["x", "y"])
        .properties(title="Altair Line Chart", width=600, height=250)
        .interactive()
    )
    st.altair_chart(altair_c, use_container_width=True)
    st.code(
        "import altair as alt\n"
        "chart = alt.Chart(df).mark_line(point=True)\\\n"
        "    .encode(x='x:Q', y='y:Q').interactive()\n"
        "st.altair_chart(chart, use_container_width=True)",
        language="python",
    )
    st.divider()

    # ── st.map ──
    st.subheader("`st.map()`")
    st.caption(
        "Quick geographic scatter map using `lat` / `lon` columns. "
        "No API key required. Based on Deck.gl."
    )
    map_df = pd.DataFrame(
        {
            "lat": [40.7128, 34.0522, 41.8781, 29.7604, 33.4484, 47.6062],
            "lon": [-74.0060, -118.2437, -87.6298, -95.3698, -112.0740, -122.3321],
        }
    )
    st.map(map_df)
    st.code(
        'map_df = pd.DataFrame({"lat": [40.71, 34.05], "lon": [-74.00, -118.24]})\n'
        "st.map(map_df)",
        language="python",
    )


# ─────────────────────────────────────────────────────────────────────────────
# TAB 4 — INPUT WIDGETS
# ─────────────────────────────────────────────────────────────────────────────
with tabs[3]:
    st.header("Input Widgets", divider="rainbow")
    st.markdown(
        "Every widget that accepts user input. "
        "All values are reactive — the **→ value** line updates live on every interaction."
    )

    left, right = st.columns([3, 1], gap="large")

    with right:
        st.info(
            "**How reactivity works**\n\n"
            "Every widget change causes Streamlit to re-run the entire script "
            "from top to bottom. The widget returns its *current* value, so the "
            "`→ value` lines below always reflect what you last set."
        )

    with left:
        # ── st.button ──
        st.subheader("`st.button()`")
        st.caption(
            "A momentary trigger. Returns `True` **only on the rerun** "
            "caused by the click, then resets to `False`."
        )
        clicked = st.button("Click me!")
        st.write(f"→ value: `{clicked}`")
        st.code("clicked = st.button('Click me!')", language="python")
        st.divider()

        # ── st.download_button ──
        st.subheader("`st.download_button()`")
        st.caption(
            "Triggers a browser file download. Data can be a string, bytes, "
            "or any file-like object. The browser never navigates away."
        )
        st.download_button(
            "⬇ Download sample CSV",
            data=SAMPLE_DF.to_csv(index=False),
            file_name="sample.csv",
            mime="text/csv",
        )
        st.code(
            'st.download_button("Download CSV", data=csv_str,\n'
            '    file_name="data.csv", mime="text/csv")',
            language="python",
        )
        st.divider()

        # ── st.link_button ──
        st.subheader("`st.link_button()`")
        st.caption(
            "Opens a URL in a new browser tab. Looks like a button but is "
            "semantically a navigation link — no Python callback runs."
        )
        st.link_button("Open Streamlit docs", url="https://docs.streamlit.io")
        st.code(
            'st.link_button("Open docs", url="https://docs.streamlit.io")',
            language="python",
        )
        st.divider()

        # ── st.checkbox ──
        st.subheader("`st.checkbox()`")
        st.caption("Boolean toggle rendered as a checkbox. Returns `True` or `False`.")
        chk = st.checkbox("Enable feature X")
        st.write(f"→ value: `{chk}`")
        st.code("chk = st.checkbox('Enable feature X')", language="python")
        st.divider()

        # ── st.toggle ──
        st.subheader("`st.toggle()`")
        st.caption(
            "Boolean toggle rendered as a slide switch. "
            "Same return value as `st.checkbox`, different visual style."
        )
        tog = st.toggle("Dark mode")
        st.write(f"→ value: `{tog}`")
        st.code("tog = st.toggle('Dark mode')", language="python")
        st.divider()

        # ── st.radio ──
        st.subheader("`st.radio()`")
        st.caption(
            "Single-choice selector shown as radio buttons. "
            "Pass `horizontal=True` to lay options side by side."
        )
        rad = st.radio("Pick a plan", ["Free", "Pro", "Enterprise"], horizontal=True)
        st.write(f"→ value: `{rad!r}`")
        st.code(
            "rad = st.radio('Pick a plan', ['Free','Pro','Enterprise'], horizontal=True)",
            language="python",
        )
        st.divider()

        # ── st.selectbox ──
        st.subheader("`st.selectbox()`")
        st.caption(
            "Dropdown single-choice selector. Best for long option lists "
            "where radio buttons would take too much space."
        )
        sel = st.selectbox(
            "Choose a country",
            ["Argentina", "Brazil", "Canada", "Denmark", "Egypt", "France"],
        )
        st.write(f"→ value: `{sel!r}`")
        st.code(
            "sel = st.selectbox('Choose a country', ['Argentina', 'Brazil', ...])",
            language="python",
        )
        st.divider()

        # ── st.multiselect ──
        st.subheader("`st.multiselect()`")
        st.caption(
            "Multi-choice dropdown. Returns a **list** of selected items. "
            "Supports `default` and `max_selections`."
        )
        multi = st.multiselect(
            "Select features",
            ["Charts", "Widgets", "Forms", "Chat", "Caching", "Maps"],
            default=["Charts", "Widgets"],
        )
        st.write(f"→ value: `{multi}`")
        st.code(
            "multi = st.multiselect('Select features', options, default=['Charts'])",
            language="python",
        )
        st.divider()

        # ── st.slider ──
        st.subheader("`st.slider()`")
        st.caption(
            "Numeric or date range slider. Pass a tuple `(min, max)` as `value` "
            "to create a **range slider** with two handles."
        )
        sli = st.slider("Pick a range", min_value=0, max_value=100, value=(20, 80))
        st.write(f"→ value: `{sli}`")
        st.code("sli = st.slider('Pick a range', 0, 100, (20, 80))", language="python")
        st.divider()

        # ── st.select_slider ──
        st.subheader("`st.select_slider()`")
        st.caption(
            "Slider over a **fixed list** of options — not numeric. "
            "Good for ordered categories or discrete steps."
        )
        ss = st.select_slider("Quality", options=["Low", "Medium", "High", "Ultra"])
        st.write(f"→ value: `{ss!r}`")
        st.code(
            "ss = st.select_slider('Quality', options=['Low','Medium','High','Ultra'])",
            language="python",
        )
        st.divider()

        # ── st.text_input ──
        st.subheader("`st.text_input()`")
        st.caption(
            "Single-line text field. Supports `placeholder`, `max_chars`, "
            "and `type='password'` for masked input."
        )
        ti = st.text_input("Your name", placeholder="Type here…")
        st.write(f"→ value: `{ti!r}`")
        st.code(
            "ti = st.text_input('Your name', placeholder='Type here…')",
            language="python",
        )
        st.divider()

        # ── st.number_input ──
        st.subheader("`st.number_input()`")
        st.caption(
            "Numeric field with ＋/− stepper buttons. "
            "Supports `int` and `float`, `min_value`, `max_value`, and `step`."
        )
        ni = st.number_input("Enter a number", min_value=0, max_value=1000, value=42, step=1)
        st.write(f"→ value: `{ni}`")
        st.code(
            "ni = st.number_input('Enter a number', min_value=0, max_value=1000, value=42)",
            language="python",
        )
        st.divider()

        # ── st.text_area ──
        st.subheader("`st.text_area()`")
        st.caption(
            "Multi-line text input. User-resizable. "
            "Use for notes, prompts, JSON snippets, or any long-form text."
        )
        ta = st.text_area("Write a note", height=100, placeholder="Your text here…")
        st.write(f"→ length: `{len(ta)}` chars")
        st.code("ta = st.text_area('Write a note', height=100)", language="python")
        st.divider()

        # ── st.date_input ──
        st.subheader("`st.date_input()`")
        st.caption(
            "Calendar date picker. Returns a `datetime.date`. "
            "Pass a tuple `(start, end)` as `value` for a **date range** picker."
        )
        di = st.date_input("Pick a date", value=date.today())
        st.write(f"→ value: `{di}`")
        st.code("di = st.date_input('Pick a date', value=date.today())", language="python")
        st.divider()

        # ── st.time_input ──
        st.subheader("`st.time_input()`")
        st.caption(
            "Time picker. Returns a `datetime.time` object. "
            "Use `step` (in seconds) to control granularity."
        )
        tmi = st.time_input("Pick a time", value=dtime(9, 0))
        st.write(f"→ value: `{tmi}`")
        st.code("tmi = st.time_input('Pick a time', value=time(9, 0))", language="python")
        st.divider()

        # ── st.file_uploader ──
        st.subheader("`st.file_uploader()`")
        st.caption(
            "Drag-and-drop or click-to-browse file upload. "
            "Returns a `UploadedFile` object (file-like). "
            "Pass `accept_multiple_files=True` for multi-upload."
        )
        uploaded = st.file_uploader("Upload a CSV", type=["csv", "txt"])
        if uploaded:
            st.write(f"→ uploaded: `{uploaded.name}` ({uploaded.size:,} bytes)")
        else:
            st.write("→ value: `None`")
        st.code(
            "uploaded = st.file_uploader('Upload a CSV', type=['csv'])\n"
            "if uploaded:\n    df = pd.read_csv(uploaded)",
            language="python",
        )
        st.divider()

        # ── st.color_picker ──
        st.subheader("`st.color_picker()`")
        st.caption(
            "Color picker dialog. Returns a hex color string like `#FF4B4B`. "
            "The chosen color can be passed directly to matplotlib, plotly, or CSS."
        )
        cp = st.color_picker("Pick a color", "#FF4B4B")
        st.markdown(
            f'<div style="width:80px;height:32px;background:{cp};'
            f'border-radius:6px;border:1px solid #ccc;margin-bottom:4px"></div>',
            unsafe_allow_html=True,
        )
        st.write(f"→ value: `{cp}`")
        st.code("cp = st.color_picker('Pick a color', '#FF4B4B')", language="python")


# ─────────────────────────────────────────────────────────────────────────────
# TAB 5 — LAYOUT & STRUCTURE
# ─────────────────────────────────────────────────────────────────────────────
with tabs[4]:
    st.header("Layout & Structure", divider="rainbow")
    st.markdown(
        "Arrange, group, and reveal content using columns, expanders, "
        "containers, popovers, and the sidebar."
    )

    # ── st.columns ──
    st.subheader("`st.columns()`")
    st.caption(
        "Divides the horizontal space into N equal columns, or pass a list of "
        "relative widths (e.g. `[3, 1]`). Any Streamlit element can go inside a column."
    )
    lc1, lc2, lc3 = st.columns(3)
    lc1.info("Column 1 — `st.info`")
    lc2.success("Column 2 — `st.success`")
    lc3.warning("Column 3 — `st.warning`")
    st.code(
        "c1, c2, c3 = st.columns(3)\nc1.info('...')\nc2.success('...')\nc3.warning('...')",
        language="python",
    )

    la, lb = st.columns([3, 1])
    la.write("Wide column — ratio 3")
    lb.write("Narrow — ratio 1")
    st.code("wide, narrow = st.columns([3, 1])", language="python")
    st.divider()

    # ── st.expander ──
    st.subheader("`st.expander()`")
    st.caption(
        "Collapsible section. Hidden until the user clicks to expand. "
        "Great for advanced settings, lengthy details, or secondary information."
    )
    with st.expander("Click to expand", expanded=False):
        st.write("Hidden content revealed! You can put any widget or element in here.")
        st.bar_chart({"A": 3, "B": 5, "C": 2})
    st.code(
        "with st.expander('Click to expand', expanded=False):\n    st.write('...')",
        language="python",
    )
    st.divider()

    # ── st.container ──
    st.subheader("`st.container()`")
    st.caption(
        "A logical grouping block. Can have a visible `border`, "
        "and lets you write to a named region **out of order** "
        "(assign it first, fill it later in the script)."
    )
    with st.container(border=True):
        st.write("Inside a bordered `st.container()`.")
        st.caption("Useful for visually grouping related widgets or content.")
    st.code(
        "with st.container(border=True):\n    st.write('Inside container')",
        language="python",
    )
    st.divider()

    # ── st.empty ──
    st.subheader("`st.empty()`")
    st.caption(
        "A **single-slot** placeholder that can be overwritten at any time. "
        "Use it for live updates, progress countdowns, or replacing content dynamically."
    )
    if st.button("Run 3-second countdown", key="countdown_btn"):
        ph = st.empty()
        for i in range(3, 0, -1):
            ph.metric("Countdown", f"{i}…")
            time.sleep(1)
        ph.success("Done! The placeholder was overwritten each second.")
    st.code(
        "ph = st.empty()\nfor i in range(3, 0, -1):\n    ph.metric('Countdown', f'{i}…')\n"
        "    time.sleep(1)\nph.success('Done!')",
        language="python",
    )
    st.divider()

    # ── st.popover ──
    st.subheader("`st.popover()`")
    st.caption(
        "A button that opens a floating overlay anchored to the button. "
        "Any Streamlit element can go inside. "
        "Good for contextual info, quick actions, or mini-forms."
    )
    with st.popover("Open popover"):
        st.markdown("**I'm inside a floating popover!**")
        st.text_input("Quick search", key="popover_search")
        st.write("Add any widget here.")
    st.code(
        "with st.popover('Open popover'):\n    st.write('Floating content')\n"
        "    st.text_input('Quick search')",
        language="python",
    )
    st.divider()

    # ── sidebar note ──
    st.subheader("`st.sidebar`")
    st.caption(
        "The persistent left panel you see in this app. "
        "Any widget placed in `with st.sidebar:` is rendered there. "
        "Great for navigation menus, global settings, and filters."
    )
    st.code(
        "with st.sidebar:\n    st.title('My App')\n    section = st.selectbox('Section', ['A','B'])",
        language="python",
    )


# ─────────────────────────────────────────────────────────────────────────────
# TAB 6 — STATUS & FEEDBACK
# ─────────────────────────────────────────────────────────────────────────────
with tabs[5]:
    st.header("Status & Feedback", divider="rainbow")
    st.markdown(
        "Alert banners, loading indicators, multi-step status boxes, "
        "toasts, and full-screen celebration effects."
    )

    # ── Alert boxes ──
    st.subheader("Alert banners")
    st.caption(
        "`st.success`, `st.info`, `st.warning`, `st.error` — "
        "colored banners with an icon. Accept Markdown. "
        "Use `icon=` to override the default emoji."
    )
    st.success("Everything worked! — `st.success()`")
    st.info("For your information. — `st.info()`")
    st.warning("Proceed with caution. — `st.warning()`")
    st.error("Something went wrong. — `st.error()`")
    st.code(
        "st.success('Everything worked!')\nst.info('FYI.')\n"
        "st.warning('Careful!')\nst.error('Something went wrong.')",
        language="python",
    )
    st.divider()

    # ── st.exception ──
    st.subheader("`st.exception()`")
    st.caption(
        "Displays a Python exception object with its full traceback "
        "in a red collapsible box. Useful for debugging inside the app."
    )
    try:
        _ = 1 / 0
    except ZeroDivisionError as e:
        st.exception(e)
    st.code(
        "try:\n    result = 1 / 0\nexcept ZeroDivisionError as e:\n    st.exception(e)",
        language="python",
    )
    st.divider()

    # ── st.progress ──
    st.subheader("`st.progress()`")
    st.caption(
        "A progress bar that accepts values 0–100 (int) or 0.0–1.0 (float). "
        "Update it in a loop with `.progress(value, text=...)` to show real-time task progress. "
        "Call `.empty()` to remove it when done."
    )
    if st.button("Run progress bar demo"):
        bar = st.progress(0, text="Starting…")
        for pct in range(1, 101):
            bar.progress(pct, text=f"Processing… {pct}%")
            time.sleep(0.02)
        bar.empty()
        st.success("Task complete!")
    st.code(
        "bar = st.progress(0, text='Starting…')\nfor i in range(1, 101):\n"
        "    bar.progress(i, text=f'Processing… {i}%')\n    time.sleep(0.02)\nbar.empty()",
        language="python",
    )
    st.divider()

    # ── st.spinner ──
    st.subheader("`st.spinner()`")
    st.caption(
        "Displays a spinning loading indicator and message while the `with` block executes. "
        "Auto-dismisses when the block exits."
    )
    if st.button("Show spinner (2 s)"):
        with st.spinner("Loading, please wait…"):
            time.sleep(2)
        st.success("Loaded!")
    st.code(
        "with st.spinner('Loading…'):\n    result = run_slow_function()",
        language="python",
    )
    st.divider()

    # ── st.status ──
    st.subheader("`st.status()`")
    st.caption(
        "A multi-step status box that expands while running and collapses when done. "
        "Write steps inside it with `st.write()`. "
        "Call `status.update(label=..., state='complete')` to seal it."
    )
    if st.button("Run multi-step process demo"):
        with st.status("Running pipeline…", expanded=True) as status:
            st.write("Step 1 — Connecting to database…")
            time.sleep(0.7)
            st.write("Step 2 — Fetching records…")
            time.sleep(0.7)
            st.write("Step 3 — Processing & writing output…")
            time.sleep(0.7)
            status.update(label="Pipeline complete!", state="complete", expanded=False)
    st.code(
        "with st.status('Running…', expanded=True) as status:\n"
        "    st.write('Step 1…')\n    time.sleep(1)\n"
        "    st.write('Step 2…')\n"
        "    status.update(label='Done!', state='complete')",
        language="python",
    )
    st.divider()

    # ── st.toast ──
    st.subheader("`st.toast()`")
    st.caption(
        "A short-lived notification that appears at the bottom-right corner "
        "and auto-dismisses after a few seconds. "
        "Non-intrusive way to confirm actions."
    )
    if st.button("Show toast notification"):
        st.toast("Action completed successfully!", icon="✅")
    st.code("st.toast('Action completed!', icon='✅')", language="python")
    st.divider()

    # ── Celebrations ──
    st.subheader("Celebration effects")
    st.caption(
        "`st.balloons()` and `st.snow()` trigger full-screen animations. "
        "One-shot, no arguments needed. Great for task completion moments."
    )
    bcol, scol = st.columns(2)
    if bcol.button("🎈 Balloons!"):
        st.balloons()
    if scol.button("❄️ Snow!"):
        st.snow()
    st.code("st.balloons()   # colorful balloons\nst.snow()       # falling snowflakes", language="python")


# ─────────────────────────────────────────────────────────────────────────────
# TAB 7 — FORMS
# ─────────────────────────────────────────────────────────────────────────────
with tabs[6]:
    st.header("Forms", divider="rainbow")
    st.markdown(
        "`st.form()` groups widgets so that **no reruns happen until the user "
        "clicks Submit**. This is the key difference from standalone widgets, "
        "which trigger a rerun on *every* change. Use forms when you need "
        "all field values to arrive together."
    )

    if "form_result" not in st.session_state:
        st.session_state.form_result = None

    with st.form("user_profile_form"):
        st.subheader("User Profile Form")
        st.caption("Fill in the fields — notice that nothing reruns until you click **Save profile**.")

        fname = st.text_input("Full name")
        age = st.number_input("Age", min_value=1, max_value=120, value=25)
        country = st.selectbox(
            "Country", ["Argentina", "Brazil", "Canada", "Germany", "India", "Spain"]
        )
        plan = st.radio("Plan", ["Free", "Pro", "Enterprise"], horizontal=True)
        agree = st.checkbox("I agree to the terms and conditions")

        submitted = st.form_submit_button("Save profile", type="primary")

        if submitted:
            if not agree:
                st.error("You must agree to the terms and conditions before submitting.")
            elif not fname.strip():
                st.error("Please enter your name.")
            else:
                st.session_state.form_result = {
                    "name": fname,
                    "age": age,
                    "country": country,
                    "plan": plan,
                }

    if st.session_state.form_result:
        st.success("Profile saved successfully!")
        st.json(st.session_state.form_result)

    st.divider()
    st.code(
        """with st.form("my_form"):
    name  = st.text_input("Name")
    age   = st.number_input("Age", min_value=1)
    agree = st.checkbox("I agree")
    submitted = st.form_submit_button("Submit")

    if submitted and agree:
        st.write(f"Hello {name}, age {age}!")""",
        language="python",
    )
    st.info(
        "**Key point:** Widgets inside a form do NOT trigger reruns. "
        "Only `st.form_submit_button` does. "
        "This prevents partial-state issues when filling out multi-field forms."
    )


# ─────────────────────────────────────────────────────────────────────────────
# TAB 8 — STATE & CACHING
# ─────────────────────────────────────────────────────────────────────────────
with tabs[7]:
    st.header("State & Caching", divider="rainbow")

    # ── st.session_state ──
    st.subheader("`st.session_state`")
    st.caption(
        "A dict-like object that persists values **across reruns** within "
        "the same browser session. Use it to store counters, flags, history, "
        "or anything that must survive script re-execution."
    )

    if "counter" not in st.session_state:
        st.session_state.counter = 0

    sc1, sc2, sc3 = st.columns([1, 1, 2])
    if sc1.button("➕ Increment"):
        st.session_state.counter += 1
    if sc2.button("🔄 Reset"):
        st.session_state.counter = 0
    sc3.metric("Counter value", st.session_state.counter)

    st.code(
        "if 'counter' not in st.session_state:\n    st.session_state.counter = 0\n\n"
        "if st.button('Increment'):\n    st.session_state.counter += 1\n\n"
        "st.metric('Counter', st.session_state.counter)",
        language="python",
    )
    st.divider()

    # ── @st.cache_data ──
    st.subheader("`@st.cache_data`")
    st.caption(
        "Caches the return value of a function keyed by its arguments. "
        "First call computes and stores the result; subsequent calls with the "
        "same arguments return it instantly from cache — no re-execution. "
        "Best for data loading, API calls, and expensive transforms. "
        "The cached value is **copied** for each caller."
    )

    @st.cache_data
    def load_cached(n: int) -> pd.DataFrame:
        time.sleep(1)  # simulate slow I/O
        return pd.DataFrame(np.random.randn(n, 3), columns=["A", "B", "C"])

    def load_uncached(n: int) -> pd.DataFrame:
        time.sleep(1)
        return pd.DataFrame(np.random.randn(n, 3), columns=["A", "B", "C"])

    dc1, dc2 = st.columns(2)
    with dc1:
        st.markdown("**Cached call** (`@st.cache_data`)")
        t0 = time.perf_counter()
        _ = load_cached(100)
        elapsed_c = time.perf_counter() - t0
        st.metric("Elapsed", f"{elapsed_c:.3f} s", help="After the first run, returns in < 1 ms.")
        st.caption("First visit: 1 s. Every visit after: instant.")

    with dc2:
        st.markdown("**Uncached call**")
        t0 = time.perf_counter()
        _ = load_uncached(100)
        elapsed_u = time.perf_counter() - t0
        st.metric("Elapsed", f"{elapsed_u:.3f} s", help="Always runs the full function body.")
        st.caption("Always takes ~1 s regardless of how many times you visit.")

    st.code(
        "@st.cache_data\ndef load_data(path: str) -> pd.DataFrame:\n"
        "    return pd.read_csv(path)  # only runs once per unique path\n\n"
        "df = load_data('data.csv')   # instant after first call",
        language="python",
    )
    st.divider()

    # ── @st.cache_resource ──
    st.subheader("`@st.cache_resource`")
    st.caption(
        "Like `@st.cache_data` but for **shared, global resources** — "
        "ML models, database connections, API clients. "
        "The object is shared across **all users and sessions** (not copied). "
        "Never re-initialized unless the server restarts or you call `.clear()`."
    )

    @st.cache_resource
    def get_shared_model() -> dict:
        time.sleep(0.4)  # simulate heavy model load
        return {
            "type": "FakeTransformerModel",
            "parameters": "7B",
            "loaded_at": time.strftime("%H:%M:%S"),
        }

    model = get_shared_model()
    st.json(model)
    st.caption("Note that `loaded_at` doesn't change on reruns — the object is reused.")
    st.code(
        "@st.cache_resource\ndef get_model():\n    return load_heavy_model('weights.bin')\n\n"
        "model = get_model()  # shared across all users, loaded once",
        language="python",
    )


# ─────────────────────────────────────────────────────────────────────────────
# TAB 9 — CHAT
# ─────────────────────────────────────────────────────────────────────────────
with tabs[8]:
    st.header("Chat", divider="rainbow")
    st.markdown(
        "Streamlit has first-class chat primitives: a message bubble renderer, "
        "a sticky input bar, and token-by-token streaming output."
    )

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hi! I'm an echo bot. I'll repeat what you say in uppercase and word-by-word streaming. Try typing something below.",
            }
        ]

    # ── st.chat_message ──
    st.subheader("`st.chat_message()`")
    st.caption(
        "Renders a chat bubble with an avatar. Role can be `'user'`, `'assistant'`, "
        "or any custom string. Any Streamlit element (text, charts, tables) can go inside."
    )

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # ── st.write_stream ──
    def _stream_response(text: str):
        """Yield words one at a time to simulate LLM streaming."""
        response = f"Echo: {text.upper()}"
        for word in response.split():
            yield word + " "
            time.sleep(0.07)

    # ── st.chat_input ──
    st.subheader("`st.chat_input()` + `st.write_stream()`")
    st.caption(
        "`st.chat_input()` is a sticky text bar that anchors to the bottom of the page — "
        "it doesn't scroll away. `st.write_stream()` consumes a generator and "
        "renders each yielded chunk live, simulating LLM token streaming."
    )

    if prompt := st.chat_input("Type a message…"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response_text = st.write_stream(_stream_response(prompt))

        st.session_state.messages.append({"role": "assistant", "content": response_text})

    if st.button("🗑️ Clear chat history"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Chat cleared. Say something!"}
        ]
        st.rerun()

    st.divider()
    st.code(
        """# Render existing messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Generator that yields tokens one by one
def stream_reply(text: str):
    for word in f"Echo: {text.upper()}".split():
        yield word + " "
        time.sleep(0.07)

# Sticky input — triggers a rerun when submitted
if prompt := st.chat_input("Type a message…"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        reply = st.write_stream(stream_reply(prompt))

    st.session_state.messages.append({"role": "assistant", "content": reply})""",
        language="python",
    )
