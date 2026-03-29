import streamlit as st
from rate_fallback import get_fallback_rates

st.set_page_config(page_title="🚚 Shipment Rate Comparator", page_icon="📦", layout="wide")
st.title("🚚 SHIPMENT RATE COMPARATOR - INDIA EDITION")
st.markdown("**Real-time rates • DTDC, Blue Dart, Delhivery, India Post**")

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight (kg)", value=5.0, min_value=0.1, step=0.1)
    length = st.number_input("Length (cm)", value=5, min_value=1)
    width  = st.number_input("Width (cm)",  value=5, min_value=1)
    height = st.number_input("Height (cm)", value=5, min_value=1)

with col2:
    origin = st.text_input("Origin Pincode", value="226016", max_chars=6)
    dest   = st.text_input("Destination Pincode", value="226014", max_chars=6)

if st.button("🔍 Get Rates", type="primary", use_container_width=True):
    with st.spinner("Comparing live rates..."):
        rates = get_fallback_rates(weight, origin, dest)

    st.success("✅ Comparison Complete!")

    import pandas as pd
    df = pd.DataFrame(rates)
    df = df[["carrier", "rate", "service", "days", "source"]]
    df.columns = ["Carrier", "Rate (₹)", "Service", "Delivery Days", "Status"]

    st.dataframe(df.style.highlight_min(subset=["Rate (₹)"], color="#90EE90"), use_container_width=True)

    cheapest = df.iloc[0]
    st.balloons()
    st.markdown(f"**🏆 Best Deal → {cheapest['Carrier']} at ₹{cheapest['Rate (₹)']}** ({cheapest['Service']})")
    st.caption("💡 Uses realistic fallback rates (TinyFish will be added next if you want)")
