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

from pathlib import Path

import streamlit as st

# ----------------------------------------------------------------------
# Resolve module paths relative to THIS file's location on disk (not the
# process's current working directory). Some deployment platforms
# (Streamlit Community Cloud among them) can launch the app with a CWD
# that differs from the repo root, which makes plain relative strings
# like "modules/app_fundamentals.py" fail with:
#   "Unable to create Page. The file `...` could not be found."
# Anchoring to __file__ makes this work the same locally and deployed.
# ----------------------------------------------------------------------
BASE_DIR = Path(__file__).parent
MODULES_DIR = BASE_DIR / "modules"

REQUIRED_MODULES = [
    "app_fundamentals.py",
    "app_components.py",
    "app_gates.py",
    "app_digital_electronics.py",
    "app_circuit_analysis.py",
    "app_rectifiers.py",
    "app_amplifiers.py",
    "app_measurements.py",
]

missing = [m for m in REQUIRED_MODULES if not (MODULES_DIR / m).is_file()]

if missing:
    # Surface a clear, actionable diagnostic in the app itself instead of
    # a bare stack trace. This tells you exactly what Streamlit Cloud
    # actually sees on disk, which is the fastest way to tell whether the
    # `modules/` folder made it into the deployed repo at all.
    st.error(
        "Setup problem: one or more topic files are missing, so the app "
        "can't build its navigation menu."
    )
    st.write(f"**Expected folder:** `{MODULES_DIR}`")
    st.write(f"**Folder exists:** {MODULES_DIR.is_dir()}")
    if MODULES_DIR.is_dir():
        found = sorted(p.name for p in MODULES_DIR.iterdir())
        st.write(f"**Files actually found in `modules/`:** {found or '(empty)'}")
    else:
        st.write(f"**Files found in app root (`{BASE_DIR}`):**")
        st.write(sorted(p.name for p in BASE_DIR.iterdir()))
    st.write(f"**Missing:** {missing}")
    st.info(
        "Fix: open your GitHub repo in the browser and confirm there is a "
        "`modules/` folder at the repo root containing these 8 files "
        "(exact names, lowercase). If it's not there, the folder was "
        "never pushed / got flattened during upload — re-add it and "
        "redeploy. If it IS there but this still fails, check for a "
        "`.gitignore` rule or nested extra folder (e.g. "
        "`elect_4_beginners/modules/` inside `modules/`)."
    )
    st.stop()

# ----------------------------------------------------------------------
# Define every topic as a Page. `title` and `icon` control what shows up
# in the sidebar nav; `url_path` controls the URL slug so each topic is
# deep-linkable, e.g. https://your-app-url/circuit_analysis
# ----------------------------------------------------------------------
pages = [
    st.Page(
        str(MODULES_DIR / "app_fundamentals.py"),
        title="Electrical Fundamentals",
        icon="🔋",
        url_path="fundamentals",
        default=True,
    ),
    st.Page(
        str(MODULES_DIR / "app_components.py"),
        title="Electronic Components",
        icon="⚡",
        url_path="components",
    ),
    st.Page(
        str(MODULES_DIR / "app_gates.py"),
        title="Logic Gates",
        icon="🔌",
        url_path="logic_gates",
    ),
    st.Page(
        str(MODULES_DIR / "app_digital_electronics.py"),
        title="Digital Electronics",
        icon="💾",
        url_path="digital_electronics",
    ),
    st.Page(
        str(MODULES_DIR / "app_circuit_analysis.py"),
        title="Circuit Analysis",
        icon="🧮",
        url_path="circuit_analysis",
    ),
    st.Page(
        str(MODULES_DIR / "app_rectifiers.py"),
        title="Diodes & Rectifiers",
        icon="🔺",
        url_path="rectifiers",
    ),
    st.Page(
        str(MODULES_DIR / "app_amplifiers.py"),
        title="Transistors & Amplifiers",
        icon="🔀",
        url_path="amplifiers",
    ),
    st.Page(
        str(MODULES_DIR / "app_measurements.py"),
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
