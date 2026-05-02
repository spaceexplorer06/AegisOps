import streamlit as st
from prometheus_client import Counter, generate_latest
import streamlit.components.v1 as components

REQUEST_COUNT = Counter("streamlit_requests_total", "Total requests")

REQUEST_COUNT.inc()

st.title("AegisOps Streamlit App")

st.write("Monitoring enabled 🚀")

# expose metrics
if st.button("Expose Metrics"):
    st.write(generate_latest())