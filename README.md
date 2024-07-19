

# Smoke Detection System
![image](https://github.com/user-attachments/assets/8428b17a-2888-4913-aaf9-c2f633d9a7fb)



https://github.com/user-attachments/assets/6fb64894-44fd-483e-b953-ad8e7f48e421


## Overview

The Smoke Detection System is a machine learning project designed to identify and classify smoke from images or sensor data. This system aims to provide early detection of potential fire hazards, enhancing safety and response times in various environments, such as residential, commercial, and industrial settings.

## Features

- **Image-Based Detection**: Uses computer vision techniques to analyze images for signs of smoke.
- **Sensor Data Analysis**: Processes data from smoke detectors to identify smoke patterns.
- **Real-Time Alerts**: Generates immediate alerts to notify users of potential smoke events.
- **Scalable**: Can be integrated with existing fire safety systems and expanded to support multiple sensors or cameras.

## Technology Stack

- **Machine Learning**: Utilizes classification algorithms to differentiate between smoke and non-smoke conditions.
- **PCA (Principal Component Analysis)**: Applied for dimensionality reduction, enhancing model efficiency and performance.
- **Oversampling Techniques**: Employs methods like SMOTE to handle imbalanced datasets, ensuring reliable detection.
- **Standard Scaler**: Standardizes features to improve model accuracy and consistency.

## Data

The model is trained on a dataset comprising:
- Images labeled with smoke and non-smoke conditions.
- Sensor data from various smoke detection devices.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smoke-detection.git
   ```

2. Navigate to the project directory:
   ```bash
   cd smoke-detection
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare Data**: Ensure your data is in the correct format and located in the specified directories.
2. **Run the Model**: Execute the script to train the model and test it with sample data.
   ```bash
   python train_model.py
   python test_model.py
   ```

3. **Integration**: Use the trained model in your application to detect smoke and trigger alerts.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. For significant changes, open an issue first to discuss the modifications.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out to [your-email@example.com](mailto:your-email@example.com).

---

Feel free to customize this template further based on the specifics of your project, including adding any additional features or instructions that are relevant.
