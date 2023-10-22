# Monte Carlo Option Pricing

This project provides a Python script to perform Monte Carlo simulations for option pricing. It's especially useful for complex options with various features and payoffs. Additionally, the project includes a Streamlit web app for visualizing the results. The final result is deployed as [Monte Carlo Option Pricing Web App](https://monte-carlo-python-dt2dhksgf6cyltzm3seiad.streamlit.app/)

Feel free to follow [this Medium article](https://medium.com/python-in-plain-english/mastering-financial-engineering-from-python-simulations-to-interactive-apps-3b5975ffa48c) for detailed instructions.

## Features

- Monte Carlo simulation for option pricing.
- Visualize simulated price paths and option payoffs.
- Deployed as a Streamlit web app.

### Prerequisites

- Python (3.7 or higher)
- Required Python packages (install via `pip install -r requirements.txt`):
  - numpy
  - matplotlib (for local visualization)
  - plotly (for web app visualization)
  - streamlit

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/JKaterina/monte-carlo-python.git
   ```

2. Navigate to the project directory:

   ```bash
   cd monte-carlo-python
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Option Pricing Script

Run the Monte Carlo option pricing script:

```bash
python monte_carlo_sim.py
```

Follow the prompts to specify option parameters and view the estimated option price. The script can also be customized for your specific use case.

#### Web App

The project includes a Streamlit web app. To run the web app, use the following command:

```bash
streamlit run monte_carlo_app.py
```

This will launch the app locally, and you can access it via your web browser.

### Deployed Web App

The web app is deployed and accessible online at:

[Monte Carlo Option Pricing Web App](https://monte-carlo-python-dt2dhksgf6cyltzm3seiad.streamlit.app/)

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with your changes: `git checkout -b feature/your-feature-name`.
3. Commit your changes and push to your branch.
4. Create a pull request to the original repository's `main` branch.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The Monte Carlo option pricing model is based on standard financial engineering principles.
- Special thanks to the open-source Python community for the libraries and tools used in this project.

Feel free to customize the README with additional details, project-specific instructions, and acknowledgements as needed.
