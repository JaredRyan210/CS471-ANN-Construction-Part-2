## Overview

This project focuses on constructing an Artificial Neural Network (ANN) classifier to recognize handwritten letters from the A-Z dataset. The primary objectives include working with large datasets, understanding statistical learning using ANN, and tuning hyperparameters for optimal performance.

## Dataset

The dataset contains 785 columns:
- The first column represents letters A to Z, encoded as integers (0 to 25).
- Columns 2 to 785 contain grayscale pixel values (0 to 255) of a 28x28 image.

## Dataset Sources

- [NIST Special Database 19](https://www.nist.gov/srd/nist-special-database-19)
- [A_Z Handwritten Data.csv](https://www.kaggle.com/datasets/sachinpatel21/az-handwritten-alphabets-in-csv-format)

## Project Structure

- **ANN_HW.py**: Initial ANN implementation.
- **ANN_HW_PART2.py**: Extended ANN implementation with additional features and visualizations.
- **Links.txt**: Useful links for reference.
- **Notes.txt**: Notes and additional information.
- **ch.py**: Script to generate column definitions for SQLite.
- **data.csv**: Dataset file.
- **generate_select.py**: Script to generate SQL select statements.
- **network.csv**: Network structure configuration.
- **network.txt**: Text file with network data.
- **normalize_cols.py**: Script to normalize columns in the dataset.

## Steps to Run

1. **Prepare the Dataset**:
   - Import the dataset using SQLite.
   - Normalize the data for better performance.
2. **Initialize the Network**:
  - Define the network structure.
  - Initialize nodes and connections.
3. **Train the Network**:
  - Use the provided scripts to train the network on the dataset.
  - Experiment with different hyperparameters and document the results.
4. **Test the Network**:
  - Evaluate the network’s performance on test data.
  - Calculate accuracy and visualize the results.
 
