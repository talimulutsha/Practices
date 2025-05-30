from flask import Flask, render_template
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

def create_plot():
    # Load dataset
    iris = sns.load_dataset('iris')
    
    # Basic analysis (exclude species column for numerical stats)
    stats = iris.drop('species', axis=1).describe().to_html()
    
    # Correlation matrix (numerical columns only)
    corr_matrix = iris.drop('species', axis=1).corr().to_html()
    
    # Create visualization
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Plot 1: Scatter plot
    sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', 
                   hue='species', ax=axes[0])
    axes[0].set_title('Sepal Length vs Width')
    
    # Plot 2: Boxplot
    sns.boxplot(data=iris, x='species', y='petal_length', ax=axes[1])
    axes[1].set_title('Petal Length by Species')
    
    plt.tight_layout()
    
    # Save plot to PNG in memory
    img = BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()
    
    return plot_url, stats, corr_matrix

@app.route('/')
def index():
    try:
        plot_url, stats, corr_matrix = create_plot()
        iris = sns.load_dataset('iris')
        sample_data = iris.head(10).to_html()
        
        return render_template('index.html', 
                            plot_url=plot_url,
                            stats=stats,
                            corr_matrix=corr_matrix,
                            sample_data=sample_data)
    except Exception as e:
        return f"""
        <h1>Error</h1>
        <p>{str(e)}</p>
        <p>Please check the terminal for detailed error logs.</p>
        """

if __name__ == '__main__':
    app.run(debug=True)