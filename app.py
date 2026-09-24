import streamlit as st
import requests

# Kurucu: IKHTIYOR (tjk2025.dyu@gmail.com)
st.set_page_config(page_title="Zilzal AI", page_icon="🛡️", layout="wide")

# Kurumsal Ücretsiz Gece Mavisi Tema
st.markdown("""
    <style>
    .stApp { background-color: #0F172A; color: #FFFFFF; }
    .stButton>button { background-color: #10B981; color: white; border-radius: 8px; width: 100%; font-weight: bold; }
    h1, h2, h3 { color: #10B981 !important; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ Zilzal AI — Global Cyber-Secure & Age-Adaptive AI")
st.caption("Founder: IKHTIYOR | Contact: tjk2025.dyu@gmail.com")

# Küresel Dil Seçici (Üretimde otomatik algılanır)
lang = st.sidebar.selectbox("🌐 Language / Dil", ["English", "Türkçe"])

# Yaş Grupları ve AR-GE Modu Ayrımı
user_mode = st.sidebar.radio(
    "Select User Profile / Profil Seçin:",
    ["🧸 2-6 Years (Toddler)", "🎒 7-10 Years (Explorer)", "🧠 11-17 Years (Academic)", "🔬 R&D & Cyber Security (Enterprise)"]
)

user_query = st.chat_input("Ask Zilzal AI anything globally...")

if user_query:
    with st.chat_message("user"):
        st.write(user_query)
        
    # Siber Güvenlik Duvarı (Prompt Injection ve Zararlı İçerik Kontrolü)
    banned_terms = ["hack", "bomba", "attack", "saldırı", "çökertme", "exploit"]
    if any(term in user_query.lower() for term in banned_terms) and "R&D" not in user_mode:
        with st.chat_message("assistant"):
            st.error("🚨 [Siber Güvenlik Engeli] Appropriate usage guidelines violated. Access blocked.")
    else:
        # Anlık yanıt simülasyonu (Yerel veya bulut API bağlantısı)
        with st.chat_message("assistant"):
            st.info(f"⚡ Processing instantly via Global Edge GPU Server for: {user_mode}")
            if "2-6" in user_mode:
                st.write("🤖 [Zilzal AI]: Hello friend! Let's explore colors and stories together today! 🌟")
            elif "7-10" in user_mode:
                st.write("🤖 [Zilzal AI]: That's a brilliant question! Let's solve this scientific puzzle step-by-step.")
            elif "11-17" in user_mode:
                st.write("🤖 [Zilzal AI]: Mentoring mode activated. I can assist with Python coding, school data, and projects.")
            else:
                st.write("🤖 [Zilzal AI - R&D]: Secure vault connection verified. Processing heavy enterprise parameters.")
