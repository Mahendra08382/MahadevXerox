import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Mahadev Internet Xerox",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject custom CSS
# CSS to force white background and light mode
st.markdown("""
    <style>
        html, body, [data-testid="stApp"] {
            background-color: white !important;
            color: black !important;
        }
        .main-header {
            background-color: #003366;
            padding: 1rem;
            text-align: center;
            color: white;
            font-size: 2rem;
            border-radius: 0 0 10px 10px;
        }
        .service-box {
            background-color: #FFC107;  /* Dark Yellow */
            padding: 1.5rem;
            margin-bottom: 1rem;
            margin-right: 1rem;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            text-align: center;
            transition: 0.3s;
            color: #000; /* Ensures text is visible on yellow background */
        }
        .service-box:hover {
            transform: translateY(-5px);
            box-shadow: 2px 8px 20px rgba(0,0,0,0.2);
        }
        .footer {
            margin-top: 3rem;
            padding: 1rem;
            text-align: center;
            font-size: 0.9rem;
            color: #666;
        }
    </style>
""", unsafe_allow_html=True)


# Header
st.markdown("<div class='main-header'>🖨️ Mahadev Internet & Xerox Center</div>", unsafe_allow_html=True)

st.write("### Contact Us: 7676802833")

st.write("### 👇👇 Our Services 👇👇")

# Services Section
# Main Section with Services on the left and Image on the right
left_col, right_col = st.columns([2, 1])

with left_col:
   
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("<div class='service-box'><h3>📄 Xerox</h3><p>High-quality B&W and color Xerox available at best prices.</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='service-box'><h3>🖨️ Printing</h3><p>Print your documents from mobile, email, or pen drive.</p></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='service-box'><h3>🌐 Internet</h3><p>High-speed browsing, form filling, and online services.</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='service-box'><h3>📠 Scanning</h3><p>Scan and send documents via email or WhatsApp.</p></div>", unsafe_allow_html=True)

with right_col:
    st.image("Image1.jpg", caption="Our Print & Xerox Machine", use_container_width=True)

st.markdown("<div style='height:5px;'></div>", unsafe_allow_html=True)
# Contact Info
st.write("---")
st.subheader("📞 Contact Us")
st.write("**Owner:** Madan Talekar")
st.write("📍 Location: Opp Mahadevastan Temple, Karwar, Karnataka - 581301")
st.write("📱 Phone: +91-7676802833")
st.write("📧 Email: mahadev.internet@gmail.com")

# Footer
st.markdown("<div class='footer'>© 2025 Mahadev Internet Xerox. All rights reserved.</div>", unsafe_allow_html=True)
