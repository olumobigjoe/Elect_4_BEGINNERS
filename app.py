"""
Electronics Learning Hub
A single Streamlit application that combines all 8 topic modules into one
app (one URL, one sidebar navigation menu):

    1. Electrical Fundamentals
    2. Electronic Components
    3. Logic Gates
    4. Digital Electronics
    5. Circuit Analysis
    6. Diodes & Rectifiers
    7. Transistors & Amplifiers
    8. Measurements & Instruments

HOW THIS WORKS
--------------
Streamlit's built-in multi-page navigation (`st.navigation` / `st.Page`,
available in Streamlit >= 1.36) is used to stitch the 8 original,
independent single-file apps together WITHOUT modifying their internal
code. Each module keeps its own `st.set_page_config(...)` call — that is
fine, because Streamlit only executes the ONE page script that is
currently selected in the sidebar; the other 7 scripts are not run at
the same time, so there is no "set_page_config called twice" conflict.

This file (app.py) is the only entry point. It must be run with:

    streamlit run app.py

Do NOT run any of the files inside modules/ directly with `streamlit
run` on their own if you want the combined experience — run app.py.
"""

import streamlit as st

# ----------------------------------------------------------------------
# Define every topic as a Page. `title` and `icon` control what shows up
# in the sidebar nav; `url_path` controls the URL slug so each topic is
# deep-linkable, e.g. https://your-app-url/circuit_analysis
# ----------------------------------------------------------------------
pages = [
    st.Page(
        "modules/app_fundamentals.py",
        title="Electrical Fundamentals",
        icon="🔋",
        url_path="fundamentals",
        default=True,
    ),
    st.Page(
        "modules/app_components.py",
        title="Electronic Components",
        icon="⚡",
        url_path="components",
    ),
    st.Page(
        "modules/app_gates.py",
        title="Logic Gates",
        icon="🔌",
        url_path="logic_gates",
    ),
    st.Page(
        "modules/app_digital_electronics.py",
        title="Digital Electronics",
        icon="💾",
        url_path="digital_electronics",
    ),
    st.Page(
        "modules/app_circuit_analysis.py",
        title="Circuit Analysis",
        icon="🧮",
        url_path="circuit_analysis",
    ),
    st.Page(
        "modules/app_rectifiers.py",
        title="Diodes & Rectifiers",
        icon="🔺",
        url_path="rectifiers",
    ),
    st.Page(
        "modules/app_amplifiers.py",
        title="Transistors & Amplifiers",
        icon="🔀",
        url_path="amplifiers",
    ),
    st.Page(
        "modules/app_measurements.py",
        title="Measurements & Instruments",
        icon="📏",
        url_path="measurements",
    ),
]

# NOTE: app.py itself must not call any st.* command (including
# st.set_page_config) before st.navigation() / pg.run() — that's what
# lets each individual page's own st.set_page_config() call succeed.
nav = st.navigation(pages, position="sidebar")
nav.run()
