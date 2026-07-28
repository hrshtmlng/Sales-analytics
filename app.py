import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(page_title="Sales & Revenue Analytics", layout="wide")

# Connect to DB
conn = sqlite3.connect('sales_analytics.db')

@st.cache_data
def load_data(query):
    return pd.read_sql(query, conn)

# ========== TITLE ==========
st.title("📊 Sales & Revenue Analytics Dashboard")
st.markdown("Built with 105K+ transactional records | Real-time insights")

# ========== KPI ROW ==========
st.markdown("---")
c1, c2, c3, c4, c5 = st.columns(5)

revenue = load_data("""
    SELECT ROUND(SUM(quantity * unit_price * (1 - discount)), 2) as total 
    FROM order_items oi JOIN orders o ON oi.order_id = o.order_id 
    WHERE o.order_status = 'Completed'
""").iloc[0, 0]

orders = load_data("""
    SELECT COUNT(DISTINCT order_id) as total FROM orders WHERE order_status = 'Completed'
""").iloc[0, 0]

customers = load_data("""
    SELECT COUNT(DISTINCT customer_id) as total FROM orders WHERE order_status = 'Completed'
""").iloc[0, 0]

aov = revenue / orders if orders > 0 else 0

margin = load_data("""
    SELECT ROUND((SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) - SUM(oi.quantity * p.unit_cost)) /
          NULLIF(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 0) * 100, 2) as margin
    FROM order_items oi JOIN orders o ON oi.order_id = o.order_id
    JOIN products p ON oi.product_id = p.product_id WHERE o.order_status = 'Completed'
""").iloc[0, 0]

c1.metric("💰 Total Revenue", f"${revenue:,.0f}")
c2.metric("📦 Total Orders", f"{orders:,}")
c3.metric("📈 Avg Order Value", f"${aov:.2f}")
c4.metric("👥 Active Customers", f"{customers:,}")
c5.metric("📊 Gross Margin", f"{margin}%")

# ========== CHARTS ROW 1 ==========
st.markdown("---")
cl, cr = st.columns(2)

monthly = load_data("""
    SELECT strftime('%Y-%m', o.order_date) as month,
           ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) as revenue
    FROM orders o JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.order_status = 'Completed' GROUP BY month ORDER BY month
""")
fig1 = px.line(monthly, x='month', y='revenue', title='📈 Monthly Revenue Trend',
               labels={'revenue': 'Revenue ($)', 'month': 'Month'})
fig1.update_traces(line_color='#1f77b4', line_width=3)
cl.plotly_chart(fig1, use_container_width=True)

category = load_data("""
    SELECT c.category_name, ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) as revenue
    FROM orders o JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id JOIN categories c ON p.category_id = c.category_id
    WHERE o.order_status = 'Completed' GROUP BY c.category_name ORDER BY revenue DESC
""")
fig2 = px.pie(category, values='revenue', names='category_name', title='🥧 Revenue by Category', hole=0.4)
cr.plotly_chart(fig2, use_container_width=True)

# ========== CHARTS ROW 2 ==========
cl2, cr2 = st.columns(2)

top_products = load_data("""
    SELECT p.product_name, ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) as revenue
    FROM orders o JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id WHERE o.order_status = 'Completed'
    GROUP BY p.product_id, p.product_name ORDER BY revenue DESC LIMIT 10
""")
fig3 = px.bar(top_products, y='product_name', x='revenue', orientation='h',
              title='🏆 Top 10 Products', labels={'revenue': 'Revenue ($)', 'product_name': ''})
fig3.update_traces(marker_color='#2ca02c')
fig3.update_layout(yaxis={'categoryorder': 'total ascending'})
cl2.plotly_chart(fig3, use_container_width=True)

segments = load_data("""
    SELECT cu.customer_segment, ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) as revenue
    FROM orders o JOIN order_items oi ON o.order_id = oi.order_id
    JOIN customers cu ON o.customer_id = cu.customer_id WHERE o.order_status = 'Completed'
    GROUP BY cu.customer_segment ORDER BY revenue DESC
""")
fig4 = px.bar(segments, x='customer_segment', y='revenue', title='👥 Revenue by Customer Segment',
              color='customer_segment', labels={'revenue': 'Revenue ($)'})
fig4.update_layout(showlegend=False)
cr2.plotly_chart(fig4, use_container_width=True)

# ========== SEASONALITY ==========
st.markdown("---")
st.subheader("🗓️ Seasonal Demand Pattern")

seasonal = load_data("""
    SELECT CAST(strftime('%m', o.order_date) AS INTEGER) as month_num,
           CASE CAST(strftime('%m', o.order_date) AS INTEGER)
               WHEN 1 THEN 'Jan' WHEN 2 THEN 'Feb' WHEN 3 THEN 'Mar' WHEN 4 THEN 'Apr'
               WHEN 5 THEN 'May' WHEN 6 THEN 'Jun' WHEN 7 THEN 'Jul' WHEN 8 THEN 'Aug'
               WHEN 9 THEN 'Sep' WHEN 10 THEN 'Oct' WHEN 11 THEN 'Nov' WHEN 12 THEN 'Dec'
           END as month_name,
           ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) as revenue
    FROM orders o JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.order_status = 'Completed' GROUP BY month_num ORDER BY month_num
""")
colors = ['#d62728' if m in [11, 12] else '#1f77b4' for m in seasonal['month_num']]
fig5 = px.bar(seasonal, x='month_name', y='revenue', title='Peak Season Detection (Red = Nov-Dec)',
              labels={'revenue': 'Revenue ($)', 'month_name': 'Month'})
fig5.update_traces(marker_color=colors)
st.plotly_chart(fig5, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("📊 *Dashboard built with Streamlit | Data: 105K+ transactions*")
