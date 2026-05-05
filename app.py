# app.py

import streamlit as st
import pandas as pd
from insurance_logic import analyze_procedure, PROCEDURE_RULES


st.set_page_config(
    page_title="Spartacus Dental AI",
    page_icon="🦷",
    layout="centered"
)


st.title("🦷 Spartacus Dental AI Assistant")
st.write(
    "A rule-based AI-style assistant that estimates dental insurance coverage, "
    "approval likelihood, and documentation needs."
)

st.warning(
    "Educational demo only. This tool does not provide real insurance determinations."
)


st.divider()

st.header("Analyze a Dental Procedure")

procedure_code = st.text_input(
    "Enter dental procedure code",
    placeholder="Example: D2740"
)

insurance_provider = st.text_input(
    "Enter insurance provider",
    placeholder="Example: Aetna, Delta Dental, Cigna"
)

if st.button("Analyze Coverage"):
    if not procedure_code:
        st.error("Please enter a dental procedure code.")
    else:
        result = analyze_procedure(procedure_code, insurance_provider)

        st.subheader("Coverage Estimate")

        st.write(f"**Procedure Code:** {result['procedure_code']}")
        st.write(f"**Procedure Name:** {result['procedure_name']}")
        st.write(f"**Insurance Provider:** {result['insurance_provider']}")
        st.write(f"**Category:** {result['category']}")
        st.write(f"**Estimated Coverage:** {result['estimated_coverage']}")
        st.write(f"**Approval Likelihood:** {result['approval_likelihood']}")
        st.write(f"**Notes:** {result['notes']}")

        st.info(result["disclaimer"])


st.divider()

st.header("Demo Procedure Codes")

demo_data = []

for code, details in PROCEDURE_RULES.items():
    demo_data.append({
        "Code": code,
        "Procedure": details["name"],
        "Category": details["category"],
        "Estimated Coverage": details["coverage"],
        "Approval Likelihood": details["approval"]
    })

df = pd.DataFrame(demo_data)
st.dataframe(df, use_container_width=True)


st.divider()

st.header("Project Purpose")
st.write(
    "Spartacus was designed to simulate how AI and structured data could help "
    "dental clinics quickly understand insurance coverage, reduce manual lookup time, "
    "and improve patient cost transparency."
)
