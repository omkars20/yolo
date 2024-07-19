import os
from src.train import train_model
from src.evaluate import evaluate_model
from src.inference import run_inference

if __name__ == "__main__":
    data_dir = '.'
    print(f"Data directory: {data_dir}")  # Debug print statement
    
    # Train the model
    train_model(data_dir)
    
    # Evaluate the model
    results = evaluate_model(data_dir)
    print(results)


