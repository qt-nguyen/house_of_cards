import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px


class Decomposer:
    @staticmethod
    def svd(matrix, k=None):
        """
        Perform SVD on the input matrix.
        
        Parameters:
            matrix: list[list] or np.ndarray — input data
            k: int or None — number of singular values to keep (optional)

        Returns:
            U_k, S_k, Vt_k — truncated SVD components
        """
        A = np.array(matrix)
        U, S, Vt = np.linalg.svd(A, full_matrices=False)

        if k is not None:
            U = U[:, :k]
            S = S[:k]
            Vt = Vt[:k, :]

        return U, S, Vt
    
    @staticmethod
    def plot_latent_space_plotly(U: np.ndarray, factor_indices: list, label, color, html_path: str = "latent_space.html"):
        """
        Plots a 2D latent space map using Plotly with hover labels and color coding.
        
        Parameters:
        - U: NumPy array from SVD (left singular vectors), shape [n_samples, n_factors]
        - factor_indices: Two indices from U specifying the latent dimensions to plot
        - label: Optional 1D array of hover labels (e.g. names)
        - color: Optional 1D array of values for dot coloring (e.g. party)
        - html_path: Output path for the HTML file
        """
        x_idx, y_idx = factor_indices
        df_plot = pd.DataFrame({
            f"Factor {x_idx}": U[:, x_idx],
            f"Factor {y_idx}": U[:, y_idx],
            "Label": label if label is not None else np.arange(U.shape[0]),
            "Color": color if color is not None else "gray"
        })

        fig = px.scatter(
            df_plot,
            x=f"Factor {x_idx}",
            y=f"Factor {y_idx}",
            color=df_plot["Color"],
            hover_name="Label",
            title=f"2D Latent Space Visualization (Factors {x_idx} & {y_idx})",
            width=800,
            height=600
        )
        fig.write_html(html_path)
        print(f"Plot saved to {html_path}")