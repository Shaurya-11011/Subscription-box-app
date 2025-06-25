import streamlit as st

# Page setup
st.set_page_config(
    page_title="Red Subscription Box",
    page_icon="📦",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
    h1 {
        color: #FF4C4C;
    }
    .title-text {
        font-size: 32px;
        color: #FF4C4C;
        margin-bottom: 10px;
    }
    .sub-section {
        font-size: 18px;
        font-weight: bold;
        color: #FAFAFA;
        margin-top: 20px;
    }
    div[data-testid="stSlider"] label {
        color: #FAFAFA !important;
    }
    .item-card {
        background-color: #1F1F1F;
        border: 1px solid #FF4C4C;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
    }
    .item-title {
        color: #FF4C4C;
        margin-bottom: 5px;
        font-size: 18px;
    }
    .item-desc {
        color: #CCCCCC;
        font-size: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<div class='title-text'>📦 Build Your Personalized Subscription Box</div>", unsafe_allow_html=True)
st.markdown("Customize your preferences — and generate your smart, AI-style box instantly.")

# Layout
col1, col2 = st.columns([1, 1.2], gap="large")

# -------- LEFT: Preferences --------
with col1:
    with st.expander("🎛️ Your Preferences", expanded=True):
        categories = st.multiselect(
            "Select Interests:",
            ["Tech", "Fitness", "Food", "Books"]
        )

        budget = st.slider("Monthly Budget (₹)", 500, 5000, 2000, step=500)

        brands = st.multiselect(
            "Preferred Brands:",
            ["Apple", "Samsung", "Nike", "Adidas", "Nestle", "MyProtein", "Penguin Books", "Tata", "Sony"]
        )

        goal = st.text_input("Personal Goal (optional)", placeholder="e.g. Improve focus, Eat healthy...")

# -------- RIGHT: Box Preview --------
with col2:
    st.markdown("<div class='sub-section'>🛍️ Your Personalized Box Preview</div>", unsafe_allow_html=True)

    def create_card(title, description):
        return f"""
        <div class='item-card'>
            <div class='item-title'>{title}</div>
            <div class='item-desc'>{description}</div>
        </div>
        """

    def generate_box(categories, budget, brands, goal):
        box = []

        if "Tech" in categories:
            box.append(("Apple AirTag" if "Apple" in brands else "Xiaomi Smart Band", "Smart tracker or wearable."))

        if "Fitness" in categories:
            box.append(("Nike Resistance Bands" if "Nike" in brands else "MyProtein Starter Pack", "Wellness & fitness."))

        if "Food" in categories:
            box.append(("Nestlé Snack Box" if "Nestle" in brands else "Tata Green Tea Sampler", "Healthy food choices."))

        if "Books" in categories:
            box.append(("Atomic Habits" if "Penguin Books" in brands else "Deep Work", "Productivity boost."))

        if goal:
            box.append(("Motivation Card", f"Custom message: {goal.title()}"))

        return box

    if categories:
        for title, desc in generate_box(categories, budget, brands, goal):
            st.markdown(create_card(title, desc), unsafe_allow_html=True)
    else:
        st.info("👈 Use the 'Your Preferences' section to start building your box.")

# Footer
st.markdown("---")
st.caption("Created by Shaurya Jain • Hyper-Personalized Subscription Box • 2025")
