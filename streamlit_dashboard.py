"""
European Bank Customer Churn Analytics Dashboard
Enhanced Version with 5+ Graphs Per Tab
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os
import base64
warnings.filterwarnings('ignore')

# Set Seaborn style
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.1)
sns.set_palette("husl")

# Page configuration
st.set_page_config(
    page_title="European Bank Churn Analytics",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
    }
    
    .main-header {
        font-size: 40px;
        font-weight: 700;
        color: #2c3e50;
        text-align: center;
        padding: 25px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    .subtitle {
        text-align: center;
        color: #7f8c8d;
        font-size: 16px;
        margin-bottom: 30px;
    }
    
    .critical-box {
        background-color: #fff5f5;
        border-left: 5px solid #e74c3c;
        padding: 20px;
        border-radius: 8px;
        margin: 20px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .critical-box h4 {
        color: #c0392b;
        margin-top: 0;
        font-size: 18px;
        font-weight: 600;
    }
    
    .critical-box ul {
        color: #2c3e50;
        line-height: 1.8;
    }
    
    .critical-box li {
        margin: 8px 0;
        color: #34495e;
    }
    
    .critical-box strong {
        color: #c0392b;
        font-weight: 600;
    }
    
    .info-box {
        background-color: #f0f8ff;
        border-left: 5px solid #3498db;
        padding: 20px;
        border-radius: 8px;
        margin: 20px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .info-box h4 {
        color: #2980b9;
        margin-top: 0;
        font-size: 18px;
        font-weight: 600;
    }
    
    .info-box ul {
        color: #2c3e50;
        line-height: 1.8;
    }
    
    .info-box li {
        margin: 8px 0;
        color: #34495e;
    }
    
    .info-box strong {
        color: #2980b9;
        font-weight: 600;
    }
    
    .warning-box {
        background-color: #fffbf0;
        border-left: 5px solid #f39c12;
        padding: 20px;
        border-radius: 8px;
        margin: 20px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .warning-box h4 {
        color: #d68910;
        margin-top: 0;
        font-size: 18px;
        font-weight: 600;
    }
    
    .warning-box ul {
        color: #2c3e50;
        line-height: 1.8;
    }
    
    .warning-box li {
        margin: 8px 0;
        color: #34495e;
    }
    
    .warning-box strong {
        color: #d68910;
        font-weight: 600;
    }
    
    .section-header {
        color: #2c3e50;
        font-size: 24px;
        font-weight: 600;
        margin: 30px 0 20px 0;
        padding-bottom: 10px;
        border-bottom: 3px solid #3498db;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and cache the processed data"""
    possible_paths = [
        'processed_bank_data.csv',
        './processed_bank_data.csv',
        os.path.join(os.path.dirname(__file__), 'processed_bank_data.csv'),
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            df = pd.read_csv(path)
            return df
    
    st.error("❌ Data file not found! Please make sure 'processed_bank_data.csv' is in the same folder.")
    st.stop()

def calculate_kpis(df, filters=None):
    """Calculate KPIs based on filters"""
    if filters:
        filtered_df = df.copy()
        if 'geography' in filters and filters['geography'] != 'All':
            filtered_df = filtered_df[filtered_df['Geography'] == filters['geography']]
        if 'age_group' in filters and filters['age_group'] != 'All':
            filtered_df = filtered_df[filtered_df['AgeGroup'] == filters['age_group']]
        if 'active_only' in filters and filters['active_only']:
            filtered_df = filtered_df[filtered_df['IsActiveMember'] == 1]
    else:
        filtered_df = df
    
    total_customers = len(filtered_df)
    churned = filtered_df['Exited'].sum()
    churn_rate = (churned / total_customers * 100) if total_customers > 0 else 0
    
    high_value = filtered_df[filtered_df['HighValueCustomer'] == 1]
    hv_churn_rate = (high_value['Exited'].mean() * 100) if len(high_value) > 0 else 0
    
    churned_balance = filtered_df[filtered_df['Exited'] == 1]['Balance'].sum()
    
    return {
        'total_customers': total_customers,
        'churned': int(churned),
        'churn_rate': churn_rate,
        'hv_churn_rate': hv_churn_rate,
        'balance_at_risk': churned_balance
    }

def main():
    # Header
    col1, col2, col3 = st.columns([1, 6, 1])
    
    with col1:
        with open("logo1.svg", "rb") as f:
            logo1_data = base64.b64encode(f.read()).decode()
        st.markdown(
            f'<a href="https://www.ecb.europa.eu/home/html/index.en.html" target="_blank">'
            f'<img src="data:image/svg+xml;base64,{logo1_data}" width="120"></a>',
            unsafe_allow_html=True
        )
        
    with col2:
        st.markdown('<div class="main-header">🏦 Customer Segmentation & Churn Pattern Analytics</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">Enhanced Dashboard | 10,000 Customers Evaluated</div>', unsafe_allow_html=True)
        
    with col3:
        with open("logo2.png", "rb") as f:
            logo2_data = base64.b64encode(f.read()).decode()
        st.markdown(
            f'<a href="https://unifiedmentor.com/" target="_blank">'
            f'<img src="data:image/png;base64,{logo2_data}" width="120"></a>',
            unsafe_allow_html=True
        )

    st.markdown("---")
    
    # Load data
    df = load_data()
    
    # Sidebar filters
    st.sidebar.markdown("### 📊 Dashboard Filters")
    st.sidebar.markdown("---")
    
    geography_filter = st.sidebar.selectbox(
        "🌍 Geography",
        ['All'] + sorted(df['Geography'].unique().tolist())
    )
    
    age_group_filter = st.sidebar.selectbox(
        "👥 Age Group",
        ['All'] + sorted(df['AgeGroup'].dropna().unique().tolist())
    )
    
    active_only = st.sidebar.checkbox("✅ Active Members Only", value=False)
    
    st.sidebar.markdown("---")
    st.sidebar.info("💡 **Tip:** Use filters to drill down into specific customer segments")
    
    filters = {
        'geography': geography_filter,
        'age_group': age_group_filter,
        'active_only': active_only
    }
    
    # Calculate KPIs
    kpis = calculate_kpis(df, filters)
    
    # Display KPIs
    st.markdown("### 📊 Key Performance Indicators")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Customers", f"{kpis['total_customers']:,}")
    
    with col2:
        st.metric("Churned", f"{kpis['churned']:,}", 
                 delta=f"-{kpis['churn_rate']:.1f}%", delta_color="inverse")
    
    with col3:
        st.metric("HV Churn Rate", f"{kpis['hv_churn_rate']:.1f}%")
    
    with col4:
        st.metric("Balance at Risk", f"€{kpis['balance_at_risk']/1e6:.1f}M")
    
    st.markdown("---")
    
    # Create tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🌍 Geographic",
        "👥 Demographics",
        "💰 Financial",
        "📊 Engagement",
        "🎯 High-Value"
    ])
    
    # Apply filters
    filtered_df = df.copy()
    if geography_filter != 'All':
        filtered_df = filtered_df[filtered_df['Geography'] == geography_filter]
    if age_group_filter != 'All':
        filtered_df = filtered_df[filtered_df['AgeGroup'] == age_group_filter]
    if active_only:
        filtered_df = filtered_df[filtered_df['IsActiveMember'] == 1]
    
    with tab1:
        st.markdown('<div class="section-header">🌍 Geographic Churn Analysis</div>', unsafe_allow_html=True)
        
        # Graph 1 & 2: Churn Rate and Distribution
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 1. Churn Rate by Country")
            geo_churn = filtered_df.groupby('Geography')['Exited'].mean().reset_index()
            geo_churn.columns = ['Country', 'ChurnRate']
            geo_churn['ChurnRate'] = geo_churn['ChurnRate'] * 100
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=geo_churn, x='Country', y='ChurnRate', 
                       palette=['#3498db', '#e74c3c', '#2ecc71'], ax=ax)
            ax.set_ylabel('Churn Rate (%)')
            ax.set_xlabel('Country')
            ax.set_title('Churn Rate by Geography')
            ax.axhline(y=filtered_df['Exited'].mean()*100, color='red', 
                      linestyle='--', label='Average', linewidth=2)
            ax.legend()
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        with col2:
            st.markdown("#### 2. Customer Distribution")
            geo_counts = filtered_df['Geography'].value_counts().reset_index()
            geo_counts.columns = ['Country', 'Count']
            
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.pie(geo_counts['Count'], labels=geo_counts['Country'], 
                   autopct='%1.1f%%', startangle=90, colors=['#3498db', '#e74c3c', '#2ecc71'])
            ax.set_title('Geographic Distribution')
            ax.axis('equal')
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        # Graph 3 & 4: Country-wise metrics
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 3. Average Balance by Country")
            geo_balance = filtered_df.groupby('Geography')['Balance'].mean().reset_index()
            geo_balance.columns = ['Country', 'AvgBalance']
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=geo_balance, x='Country', y='AvgBalance', 
                       palette='Blues_d', ax=ax)
            ax.set_ylabel('Average Balance (€)')
            ax.set_xlabel('Country')
            ax.set_title('Average Customer Balance by Country')
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        with col2:
            st.markdown("#### 4. Churned vs Retained by Country")
            geo_status = filtered_df.groupby(['Geography', 'Exited']).size().reset_index(name='Count')
            geo_status['Status'] = geo_status['Exited'].map({0: 'Retained', 1: 'Churned'})
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=geo_status, x='Geography', y='Count', hue='Status',
                       palette={'Retained': 'green', 'Churned': 'red'}, ax=ax)
            ax.set_ylabel('Number of Customers')
            ax.set_xlabel('Country')
            ax.set_title('Customer Retention Status by Country')
            ax.legend(title='Status')
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        # Graph 5 & 6: Activity and Product analysis by country
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 5. Active vs Inactive by Country")
            geo_activity = filtered_df.groupby(['Geography', 'IsActiveMember']).size().reset_index(name='Count')
            geo_activity['Activity'] = geo_activity['IsActiveMember'].map({0: 'Inactive', 1: 'Active'})
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=geo_activity, x='Geography', y='Count', hue='Activity',
                       palette={'Active': '#2ecc71', 'Inactive': '#e74c3c'}, ax=ax)
            ax.set_ylabel('Number of Customers')
            ax.set_xlabel('Country')
            ax.set_title('Customer Activity Status by Country')
            ax.legend(title='Activity')
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        with col2:
            st.markdown("#### 6. Average Products by Country")
            geo_products = filtered_df.groupby('Geography')['NumOfProducts'].mean().reset_index()
            geo_products.columns = ['Country', 'AvgProducts']
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=geo_products, x='Country', y='AvgProducts', 
                       palette='viridis', ax=ax)
            ax.set_ylabel('Average Number of Products')
            ax.set_xlabel('Country')
            ax.set_title('Product Portfolio Size by Country')
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        # Insights
        st.markdown("---")
        st.markdown('<div class="section-header">🔍 Key Geographic Insights</div>', unsafe_allow_html=True)
        
        germany_churn = filtered_df[filtered_df['Geography']=='Germany']['Exited'].mean()*100 if 'Germany' in filtered_df['Geography'].values else 0
        france_churn = filtered_df[filtered_df['Geography']=='France']['Exited'].mean()*100 if 'France' in filtered_df['Geography'].values else 0
        spain_churn = filtered_df[filtered_df['Geography']=='Spain']['Exited'].mean()*100 if 'Spain' in filtered_df['Geography'].values else 0
        
        st.markdown(f"""
        <div class="critical-box">
            <h4>🚨 Critical Alert: Germany Market Crisis</h4>
            <ul>
                <li><strong>Germany churn rate: {germany_churn:.2f}%</strong> - Critically elevated</li>
                <li>This represents <strong>approximately 2x the churn</strong> seen in France ({france_churn:.2f}%) and Spain ({spain_churn:.2f}%)</li>
                <li><strong>Immediate investigation required</strong> for German market dynamics</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="section-header">👥 Demographic Churn Analysis</div>', unsafe_allow_html=True)
        
        # Graph 1 & 2: Age and Gender
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 1. Churn Rate by Age Group")
            age_churn = filtered_df.groupby('AgeGroup')['Exited'].mean().reset_index()
            age_churn.columns = ['AgeGroup', 'ChurnRate']
            age_churn['ChurnRate'] = age_churn['ChurnRate'] * 100
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=age_churn, x='AgeGroup', y='ChurnRate', 
                       palette='rocket', ax=ax)
            ax.set_ylabel('Churn Rate (%)')
            ax.set_xlabel('Age Group')
            ax.set_title('Churn Rate by Age Group')
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        with col2:
            st.markdown("#### 2. Gender Comparison")
            gender_churn = filtered_df.groupby('Gender')['Exited'].mean().reset_index()
            gender_churn.columns = ['Gender', 'ChurnRate']
            gender_churn['ChurnRate'] = gender_churn['ChurnRate'] * 100
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=gender_churn, x='Gender', y='ChurnRate', 
                       palette=['#3498db', '#e91e63'], ax=ax)
            ax.set_ylabel('Churn Rate (%)')
            ax.set_xlabel('Gender')
            ax.set_title('Gender-Based Churn Rate')
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        # Graph 3: Age Distribution
        st.markdown("---")
        st.markdown("#### 3. Age Distribution: Churned vs Retained")
        
        fig, ax = plt.subplots(figsize=(18, 5))
        sns.histplot(data=filtered_df, x='Age', hue='Exited', bins=30, 
                    palette={0: 'green', 1: 'red'}, alpha=0.6, ax=ax)
        ax.set_xlabel('Age (years)')
        ax.set_ylabel('Number of Customers')
        ax.set_title('Age Distribution Comparison')
        ax.legend(labels=['Retained', 'Churned'])
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close()
        
        # Graph 4 & 5: Gender by Age and Country
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 4. Gender Distribution by Age Group")
            gender_age = filtered_df.groupby(['AgeGroup', 'Gender']).size().reset_index(name='Count')
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=gender_age, x='AgeGroup', y='Count', hue='Gender',
                       palette=['#3498db', '#e91e63'], ax=ax)
            ax.set_ylabel('Number of Customers')
            ax.set_xlabel('Age Group')
            ax.set_title('Gender Distribution Across Age Groups')
            plt.xticks(rotation=45)
            ax.legend(title='Gender')
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        with col2:
            st.markdown("#### 5. Average Age by Country")
            geo_age = filtered_df.groupby('Geography')['Age'].mean().reset_index()
            geo_age.columns = ['Country', 'AvgAge']
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=geo_age, x='Country', y='AvgAge', 
                       palette='coolwarm', ax=ax)
            ax.set_ylabel('Average Age (years)')
            ax.set_xlabel('Country')
            ax.set_title('Average Customer Age by Country')
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        # Graph 6: Age vs Balance Scatter
        st.markdown("---")
        st.markdown("#### 6. Age vs Balance Relationship")
        
        fig, ax = plt.subplots(figsize=(18, 5))
        sns.scatterplot(data=filtered_df, x='Age', y='Balance', hue='Exited',
                       palette={0: 'green', 1: 'red'}, alpha=0.5, s=30, ax=ax)
        ax.set_xlabel('Age (years)')
        ax.set_ylabel('Account Balance (€)')
        ax.set_title('Age vs Balance: Churn Pattern Analysis')
        ax.legend(labels=['Retained', 'Churned'])
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close()
        
        # Insights
        st.markdown("---")
        st.markdown('<div class="section-header">🔍 Key Demographic Insights</div>', unsafe_allow_html=True)
        
        age_stats = filtered_df.groupby('AgeGroup')['Exited'].agg(['count', 'sum', 'mean']).round(4)
        age_46_60_churn = age_stats.loc['46-60', 'mean'] * 100 if '46-60' in age_stats.index else 0
        
        st.markdown(f"""
        <div class="critical-box">
            <h4>🚨 Critical Age Vulnerability: 46-60 Segment</h4>
            <ul>
                <li><strong>Age 46-60 shows {age_46_60_churn:.2f}% churn rate</strong> - over half churning</li>
                <li><strong>Urgent intervention needed</strong> for pre-retirement demographic</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="section-header">💰 Financial Profile Analysis</div>', unsafe_allow_html=True)
        
        # Graph 1 & 2: Credit Score and Balance
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 1. Credit Score Impact")
            credit_churn = filtered_df.groupby('CreditScoreBand')['Exited'].mean().reset_index()
            credit_churn.columns = ['CreditScoreBand', 'ChurnRate']
            credit_churn['ChurnRate'] = credit_churn['ChurnRate'] * 100
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=credit_churn, x='CreditScoreBand', y='ChurnRate', 
                       palette='YlOrRd', ax=ax)
            ax.set_ylabel('Churn Rate (%)')
            ax.set_xlabel('Credit Score Band')
            ax.set_title('Churn by Credit Score')
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        with col2:
            st.markdown("#### 2. Balance Segment Analysis")
            balance_churn = filtered_df.groupby('BalanceSegment')['Exited'].mean().reset_index()
            balance_churn.columns = ['BalanceSegment', 'ChurnRate']
            balance_churn['ChurnRate'] = balance_churn['ChurnRate'] * 100
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=balance_churn, x='BalanceSegment', y='ChurnRate', 
                       palette='viridis', ax=ax)
            ax.set_ylabel('Churn Rate (%)')
            ax.set_xlabel('Balance Segment')
            ax.set_title('Churn by Balance Level')
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        # Graph 3: Balance vs Salary Scatter
        st.markdown("---")
        st.markdown("#### 3. Balance vs Salary: Churn Pattern")
        
        fig, ax = plt.subplots(figsize=(18, 5))
        sns.scatterplot(data=filtered_df, x='Balance', y='EstimatedSalary', 
                       hue='Exited', palette={0: 'green', 1: 'red'},
                       alpha=0.6, s=50, ax=ax)
        ax.set_xlabel('Account Balance (€)')
        ax.set_ylabel('Estimated Salary (€)')
        ax.set_title('Financial Profile: Churn Pattern')
        ax.legend(labels=['Retained', 'Churned'])
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close()
        
        # Graph 4 & 5: Credit Score and Salary Distributions
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 4. Credit Score Distribution")
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.histplot(data=filtered_df, x='CreditScore', hue='Exited', 
                        bins=30, palette={0: 'green', 1: 'red'}, alpha=0.6, ax=ax)
            ax.set_xlabel('Credit Score')
            ax.set_ylabel('Number of Customers')
            ax.set_title('Credit Score Distribution by Churn Status')
            ax.legend(labels=['Retained', 'Churned'])
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        with col2:
            st.markdown("#### 5. Salary Distribution")
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.histplot(data=filtered_df, x='EstimatedSalary', hue='Exited', 
                        bins=30, palette={0: 'green', 1: 'red'}, alpha=0.6, ax=ax)
            ax.set_xlabel('Estimated Salary (€)')
            ax.set_ylabel('Number of Customers')
            ax.set_title('Salary Distribution by Churn Status')
            ax.legend(labels=['Retained', 'Churned'])
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        # Graph 6: Average Balance by Credit Band
        st.markdown("---")
        st.markdown("#### 6. Average Balance by Credit Score Band")
        
        balance_credit = filtered_df.groupby('CreditScoreBand')['Balance'].mean().reset_index()
        balance_credit.columns = ['CreditScoreBand', 'AvgBalance']
        
        fig, ax = plt.subplots(figsize=(18, 5))
        sns.barplot(data=balance_credit, x='CreditScoreBand', y='AvgBalance', 
                   palette='Blues_d', ax=ax)
        ax.set_ylabel('Average Balance (€)')
        ax.set_xlabel('Credit Score Band')
        ax.set_title('Average Account Balance by Credit Score Band')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close()
        
        # Insights
        st.markdown("---")
        st.markdown('<div class="section-header">🔍 Key Financial Insights</div>', unsafe_allow_html=True)
        
        total_balance_risk = filtered_df[filtered_df['Exited']==1]['Balance'].sum()
        
        st.markdown(f"""
        <div class="critical-box">
            <h4>💰 Critical Revenue Impact</h4>
            <ul>
                <li><strong>Total balance at risk: €{total_balance_risk/1e6:.1f} million</strong></li>
                <li><strong>Higher balances correlate with higher churn</strong> - service expectations not being met</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown('<div class="section-header">📊 Customer Engagement Analysis</div>', unsafe_allow_html=True)
        
        # Graph 1 & 2: Activity and Products
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 1. Active vs Inactive Impact")
            active_churn = filtered_df.groupby('IsActiveMember')['Exited'].mean().reset_index()
            active_churn.columns = ['IsActiveMember', 'ChurnRate']
            active_churn['ChurnRate'] = active_churn['ChurnRate'] * 100
            active_churn['Status'] = active_churn['IsActiveMember'].map({0: 'Inactive', 1: 'Active'})
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=active_churn, x='Status', y='ChurnRate', 
                       palette=['#e74c3c', '#2ecc71'], ax=ax)
            ax.set_ylabel('Churn Rate (%)')
            ax.set_xlabel('Membership Status')
            ax.set_title('Activity Impact on Churn')
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        with col2:
            st.markdown("#### 2. Product Portfolio Analysis")
            product_churn = filtered_df.groupby('NumOfProducts')['Exited'].mean().reset_index()
            product_churn.columns = ['NumOfProducts', 'ChurnRate']
            product_churn['ChurnRate'] = product_churn['ChurnRate'] * 100
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=product_churn, x='NumOfProducts', y='ChurnRate', 
                       palette='mako', ax=ax)
            ax.set_ylabel('Churn Rate (%)')
            ax.set_xlabel('Number of Products')
            ax.set_title('Product Count vs Churn')
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        # Graph 3 & 4: Tenure and Credit Card
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 3. Customer Tenure Analysis")
            tenure_churn = filtered_df.groupby('TenureGroup')['Exited'].mean().reset_index()
            tenure_churn.columns = ['TenureGroup', 'ChurnRate']
            tenure_churn['ChurnRate'] = tenure_churn['ChurnRate'] * 100
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=tenure_churn, x='TenureGroup', y='ChurnRate', 
                       palette='Blues_d', ax=ax)
            ax.set_ylabel('Churn Rate (%)')
            ax.set_xlabel('Tenure Group')
            ax.set_title('Churn by Customer Tenure')
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        with col2:
            st.markdown("#### 4. Credit Card Ownership Impact")
            card_churn = filtered_df.groupby('HasCrCard')['Exited'].mean().reset_index()
            card_churn.columns = ['HasCrCard', 'ChurnRate']
            card_churn['ChurnRate'] = card_churn['ChurnRate'] * 100
            card_churn['Status'] = card_churn['HasCrCard'].map({0: 'No Card', 1: 'Has Card'})
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=card_churn, x='Status', y='ChurnRate', ax=ax)
            ax.set_ylabel('Churn Rate (%)')
            ax.set_xlabel('Credit Card Ownership')
            ax.set_title('Credit Card Impact on Churn')
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        # Graph 5: Tenure Distribution
        st.markdown("---")
        st.markdown("#### 5. Tenure Distribution")
        
        fig, ax = plt.subplots(figsize=(18, 5))
        sns.histplot(data=filtered_df, x='Tenure', hue='Exited', 
                    bins=11, palette={0: 'green', 1: 'red'}, alpha=0.6, ax=ax)
        ax.set_xlabel('Tenure (years)')
        ax.set_ylabel('Number of Customers')
        ax.set_title('Customer Tenure Distribution by Churn Status')
        ax.legend(labels=['Retained', 'Churned'])
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close()
        
        # Graph 6 & 7: Product and Activity combinations
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 6. Products by Activity Status")
            prod_activity = filtered_df.groupby(['NumOfProducts', 'IsActiveMember']).size().reset_index(name='Count')
            prod_activity['Status'] = prod_activity['IsActiveMember'].map({0: 'Inactive', 1: 'Active'})
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=prod_activity, x='NumOfProducts', y='Count', hue='Status',
                       palette={'Active': '#2ecc71', 'Inactive': '#e74c3c'}, ax=ax)
            ax.set_ylabel('Number of Customers')
            ax.set_xlabel('Number of Products')
            ax.set_title('Product Portfolio by Activity Status')
            ax.legend(title='Status')
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        with col2:
            st.markdown("#### 7. Average Tenure by Products")
            tenure_products = filtered_df.groupby('NumOfProducts')['Tenure'].mean().reset_index()
            tenure_products.columns = ['NumOfProducts', 'AvgTenure']
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=tenure_products, x='NumOfProducts', y='AvgTenure', 
                       palette='rocket', ax=ax)
            ax.set_ylabel('Average Tenure (years)')
            ax.set_xlabel('Number of Products')
            ax.set_title('Average Customer Tenure by Product Count')
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        # Insights
        st.markdown("---")
        st.markdown('<div class="section-header">🔍 Key Engagement Insights</div>', unsafe_allow_html=True)
        
        active_churn_rate = filtered_df[filtered_df['IsActiveMember']==1]['Exited'].mean()*100
        inactive_churn_rate = filtered_df[filtered_df['IsActiveMember']==0]['Exited'].mean()*100
        
        st.markdown(f"""
        <div class="critical-box">
            <h4>🚨 Engagement Crisis</h4>
            <ul>
                <li><strong>Inactive members: {inactive_churn_rate:.2f}% churn</strong> vs {active_churn_rate:.2f}% for active</li>
                <li><strong>Product complexity paradox:</strong> 3-4 products show critically high churn</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab5:
        st.markdown('<div class="section-header">🎯 High-Value Customer Analysis</div>', unsafe_allow_html=True)
        
        high_value = filtered_df[filtered_df['HighValueCustomer'] == 1]
        regular = filtered_df[filtered_df['HighValueCustomer'] == 0]
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("High-Value Customers", f"{len(high_value):,}")
        with col2:
            st.metric("HV Churn Rate", f"{high_value['Exited'].mean()*100:.1f}%")
        with col3:
            hv_churned = high_value[high_value['Exited'] == 1]
            st.metric("HV Churned", f"{len(hv_churned):,}")
        with col4:
            st.metric("Balance at Risk", f"€{hv_churned['Balance'].sum()/1e6:.1f}M")
        
        st.markdown("---")
        
        # Graph 1 & 2: HV vs Regular and Geography
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 1. High-Value vs Regular")
            comparison = pd.DataFrame({
                'CustomerType': ['Regular', 'High-Value'],
                'ChurnRate': [regular['Exited'].mean()*100, high_value['Exited'].mean()*100]
            })
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=comparison, x='CustomerType', y='ChurnRate',
                       palette=['#95a5a6', '#f39c12'], ax=ax)
            ax.set_ylabel('Churn Rate (%)')
            ax.set_xlabel('Customer Segment')
            ax.set_title('Customer Value vs Churn')
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        with col2:
            st.markdown("#### 2. HV Churn by Geography")
            hv_geo_churn = high_value.groupby('Geography')['Exited'].mean().reset_index()
            hv_geo_churn.columns = ['Country', 'ChurnRate']
            hv_geo_churn['ChurnRate'] = hv_geo_churn['ChurnRate'] * 100
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=hv_geo_churn, x='Country', y='ChurnRate', ax=ax)
            ax.set_ylabel('Churn Rate (%)')
            ax.set_xlabel('Country')
            ax.set_title('HV Customer Churn by Country')
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        # Graph 3 & 4: HV by Age and Activity
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 3. HV Customers by Age Group")
            hv_age = high_value.groupby('AgeGroup').size().reset_index(name='Count')
            
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=hv_age, x='AgeGroup', y='Count', 
                       palette='Oranges', ax=ax)
            ax.set_ylabel('Number of HV Customers')
            ax.set_xlabel('Age Group')
            ax.set_title('High-Value Customer Distribution by Age')
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        with col2:
            st.markdown("#### 4. HV Activity Status")
            hv_activity = high_value.groupby('IsActiveMember').size().reset_index(name='Count')
            hv_activity['Status'] = hv_activity['IsActiveMember'].map({0: 'Inactive', 1: 'Active'})
            
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.pie(hv_activity['Count'], labels=hv_activity['Status'], 
                   autopct='%1.1f%%', startangle=90, 
                   colors=['#e74c3c', '#2ecc71'])
            ax.set_title('HV Customer Activity Distribution')
            ax.axis('equal')
            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close()
        
        # Graph 5: HV Balance Distribution
        st.markdown("---")
        st.markdown("#### 5. High-Value Customer Balance Distribution")
        
        fig, ax = plt.subplots(figsize=(18, 5))
        sns.histplot(data=high_value, x='Balance', hue='Exited', 
                    bins=30, palette={0: 'green', 1: 'red'}, alpha=0.6, ax=ax)
        ax.set_xlabel('Account Balance (€)')
        ax.set_ylabel('Number of HV Customers')
        ax.set_title('HV Customer Balance Distribution by Churn Status')
        ax.legend(labels=['Retained', 'Churned'])
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close()
        
        # Insights
        st.markdown("---")
        st.markdown('<div class="section-header">🔍 Key High-Value Insights</div>', unsafe_allow_html=True)
        
        hv_churn_rate = high_value['Exited'].mean()*100
        hv_total_balance = hv_churned['Balance'].sum()
        
        st.markdown(f"""
        <div class="critical-box">
            <h4>🚨 Premium Customer Crisis</h4>
            <ul>
                <li><strong>High-value churn: {hv_churn_rate:.2f}%</strong></li>
                <li><strong>€{hv_total_balance/1e6:.1f} million in deposits at risk</strong></li>
                <li><strong>Immediate premium customer success program needed</strong></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; color: #95a5a6; padding: 30px 0;'>
            <p><strong>European Bank Customer Churn Analytics Dashboard</strong></p>
            <p>Developed by: <a href="https://www.linkedin.com/in/ayushman-gupta647646">Ayushman Gupta</a></p>
            <p>Mentored by: <a href="https://saikagne.github.io/">Saiprasad Kagne</a></p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
