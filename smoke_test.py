
import streamlit as st

# Simulate core UI components from reef_tank_tracker_app.py

try:
    st.title("🧪 ReefTrack Smoke Test")

    if "tanks" not in st.session_state:
        st.session_state.tanks = {}

    if "selected_tank" not in st.session_state:
        st.session_state.selected_tank = None

    tank_names = list(st.session_state.tanks.keys())
    selected = st.selectbox("Select Tank", tank_names) if tank_names else None

    if st.button("Add Tank"):
        st.session_state.tanks["Test Tank"] = {"volume": 100, "type": "Mixed"}
        st.success("Added mock tank.")

    with st.expander("Test Expander"):
        st.write("This section should be visible and functional.")

    st.success("✅ App ran without crashing.")

except Exception as e:
    st.error(f"❌ Smoke test failed: {e}")
